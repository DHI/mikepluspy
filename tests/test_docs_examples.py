"""Run the docs' code examples against copies of a test database.

This is the runtime half of ``scripts/lint_docs_examples.py``. The static linter cannot
see what a call does at runtime: that ``insert()`` has already run, or that a property
setter rejects a string. Running the examples does.

Each user guide page, and the ``>>>`` examples of each module's docstrings, run top to
bottom in one namespace, as a reader would run them. ``mp`` and ``db`` are bound before
the first block (``db`` to a copy of the Sirius database), and every ``.sqlite`` path
passed to ``mp.open`` or ``Database`` is created as another copy, so placeholder paths
such as ``"path/to/model.sqlite"`` work. The working directory is a temporary one.

A block is not run when its fence has the class ``.no-run`` (```` ```{.python .no-run} ````)
or it contains a bare ``...`` statement. An error is counted as a skip, not a failure,
when it names a path written in the example that does not exist, or a name that a
``# Assuming 'x' is ...`` comment leaves to the reader. Anything else fails the test.
"""

from __future__ import annotations

import ast
import contextlib
import importlib
import io
import re
import shutil
import sys
import traceback
from functools import cache
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lint_docs_examples import (
    ASSUMING,
    Package,
    Snippet,
    doc_pages,
    docstring_pages,
)

pytestmark = [pytest.mark.license_required, pytest.mark.slow]

USER_GUIDE = sorted((ROOT / "docs" / "user_guide").glob("*.qmd"))
DOCSTRING_MODULES = sorted(
    path
    for path in (ROOT / "mikeplus").rglob("*.py")
    if "auto_generated" not in path.parts and ">>>" in path.read_text(encoding="utf-8")
)
DB_SUFFIXES = {".sqlite", ".mupp"}
OPENERS = {"open", "Database"}
PATH_LITERAL = re.compile(
    r"[\w.\-]*[/\\][\w./\\\- ]+\.\w+|[\w\-]+\.(?:xml|inp|dfs\d|shp|res1d)"
)


@cache
def package() -> Package:
    """Load the package once for every docstring test."""
    return Package()


def placeholder_paths(snippets: list[Snippet]) -> set[str]:
    """Return the database paths the examples open, e.g. ``mp.open("model.sqlite")``."""
    paths = set()
    for snippet in snippets:
        try:
            tree = ast.parse(snippet.source)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not (isinstance(node, ast.Call) and node.args):
                continue
            func = node.func
            name = (
                func.attr
                if isinstance(func, ast.Attribute)
                else getattr(func, "id", "")
            )
            first = node.args[0]
            if (
                name in OPENERS
                and isinstance(first, ast.Constant)
                and isinstance(first.value, str)
                and Path(first.value).suffix in DB_SUFFIXES
            ):
                paths.add(first.value)
    return paths


def copy_database(source: Path, target: Path) -> None:
    """Copy a test database folder so that its ``.sqlite`` is at ``target``."""
    if target.with_suffix(".sqlite").exists():
        return
    shutil.copytree(
        source.parent,
        target.parent,
        dirs_exist_ok=True,
        ignore=lambda _, names: [n for n in names if Path(n).suffix in DB_SUFFIXES],
    )
    shutil.copy2(source, target.with_suffix(".sqlite"))


def is_placeholder(snippet: Snippet) -> bool:
    """Whether a block is illustration only: it has a bare ``...`` statement."""
    try:
        tree = ast.parse(snippet.source)
    except SyntaxError:
        return False
    return any(
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and node.value.value is Ellipsis
        for node in ast.walk(tree)
    )


def skip_reason(
    error: BaseException, snippet: Snippet, assumed: set[str]
) -> str | None:
    """Return why an error is the example's placeholder, not a mismatch, or None."""
    if isinstance(error, NameError) and error.name in assumed:
        return f"'{error.name}' is left to the reader"
    message = str(error)
    for literal in PATH_LITERAL.findall(snippet.source):
        named = literal in message.replace("\\", "/") or Path(literal).name in message
        if named and not Path(literal).exists():
            return f"placeholder path {literal!r}"
    return None


def snippet_filename(snippet: Snippet) -> str:
    """Return the name a snippet is compiled under, unique to it among the frames."""
    return f"<doc {snippet.path}:{snippet.line}>"


def error_line(error: BaseException, snippet: Snippet) -> int:
    """Return the doc line an error was raised from."""
    frames = [
        f
        for f in traceback.extract_tb(error.__traceback__)
        if f.filename == snippet_filename(snippet)
    ]
    return frames[-1].lineno if frames and frames[-1].lineno else snippet.line


def needs_db(snippets: list[Snippet]) -> bool:
    """Whether a page uses ``db`` or opens a database path."""
    return bool(placeholder_paths(snippets)) or any(
        re.search(r"\bdb\b", s.source) for s in snippets
    )


def run_page(
    snippets: list[Snippet], workdir: Path, source_db: Path, namespace: dict
) -> None:
    """Run a page's snippets in order and fail with every error that is not a placeholder."""
    for placeholder in placeholder_paths(snippets):
        copy_database(source_db, workdir / placeholder)
    import mikeplus

    namespace.setdefault("mp", mikeplus)
    opened = None
    if any(re.search(r"\bdb\b", s.source) for s in snippets):
        opened = namespace["db"] = mikeplus.open(source_db)
    assumed = {m.group("name") for s in snippets for m in ASSUMING.finditer(s.source)}
    failures, skips = [], []
    try:
        for snippet in snippets:
            where = f"{snippet.path.relative_to(ROOT)}:{snippet.line}"
            if ".no-run" in snippet.attrs or is_placeholder(snippet):
                skips.append(f"{where}: not run (marked .no-run or has a bare ...)")
                continue
            try:
                tree = ast.parse(snippet.source)
            except SyntaxError as error:
                skips.append(f"{where}: does not parse ({error.msg})")
                continue
            ast.increment_lineno(tree, snippet.line - 1)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(compile(tree, snippet_filename(snippet), "exec"), namespace)  # noqa: S102 - running the docs is the test
            except Exception as error:
                line = error_line(error, snippet)
                text = f"{snippet.path.relative_to(ROOT)}:{line}: {type(error).__name__}: {error}"
                reason = skip_reason(error, snippet, assumed)
                (skips if reason else failures).append(
                    f"{text.splitlines()[0]} [skipped: {reason}]" if reason else text
                )
    finally:
        for value in [opened, *namespace.values()]:
            if isinstance(value, mikeplus.Database):
                with contextlib.suppress(Exception):
                    value.close()
    if skips:
        print("\n".join(["", *skips]))
    assert not failures, "\n\n".join(failures)


@pytest.fixture
def workdir(tmp_path, monkeypatch) -> Path:
    """Run each page from an empty working directory."""
    path = tmp_path / "work"
    path.mkdir()
    monkeypatch.chdir(path)
    return path


@pytest.mark.parametrize("path", USER_GUIDE, ids=lambda p: p.name)
def test_user_guide_page_runs(path, sirius_db, workdir):
    """Each user guide page runs from top to bottom."""
    page = next(p for p in doc_pages() if p.path == path)
    run_page(page.snippets, workdir, sirius_db, {"__name__": "__docs__"})


@pytest.mark.parametrize(
    "path", DOCSTRING_MODULES, ids=lambda p: p.relative_to(ROOT / "mikeplus").as_posix()
)
def test_docstring_examples_run(path, sirius_db, tmp_path, monkeypatch):
    """The ``>>>`` examples of a module's docstrings run, each docstring on its own.

    Each docstring gets its own working directory and database copy: one that creates
    ``path/to/model.sqlite`` must not make the next one's ``mp.create`` fail.
    ``sirius_db`` itself is only copied, never opened.
    """
    pages = [p for p in docstring_pages(package()) if p.path == path]
    module_name = ".".join(path.relative_to(ROOT).with_suffix("").parts)
    module = importlib.import_module(module_name.removesuffix(".__init__"))
    errors = []
    for index, page in enumerate(pages):
        page_dir = tmp_path / f"page{index}"
        workdir = page_dir / "work"
        workdir.mkdir(parents=True)
        page_db = page_dir / "db" / sirius_db.name
        if needs_db(page.snippets):
            copy_database(sirius_db, page_db)
        monkeypatch.chdir(workdir)
        try:
            run_page(page.snippets, workdir, page_db, dict(vars(module)))
        except AssertionError as error:
            errors.append(str(error))
    assert not errors, "\n\n".join(errors)
