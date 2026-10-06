"""Check that the code examples in the docs agree with the package's real API.

The examples are the Python code blocks of the user guide, README and notebooks, and the
``>>>`` examples in docstrings. Each page is written out as one module, its blocks in
order, so a name bound in one block is known in the next. ``mp`` is imported and ``db``
is a ``Database``; a docstring's examples also see the names of the module that defines
them, as doctest would. A comment such as ``# Assuming 'alt' is an Alternative object``
gives ``alt`` that type. Then:

pyrefly          type-checks the modules against the package source (unknown attributes,
                 keywords and imports, wrong argument types and ``Literal`` values,
                 read-only properties, ...); a finding is named after pyrefly's error kind
ast-grep         applies the rules in ``scripts/docs_examples/``, e.g. ``query-reused``
docstring-*      griffe checks the ``Methods`` and ``Attributes`` sections of class
                 docstrings against the class

Nothing is imported, so no MIKE+ install is needed. ruff's DOC102 covers ``Parameters``.

Usage
-----
    just docs-examples          # or: python scripts/lint_docs_examples.py

Exits 1 when there are findings. Output is ``path:line: check message``.
"""

from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import griffe

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = "mikeplus"
RULES = ROOT / "scripts" / "docs_examples"

DOC_SUFFIXES = {".qmd", ".md", ".ipynb"}

# Generated per table; their docstrings hold no examples and parsing them takes most of the time.
SKIP_DOCSTRINGS_IN = f"{PACKAGE}.tables.auto_generated"

# Bases that add no attributes a docstring section would name.
NEUTRAL_BASES = {"abc.ABC", "typing.Generic", "object", "builtins.object"}

# Placeholders such as `repair_tool` or `group` that a page leaves to the reader.
DISABLED_ERRORS = ["unknown-name"]

# The examples assume a lookup such as `by_name()` or `execute()` finds what it looks for,
# so using its `X | None` result as an `X` is not a mismatch. pyrefly has no error kind
# of its own for that, so these are recognised by their messages.
ASSUMES_FOUND = re.compile(
    r"^Object of class `NoneType` has no attribute|`[^`]+ \| None` is not assignable"
)

PRELUDE = [
    "import mikeplus as mp",
    "from typing import cast as _cast",
    "db = _cast(mp.Database, None)",
]

ASSUMING = re.compile(
    r"#\s*(?:Assuming\s+)?'?(?P<name>[A-Za-z_]\w*)'?\s+is\s+(?:a|an|your)\b[^\n]*?"
    r"\b(?P<cls>(?:\w+\.)*[A-Z]\w*)\s+object"
)
FENCE = re.compile(
    r"^(?P<indent>[ \t]*)```[ \t]*\{?\.?python(?P<attrs>[^\n]*)\n(?P<body>.*?)^(?P=indent)```",
    re.DOTALL | re.MULTILINE,
)
IMPORTED = re.compile(r"^\s*(?:import|from)\s+([A-Za-z_]\w*)", re.MULTILINE)
NOTEBOOK_SOURCE = re.compile(r'^[ \t]*"source": \[(?:\]|$)', re.MULTILINE)


@dataclass(frozen=True)
class Finding:
    """A problem found by one of the checks."""

    path: Path
    line: int
    check: str
    message: str

    def __str__(self) -> str:
        """Format as ``path:line: check message``."""
        return f"{self.path.relative_to(ROOT)}:{self.line}: {self.check} {self.message}"


# --- The package ----------------------------------------------------------------------


class Package:
    """The package as griffe sees it, and lookups on it."""

    def __init__(self, search_path: Path = ROOT) -> None:
        """Load the package statically from the directory that contains it."""
        self.loader = griffe.GriffeLoader(
            search_paths=[str(search_path)], docstring_parser="numpy"
        )
        # By path: by name, griffe also searches sys.path and the editable install's .pth.
        self.root = self.loader.load(search_path / PACKAGE)
        self.loader.resolve_aliases(external=False, implicit=False)
        self._class_names: dict[str, Any] | None = None
        self._subclasses: dict[str, list[Any]] | None = None

    def class_names(self) -> dict[str, Any]:
        """Return every class in the package by its name."""
        if self._class_names is None:
            self._class_names = {}
            for obj in walk(self.root, generated=True):
                if obj.is_class:
                    self._class_names.setdefault(obj.name, obj)
        return self._class_names

    def subclass_has(self, cls: Any, attr: str) -> bool:
        """Whether a subclass of ``cls`` has ``attr``; the object may be one at runtime."""
        if self._subclasses is None:
            self._subclasses = {}
            for obj in walk(self.root, generated=True):
                if obj.is_class:
                    for base in obj.resolved_bases:
                        self._subclasses.setdefault(base.path, []).append(obj)
        pending, seen = list(self._subclasses.get(cls.path, [])), set()
        while pending:
            sub = pending.pop()
            if sub.path in seen:
                continue
            seen.add(sub.path)
            if attr in sub.all_members:
                return True
            pending.extend(self._subclasses.get(sub.path, []))
        return False

    def may_have(self, cls: Any, attr: str) -> bool:
        """Whether an instance of ``cls`` may have ``attr`` though griffe lists no such member."""
        return assigns_self(cls, attr) or self.subclass_has(cls, attr)


def assigns_self(cls: Any, attr: str) -> bool:
    """Whether a method of ``cls`` or of a package base assigns ``self.attr``.

    griffe records only the ``self.x`` assignments made in ``__init__``.
    """
    pattern = re.compile(rf"\bself\.{re.escape(attr)}\s*(?::[^=\n]+)?=(?!=)")
    pending, seen = [cls], set()
    while pending:
        current = pending.pop()
        if current.path in seen:
            continue
        seen.add(current.path)
        if pattern.search(current.source):
            return True
        pending.extend(current.resolved_bases)
    return False


def final(obj: Any) -> Any:
    """Follow an alias to its target, or return None if it leads outside the package."""
    if obj is None or not obj.is_alias:
        return obj
    try:
        return obj.final_target
    except (griffe.AliasResolutionError, griffe.CyclicAliasError):
        return None


def walk(obj: Any, *, generated: bool = False):
    """Yield every non-alias object in a module tree, by default without the generated tables."""
    for member in obj.members.values():
        if member.is_alias or (
            not generated and member.path.startswith(SKIP_DOCSTRINGS_IN)
        ):
            continue
        yield member
        if member.is_module or member.is_class:
            yield from walk(member, generated=generated)


def is_closed(cls: Any, seen: set[str] | None = None) -> bool:
    """Whether every attribute of a class is known: no ``__getattr__``, no foreign bases."""
    seen = seen if seen is not None else set()
    if cls.path in seen:
        return True
    seen.add(cls.path)
    if "__getattr__" in cls.all_members or "__getattribute__" in cls.all_members:
        return False
    for base in cls.bases:
        expr = base.left if isinstance(base, griffe.ExprSubscript) else base
        path = getattr(expr, "canonical_path", str(expr))
        if path in NEUTRAL_BASES:
            continue
        if not path.startswith(f"{PACKAGE}."):
            return False
    return all(is_closed(base, seen) for base in cls.resolved_bases)


# --- Snippets -------------------------------------------------------------------------


@dataclass
class Snippet:
    """Code to check, with where it came from."""

    path: Path
    line: int
    source: str
    scope: Any = None  # the module a docstring example belongs to
    attrs: str = ""  # what follows ```python or ```{.python on the fence line


@dataclass
class Page:
    """Snippets checked as one session, in order."""

    path: Path
    snippets: list[Snippet] = field(default_factory=list)


def doc_files() -> list[Path]:
    """Return the tracked docs, notebooks and README."""
    try:
        tracked = subprocess.run(
            ["git", "ls-files", "docs", "notebooks", "README.md"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        paths = [ROOT / p for p in tracked]
    except (OSError, subprocess.CalledProcessError):
        paths = [*ROOT.glob("docs/**/*"), *ROOT.glob("notebooks/*"), ROOT / "README.md"]
    return sorted(p for p in paths if p.suffix in DOC_SUFFIXES and p.is_file())


def code_blocks(text: str):
    """Yield (first line, attributes, source) for each Python fence in Markdown."""
    for match in FENCE.finditer(text):
        body = textwrap.dedent(match.group("body"))
        yield text.count("\n", 0, match.start("body")) + 1, match.group("attrs"), body


def notebook_snippets(path: Path, text: str) -> list[Snippet]:
    """Return a notebook's code cells, each at the line of the JSON file its source starts on.

    nbformat writes one source line per JSON line, so a finding's line can be opened in
    the file. A notebook written otherwise is numbered as if its cells were concatenated.
    """
    cells = json.loads(text).get("cells", [])
    sources = ["".join(cell.get("source", [])) for cell in cells]
    starts = [text.count("\n", 0, m.end()) + 2 for m in NOTEBOOK_SOURCE.finditer(text)]
    if len(starts) != len(cells):
        starts, line = [], 1
        for source in sources:
            starts.append(line)
            line += source.count("\n") + 1
    return [
        Snippet(path, start, source)
        for cell, start, source in zip(cells, starts, sources, strict=True)
        if cell.get("cell_type") == "code"
    ]


def doc_pages() -> list[Page]:
    """Return the user guide, README and notebooks as pages of snippets."""
    pages = []
    for path in doc_files():
        text = path.read_text(encoding="utf-8")
        page = Page(path)
        if path.suffix == ".ipynb":
            page.snippets = notebook_snippets(path, text)
        else:
            for line, attrs, body in code_blocks(text):
                page.snippets.append(Snippet(path, line, body, attrs=attrs))
        pages.append(page)
    return pages


def docstring_lines(docstring: Any) -> list[str]:
    """Return a docstring's lines as written, line ``i`` being at ``lineno + i``.

    The cleaned ``value`` drops a blank first line, which would shift every line by one.
    """
    try:
        return docstring.source.splitlines()
    except ValueError:
        return docstring.value.splitlines()


def docstring_pages(package: Package) -> list[Page]:
    """Return the ``>>>`` examples of each docstring as a page of its own."""
    pages = []
    for obj in walk(package.root):
        docstring = obj.docstring
        if docstring is None:
            continue
        module = obj if obj.is_module else obj.module
        lines = docstring_lines(docstring)
        code, first = [], None
        for index, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith(">>>") or (code and stripped.startswith("...")):
                first = first if first is not None else index
                code.append(stripped[3:].removeprefix(" "))
            elif code:
                code.append("")  # output and prose stay as blanks to keep line numbers
        if code:
            path = Path(module.filepath)
            snippet = Snippet(path, docstring.lineno + first, "\n".join(code), module)
            pages.append(Page(path, [snippet]))
    return pages


# --- Pages as modules -----------------------------------------------------------------


@dataclass
class Module:
    """A page written out as one module, and where each of its lines came from."""

    page: Page
    lines: list[str] = field(default_factory=list)
    origins: list[tuple[Path, int] | None] = field(default_factory=list)

    def add(self, line: str, origin: tuple[Path, int] | None = None) -> None:
        """Append a line; ``origin`` is the docs line it came from, if any."""
        self.lines.append(line)
        self.origins.append(origin)

    def origin(self, line: int) -> tuple[Path, int]:
        """Return the docs line of a module line (1-based); prelude lines map to the page."""
        found = self.origins[line - 1] if 0 < line <= len(self.origins) else None
        return found or (self.page.path, 1)


def assumed_type(package: Package, cls: str) -> str | None:
    """Return the import path of a class an ``# Assuming`` comment names, or None."""
    obj = package.class_names().get(cls.rsplit(".", 1)[-1])
    return obj.path if obj is not None else None


def to_module(package: Package, page: Page) -> Module:
    """Write a page's snippets as one module, with the prelude and the assumed names."""
    module = Module(page)
    for line in PRELUDE:
        module.add(line)
    scope = page.snippets[0].scope if page.snippets else None
    if scope is not None:
        names = sorted(n for n in scope.members if not n.startswith("__"))
        if names:
            module.add(f"from {scope.path} import {', '.join(names)}")
    for snippet in page.snippets:
        for offset, line in enumerate(snippet.source.splitlines()):
            if line.lstrip().startswith(("%", "!")):
                line = ""  # notebook magics and shell escapes
            # Only a comment line: replacing a line of code would hide its errors.
            match = ASSUMING.match(line.lstrip())
            target = match and assumed_type(package, match.group("cls"))
            if match and target:
                indent = line[: len(line) - len(line.lstrip())]
                cls_module, _, cls_name = target.rpartition(".")
                line = (
                    f"{indent}import {cls_module} as _assumed; "
                    f"{match.group('name')} = _cast(_assumed.{cls_name}, None)"
                )
            module.add(line, (snippet.path, snippet.line + offset))
    return module


# --- Checks ---------------------------------------------------------------------------


def tool(name: str) -> str:
    """Return the path of a tool installed next to this Python, or on PATH."""
    scripts = Path(sys.executable).parent
    for candidate in (scripts / name, scripts / f"{name}.exe"):
        if candidate.is_file():
            return str(candidate)
    found = shutil.which(name)
    if found is None:
        raise SystemExit(f"{name} is not installed; run `just setup`")
    return found


def write_modules(modules: list[Module], directory: Path) -> dict[str, Module]:
    """Write the modules and a pyrefly config into a directory; return them by file name."""
    by_name = {}
    for index, module in enumerate(modules):
        name = f"page_{index:03d}.py"
        (directory / name).write_text("\n".join(module.lines) + "\n", encoding="utf-8")
        by_name[name] = module
    # Other packages a page imports (mikeio, contextily, ...) need not be installed.
    imported = {m for module in modules for m in IMPORTED.findall("\n".join(module.lines))}
    ignored = [p for m in sorted(imported - {PACKAGE}) for p in (m, f"{m}.*")]
    config = {
        "project-includes": ["*.py"],
        "preset": "default",
        "python-interpreter-path": sys.executable,
        "search-path": [str(ROOT)],
        "ignore-missing-imports": ignored,
    }
    lines = [f"{key} = {json.dumps(value)}" for key, value in config.items()]
    lines += ["[errors]", *(f"{error} = false" for error in DISABLED_ERRORS)]
    (directory / "pyrefly.toml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return by_name


def run_pyrefly(directory: Path, modules: dict[str, Module]) -> list[Finding]:
    """Type-check the modules with pyrefly and map its errors back to the docs."""
    result = subprocess.run(
        [tool("pyrefly"), "check", "--output-format", "json", "--summary=none"],
        cwd=directory,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    try:
        errors = json.loads(result.stdout)["errors"]
    except (json.JSONDecodeError, KeyError):
        raise SystemExit(f"pyrefly failed:\n{result.stdout}\n{result.stderr}") from None
    findings = []
    for error in errors:
        if error.get("severity", "error") != "error" or ASSUMES_FOUND.search(
            error["description"]
        ):
            continue
        module = modules.get(Path(error["path"]).name)
        if module is None:
            continue
        path, line = module.origin(error["line"])
        message = error["description"].splitlines()[0]
        findings.append(Finding(path, line, error["name"], message))
    return findings


def run_ast_grep(directory: Path, modules: dict[str, Module]) -> list[Finding]:
    """Apply each ast-grep rule to the modules and map its matches back to the docs."""
    findings = []
    for rule in sorted(RULES.glob("*.yml")):
        result = subprocess.run(
            [tool("ast-grep"), "scan", "--rule", str(rule), "--json=stream", "."],
            cwd=directory,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if result.returncode not in (0, 1):
            raise SystemExit(f"ast-grep failed on {rule.name}:\n{result.stderr}")
        for match in map(json.loads, result.stdout.splitlines()):
            module = modules.get(Path(match["file"]).name)
            if module is None:
                continue
            path, line = module.origin(match["range"]["start"]["line"] + 1)
            findings.append(Finding(path, line, match["ruleId"], match["message"]))
    return findings


def docstring_line(obj: Any, text: str) -> int:
    """Return the source line of the first docstring line containing ``text``."""
    for index, line in enumerate(docstring_lines(obj.docstring)):
        if text in line:
            return obj.docstring.lineno + index
    return obj.docstring.lineno


def check_docstring_sections(package: Package) -> list[Finding]:
    """Check ``Methods`` and ``Attributes`` sections of class docstrings against the class."""
    findings = []
    for cls in walk(package.root):
        if not cls.is_class or cls.docstring is None:
            continue
        path = Path(cls.filepath)
        for section in cls.docstring.parsed:
            if section.kind is griffe.DocstringSectionKind.attributes:
                for attribute in section.value:
                    if (
                        attribute.name not in cls.all_members
                        and is_closed(cls)
                        and not package.may_have(cls, attribute.name)
                    ):
                        findings.append(
                            Finding(
                                path,
                                docstring_line(cls, attribute.name),
                                "docstring-attrs",
                                f"{cls.name} documents attribute '{attribute.name}', "
                                "which it does not have",
                            )
                        )
            if section.kind is not griffe.DocstringSectionKind.functions:
                continue
            for entry in section.value:
                signature = str(entry.annotation or entry.name).split(" : ")[0].strip()
                line = docstring_line(cls, signature)
                method = final(cls.all_members.get(entry.name))
                if method is None or not method.is_function:
                    findings.append(
                        Finding(
                            path,
                            line,
                            "docstring-methods",
                            f"{cls.name} documents method '{entry.name}', which it does not have",
                        )
                    )
                    continue
                try:
                    documented = ast.parse(f"def {signature}: pass").body[0].args
                except SyntaxError:
                    continue
                real = {p.name for p in method.parameters}
                if any(
                    p.kind is griffe.ParameterKind.var_keyword
                    for p in method.parameters
                ):
                    continue
                for arg in [
                    *documented.posonlyargs,
                    *documented.args,
                    *documented.kwonlyargs,
                ]:
                    if arg.arg not in real:
                        findings.append(
                            Finding(
                                path,
                                line,
                                "docstring-methods",
                                f"{cls.name} documents {entry.name}({arg.arg}=...), but "
                                f"{entry.name} has no parameter '{arg.arg}'",
                            )
                        )
    return findings


# --- Main -----------------------------------------------------------------------------


def lint_pages(package: Package, pages: list[Page]) -> list[Finding]:
    """Run pyrefly and the ast-grep rules on pages of snippets."""
    modules = [to_module(package, page) for page in pages if page.snippets]
    with tempfile.TemporaryDirectory(prefix="docs-examples-") as tmp:
        directory = Path(tmp)
        by_name = write_modules(modules, directory)
        return run_pyrefly(directory, by_name) + run_ast_grep(directory, by_name)


def lint() -> list[Finding]:
    """Run every check and return the findings."""
    package = Package()
    pages = [*doc_pages(), *docstring_pages(package)]
    findings = lint_pages(package, pages) + check_docstring_sections(package)
    return sorted(
        set(findings), key=lambda f: (str(f.path), f.line, f.check, f.message)
    )


def main() -> int:
    """Print the findings; return 1 if there are any."""
    findings = lint()
    for finding in findings:
        print(finding)
    if findings:
        counts: dict[str, int] = {}
        for finding in findings:
            counts[finding.check] = counts.get(finding.check, 0) + 1
        summary = ", ".join(
            f"{count} {check}" for check, count in sorted(counts.items())
        )
        print(f"\n{len(findings)} findings: {summary}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
