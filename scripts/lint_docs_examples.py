"""Check that the code examples in the docs agree with the package's real API.

The examples are the Python code blocks of the user guide, README and notebooks, the
inline code in the user guide's prose, and the ``>>>`` examples in docstrings. They are
read with griffe, which parses the package statically: nothing is imported, so .NET is
never loaded and no MIKE+ install is needed.

Each page is checked top to bottom like one interpreter session, so a name bound in one
block is known in the next. A docstring example also sees the names of the module that
defines it, as doctest would. Types are inferred from the package's annotations, and from
the numpydoc ``Returns`` section where a function has no return annotation. A name a page
uses before binding it gets a type from a comment such as ``# Assuming 'alt' is an
Alternative object``; ``db`` is assumed to be a ``Database``.

Anything whose type cannot be inferred is skipped, not flagged, so a finding should
always be a real mismatch. Commented-out statements are checked too, since readers copy
them; a finding in one says so.

Checks
------
unknown-module      an import names a module the package does not have
unknown-import      ``from mikeplus.x import y`` where x has no y
unknown-attribute   an attribute a module or a package class does not have
unknown-name        inline code names a class that does not exist but nearly matches one
unknown-keyword     a call passes a keyword its signature does not take
too-many-arguments  a call passes more positional arguments than the signature takes
missing-argument    a call leaves out a required argument
invalid-literal     a constant argument is not one of the values a ``Literal`` allows
read-only-property  an assignment to a property that has no setter
wrong-type          a literal is assigned to a property whose setter takes a package class
query-reused        a query variable runs a second time; queries run once unless reset()
docstring-methods   a ``Methods`` entry names a method or parameter the class lacks
docstring-attrs     an ``Attributes`` entry names an attribute the class lacks
docstring-params    a ``Parameters`` entry is not in the signature (griffe's own check)

Usage
-----
    just docs-examples          # or: python scripts/lint_docs_examples.py [--verbose]

Exits 1 when there are findings. Output is ``path:line: check message``; ``--verbose``
also lists the code it could not parse.
"""

from __future__ import annotations

import ast
import builtins
import collections.abc
import difflib
import importlib
import json
import logging
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import griffe

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = "mikeplus"

DOC_SUFFIXES = {".qmd", ".md", ".ipynb"}

# Generated per table; their docstrings hold no examples and parsing them takes most of the time.
SKIP_DOCSTRINGS_IN = f"{PACKAGE}.tables.auto_generated"

# Bases that add no attributes a doc example would use.
NEUTRAL_BASES = {"abc.ABC", "typing.Generic", "object", "builtins.object"}

# Names a page may use without binding them, and the class they stand for.
ASSUMED_NAMES = {"db": f"{PACKAGE}.database.Database"}

# Methods on a query that leave it runnable again.
QUERY_RESET_METHODS = {"reset"}

# Inline code in prose is evaluated only when it starts with one of these names.
INLINE_ROOTS = {"db", "mp", PACKAGE}

ASSUMING = re.compile(
    r"#\s*(?:Assuming\s+)?'?(?P<name>[A-Za-z_]\w*)'?\s+is\s+(?:a|an|your)\b[^\n]*?"
    r"\b(?P<cls>(?:\w+\.)*[A-Z]\w*)\s+object"
)
FENCE = re.compile(
    r"^(?P<indent>[ \t]*)```[ \t]*\{?\.?python(?P<attrs>[^\n]*)\n(?P<body>.*?)^(?P=indent)```",
    re.DOTALL | re.MULTILINE,
)
NOTEBOOK_SOURCE = re.compile(r'^[ \t]*"source": \[(?:\]|$)', re.MULTILINE)
INLINE_CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
CAMEL_CASE = re.compile(r"^[A-Z][a-z]+(?:[A-Z][a-z0-9]*)+$")
COMMENTED = re.compile(r"^\s*#\s?(?!\|)(?P<code>.*\S)\s*$")


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


# --- Types ----------------------------------------------------------------------------


@dataclass(eq=False)
class Type:
    """One inferred type.

    ``kind`` is ``module``, ``class`` or ``instance`` (``obj`` a griffe object),
    ``function`` (a griffe function, with the class it was looked up on as ``owner``),
    ``python`` (``obj`` a real stdlib or builtin type, with ``item`` its element type)
    or ``dict`` (a dict literal, ``keys`` its constant keys).
    """

    kind: str
    obj: Any
    owner: Any = None
    item: tuple[Type, ...] | None = None
    keys: tuple[str, ...] | None = None


# A union of types, or None when nothing is known.
Value = tuple[Type, ...] | None


def instance(obj: Any) -> Value:
    """Return the value of an instance of a griffe class or a Python type."""
    if isinstance(obj, griffe.Object):
        return (Type("instance", obj),)
    return (Type("python", obj),)


def union(*values: Value) -> Value:
    """Join values; unknown if any part is unknown."""
    types: list[Type] = []
    for value in values:
        if value is None:
            return None
        types.extend(value)
    return tuple(types) or None


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

    def get(self, path: str) -> Any:
        """Return the object at a dotted path, following aliases, or None."""
        try:
            obj = self.loader.modules_collection.get_member(path)
        except (KeyError, ValueError):
            return None
        return final(obj)

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


def python_type(path: str) -> Any:
    """Return the real stdlib or builtin object at a dotted path, or None."""
    module_name, _, name = path.rpartition(".")
    if not module_name:
        return getattr(builtins, path, None)
    if module_name.split(".")[0] not in sys.stdlib_module_names:
        return None
    try:
        return getattr(importlib.import_module(module_name), name, None)
    except ImportError:
        return None


CONTAINERS = {
    "list",
    "typing.List",
    "collections.abc.Iterator",
    "collections.abc.Iterable",
    "collections.abc.Generator",
    "collections.abc.Sequence",
    "typing.Iterator",
    "typing.Iterable",
}


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


def is_query(cls: Any) -> bool:
    """Whether a class is one of the run-once query classes."""
    return cls.path.startswith(f"{PACKAGE}.queries.") and "execute" in cls.all_members


def literal_values(annotation: Any) -> list[Any] | None:
    """Return the values a ``Literal[...]`` annotation (possibly ``| None``) allows."""
    if isinstance(annotation, griffe.ExprBinOp) and annotation.operator == "|":
        values: list[Any] = []
        for side in (annotation.left, annotation.right):
            if str(side) == "None":
                values.append(None)
                continue
            allowed = literal_values(side)
            if allowed is None:
                return None  # e.g. Literal[...] | str allows any str
            values.extend(allowed)
        return values
    if (
        isinstance(annotation, griffe.ExprSubscript)
        and getattr(annotation.left, "canonical_path", "") == "typing.Literal"
    ):
        items = annotation.slice
        elements = items.elements if isinstance(items, griffe.ExprTuple) else [items]
        try:
            return [ast.literal_eval(str(element)) for element in elements]
        except (ValueError, SyntaxError):
            return None
    return None


# --- Snippets -------------------------------------------------------------------------


@dataclass
class Snippet:
    """Code to check, with where it came from."""

    path: Path
    line: int
    source: str
    scope: Any = None  # the module a docstring example belongs to
    attrs: str = ""  # what follows ```python or ```{.python on the fence line
    commented: bool = False
    inline: bool = False  # prose writes `f()` to name a function, not to call it bare


@dataclass
class Page:
    """Snippets checked as one session, in order."""

    path: Path
    snippets: list[Snippet] = field(default_factory=list)
    inline: list[tuple[int, str]] = field(default_factory=list)


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


def inline_code(text: str):
    """Yield (line, code) for inline code outside the fences of Markdown."""
    blanked = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    for match in INLINE_CODE.finditer(blanked):
        yield blanked.count("\n", 0, match.start()) + 1, match.group(1).strip()


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
            page.inline = list(inline_code(text))
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


def parse_chunks(source: str) -> tuple[list[tuple[int, ast.Module]], list[int]]:
    """Parse source into top-level chunks, skipping the ones that do not parse.

    Returns the parsed chunks with their line offsets, and the first lines of the
    chunks that were skipped.
    """
    lines = [
        "" if line.lstrip().startswith(("%", "!", "#|")) else line
        for line in source.splitlines()
    ]
    try:
        return [(0, ast.parse("\n".join(lines)))], []
    except SyntaxError:
        pass
    starts = [i for i, line in enumerate(lines) if line[:1] not in ("", " ", "\t")]
    starts.append(len(lines))
    chunks, skipped = [], []
    i = 0
    while i < len(starts) - 1:
        for j in range(i + 1, len(starts)):
            try:
                tree = ast.parse("\n".join(lines[starts[i] : starts[j]]))
            except SyntaxError:
                continue
            chunks.append((starts[i], tree))
            i = j
            break
        else:
            skipped.append(starts[i] + 1)
            i += 1
    return chunks, skipped


def commented_statements(source: str) -> list[tuple[int, ast.Module]]:
    """Return the commented-out lines that parse as a statement on their own."""
    found = []
    for index, line in enumerate(source.splitlines()):
        match = COMMENTED.match(line)
        if not match:
            continue
        try:
            tree = ast.parse(match.group("code").strip())
        except SyntaxError:
            continue
        statement = tree.body[0] if len(tree.body) == 1 else None
        if statement is None or isinstance(statement, (ast.Pass, ast.Import)):
            continue
        if isinstance(statement, ast.Expr) and isinstance(
            statement.value, (ast.Name, ast.Constant, ast.Compare, ast.BinOp)
        ):
            continue  # prose that happens to parse: "Example", "db is open"
        if isinstance(statement, ast.AnnAssign):
            continue  # "Note: ..." parses as an annotation
        found.append((index, tree))
    return found


# --- Checking -------------------------------------------------------------------------


class Checker:
    """Infers types through a page and reports what does not match the package."""

    def __init__(self, package: Package, page: Page) -> None:
        """Start a session for one page."""
        self.package = package
        self.page = page
        self.env: dict[str, Value] = {}
        self.ran: dict[str, int] = {}  # query variables that have run, and where
        self.findings: list[Finding] = []
        self.snippet: Snippet = (
            page.snippets[0] if page.snippets else Snippet(page.path, 1, "")
        )
        self.offset = 0

    # Reporting

    def report(self, node: ast.AST, check: str, message: str) -> None:
        """Record a finding at a node of the current snippet."""
        if self.snippet.commented:
            message += " (in commented-out code)"
        line = self.snippet.line + self.offset + getattr(node, "lineno", 1) - 1
        self.findings.append(Finding(self.snippet.path, line, check, message))

    # Running

    def run(self) -> list[int]:
        """Check every snippet of the page; return the lines that could not be parsed."""
        skipped = []
        for snippet in self.page.snippets:
            self.snippet = snippet
            chunks, bad = parse_chunks(snippet.source)
            skipped.extend(snippet.line + line - 1 for line in bad)
            commented = commented_statements(snippet.source)
            assumed = {
                snippet.source.count("\n", 0, m.start()): (
                    m.group("name"),
                    m.group("cls"),
                )
                for m in ASSUMING.finditer(snippet.source)
            }
            # Interleave code, commented-out code and assumptions in line order.
            events: list[tuple[int, int, Any]] = []
            for offset, tree in chunks:
                for statement in tree.body:
                    events.append(
                        (offset + statement.lineno - 1, 1, (offset, statement))
                    )
            for index, tree in commented:
                events.append((index, 2, (index, tree.body[0])))
            for index, (name, cls) in assumed.items():
                events.append((index, 0, (name, cls)))
            for _, kind, payload in sorted(events, key=lambda e: (e[0], e[1])):
                if kind == 0:
                    self.assume(*payload)
                    continue
                offset, statement = payload
                self.offset = offset
                snippet.commented = kind == 2
                if kind == 2:
                    statement.lineno = 1
                    for node in ast.walk(statement):
                        if hasattr(node, "lineno"):
                            node.lineno = 1
                self.statement(statement)
            snippet.commented = False
        for line, code in self.page.inline:
            self.inline(line, code)
        return skipped

    def assume(self, name: str, cls_name: str) -> None:
        """Bind a name a comment says is an instance of a class, if it is unbound."""
        if name in self.env:
            return
        cls = self.package.class_names().get(cls_name.rsplit(".", 1)[-1])
        if cls is not None:
            self.env[name] = instance(cls)

    def inline(self, line: int, code: str) -> None:
        """Check inline code from prose: class names, and expressions on known roots."""
        self.snippet = Snippet(self.page.path, line, code, inline=True)
        self.offset = 0
        if CAMEL_CASE.match(code):
            names = self.package.class_names()
            if code not in names:
                close = difflib.get_close_matches(code, names, n=1, cutoff=0.85)
                if close:
                    self.report(
                        ast.Pass(lineno=1),
                        "unknown-name",
                        f"'{code}' is not a class of the package; did you mean '{close[0]}'?",
                    )
            return
        try:
            tree = ast.parse(code, mode="eval")
        except SyntaxError:
            return
        root = tree.body
        while isinstance(root, (ast.Attribute, ast.Call, ast.Subscript)):
            root = root.func if isinstance(root, ast.Call) else root.value
        if not (isinstance(root, ast.Name) and root.id in INLINE_ROOTS):
            return
        saved_env, saved_ran = self.env, self.ran
        package = self.module_value(PACKAGE)
        self.env, self.ran = {"mp": package, PACKAGE: package}, {}
        try:
            self.expr(tree.body)
        finally:
            self.env, self.ran = saved_env, saved_ran

    # Statements

    def statement(self, node: ast.stmt) -> None:
        """Check a statement and update the session's bindings."""
        if isinstance(node, ast.Import):
            for alias in node.names:
                self.import_module(node, alias)
        elif isinstance(node, ast.ImportFrom):
            self.import_from(node)
        elif isinstance(node, ast.Assign):
            value = self.expr(node.value)
            for target in node.targets:
                self.assign(target, value, node.value)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            value = self.expr(node.value) if node.value is not None else None
            self.assign(
                node.target, value if isinstance(node, ast.AnnAssign) else None, None
            )
        elif isinstance(node, ast.Expr):
            self.expr(node.value)
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            for item in node.items:
                value = self.enter(self.expr(item.context_expr))
                if item.optional_vars is not None:
                    self.assign(item.optional_vars, value, None)
            self.body(node.body)
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            self.assign(node.target, self.iterate(self.expr(node.iter)), None)
            self.body(node.body)
            self.body(node.orelse)
        elif isinstance(node, ast.If):
            self.expr(node.test)
            self.branches([node.body, node.orelse])
        elif isinstance(node, ast.While):
            self.expr(node.test)
            self.body(node.body)
            self.body(node.orelse)
        elif isinstance(node, (ast.Try, ast.TryStar)):
            for handler in node.handlers:
                if handler.name:
                    self.env[handler.name] = None
            self.branches(
                [node.body + node.orelse, *(handler.body for handler in node.handlers)]
            )
            self.body(node.finalbody)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            self.env[node.name] = None
        elif isinstance(node, (ast.Return, ast.Delete, ast.Raise, ast.Assert)):
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.expr):
                    self.expr(child)

    def body(self, statements: list[ast.stmt]) -> None:
        """Check a block of statements."""
        for statement in statements:
            self.statement(statement)

    def branches(self, blocks: list[list[ast.stmt]]) -> None:
        """Check alternative blocks, each from the runs before them, then join the runs.

        Bindings are not joined: each block's bindings apply in order.
        """
        before, ran = self.ran, {}
        for block in blocks:
            self.ran = dict(before)
            self.body(block)
            ran |= self.ran
        self.ran = ran

    def assign(self, target: ast.expr, value: Value, source: ast.expr | None) -> None:
        """Bind an assignment target."""
        if isinstance(target, ast.Name):
            if self.snippet.commented and target.id in self.env:
                return  # commented-out alternatives must not replace what the page bound
            self.env[target.id] = value
            self.ran.pop(target.id, None)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for element in target.elts:
                self.assign(element, None, None)
        elif isinstance(target, ast.Attribute):
            self.set_attribute(target, source)
        elif isinstance(target, ast.Subscript):
            self.expr(target.value)

    def set_attribute(self, target: ast.Attribute, source: ast.expr | None) -> None:
        """Check an assignment to an attribute of a package object."""
        owner = self.expr(target.value)
        if owner is None or len(owner) != 1 or owner[0].kind != "instance":
            return
        cls = owner[0].obj
        member = final(cls.all_members.get(target.attr))
        if member is None:
            if (
                is_closed(cls)
                and not target.attr.startswith("_")
                and not self.package.may_have(cls, target.attr)
            ):
                self.report(
                    target,
                    "unknown-attribute",
                    f"{cls.name} has no attribute '{target.attr}'",
                )
            return
        if not (member.is_attribute and "property" in member.labels):
            return
        if "writable" not in member.labels:
            self.report(
                target,
                "read-only-property",
                f"{cls.name}.{target.attr} is a read-only property",
            )
            return
        setter = getattr(member, "setter", None)
        if (
            setter is None
            or not isinstance(source, ast.Constant)
            or source.value is None
        ):
            return
        parameters = [p for p in setter.parameters if p.name != "self"]
        if not parameters:
            return
        expected = self.annotation(parameters[0].annotation, cls)
        if expected and all(t.kind == "instance" for t in expected):
            names = " or ".join(t.obj.name for t in expected)
            self.report(
                target,
                "wrong-type",
                f"{cls.name}.{target.attr} takes a {names}, not a "
                f"{type(source.value).__name__} literal",
            )

    # Imports

    def module_value(self, path: str) -> Value:
        """Return the value of a package module, or None if there is no such module."""
        obj = self.package.get(path)
        return (Type("module", obj),) if obj is not None and obj.is_module else None

    def import_module(self, node: ast.Import, alias: ast.alias) -> None:
        """Check ``import mikeplus.x`` and bind its name."""
        if alias.name.split(".")[0] != PACKAGE:
            self.env[(alias.asname or alias.name).split(".")[0]] = None
            return
        if self.module_value(alias.name) is None:
            self.report(
                node, "unknown-module", f"'{alias.name}' is not a module of the package"
            )
        if alias.asname:
            self.env[alias.asname] = self.module_value(alias.name)
        else:
            self.env[PACKAGE] = self.module_value(PACKAGE)

    def import_from(self, node: ast.ImportFrom) -> None:
        """Check ``from mikeplus.x import y`` and bind the names."""
        module_name = node.module or ""
        names = [alias.asname or alias.name for alias in node.names]
        if node.level or module_name.split(".")[0] != PACKAGE:
            for name in names:
                self.env[name] = None
            return
        module = self.module_value(module_name)
        if module is None:
            self.report(
                node,
                "unknown-module",
                f"'{module_name}' is not a module of the package",
            )
            for name in names:
                self.env[name] = None
            return
        for alias in node.names:
            if alias.name == "*":
                continue
            self.env[alias.asname or alias.name] = self.member_of_module(
                node, module[0].obj, alias.name, "unknown-import"
            )

    # Expressions

    def expr(self, node: ast.expr) -> Value:
        """Infer the value of an expression, checking it on the way."""
        if isinstance(node, ast.Name):
            return self.name(node.id)
        if isinstance(node, ast.Attribute):
            return self.attribute(node, self.expr(node.value))
        if isinstance(node, ast.Call):
            return self.call(node)
        if isinstance(node, ast.Subscript):
            value = self.expr(node.value)
            self.expr(node.slice)
            if isinstance(node.slice, ast.Slice):
                return value if value and value[0].kind == "python" else None
            return self.subscript(value)
        if isinstance(node, ast.Constant):
            return None if node.value is None else instance(type(node.value))
        if isinstance(node, ast.Dict):
            for child in [*node.keys, *node.values]:
                if child is not None:
                    self.expr(child)
            keys = tuple(
                k.value
                for k in node.keys
                if isinstance(k, ast.Constant) and isinstance(k.value, str)
            )
            complete = len(keys) == len(node.keys)
            return (Type("dict", dict, keys=keys),) if complete else instance(dict)
        if isinstance(
            node,
            (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp, ast.Lambda),
        ):
            return None  # their own scope; the comprehension variables are not tracked
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.expr):
                self.expr(child)
        return None

    def name(self, name: str) -> Value:
        """Look up a name in the session, then the docstring's module, then the assumptions."""
        if name in self.env:
            return self.env[name]
        scope = self.snippet.scope
        if scope is not None and name in scope.members:
            return self.wrap(final(scope.members[name]), None)
        if name in ASSUMED_NAMES:
            return instance(self.package.get(ASSUMED_NAMES[name]))
        return None

    def wrap(self, obj: Any, owner: Any) -> Value:
        """Return the value of a griffe member looked up on a module or a class."""
        if obj is None:
            return None
        if obj.is_module:
            return (Type("module", obj),)
        if obj.is_class:
            return (Type("class", obj),)
        if obj.is_function:
            return (Type("function", obj, owner=owner),)
        if obj.is_attribute:
            return self.annotation(obj.annotation, owner)
        return None

    def member_of_module(
        self, node: ast.AST, module: Any, attr: str, check: str
    ) -> Value:
        """Look up a module member, reporting it if missing."""
        member = module.members.get(attr)
        if member is None:
            close = difflib.get_close_matches(attr, list(module.members), n=1)
            hint = f"; did you mean '{close[0]}'?" if close else ""
            self.report(node, check, f"module {module.path} has no '{attr}'{hint}")
            return None
        return self.wrap(final(member), None)

    def attribute(self, node: ast.Attribute, value: Value) -> Value:
        """Look up an attribute on every type of a value."""
        if value is None or node.attr.startswith("__"):
            return None
        if len(value) == 1 and value[0].kind == "module":
            return self.member_of_module(
                node, value[0].obj, node.attr, "unknown-attribute"
            )
        results: list[Value] = []
        missing: list[str] = []
        for t in value:
            if t.kind in ("class", "instance"):
                member = t.obj.all_members.get(node.attr)
                if member is None:
                    if not is_closed(t.obj) or self.package.may_have(t.obj, node.attr):
                        return None
                    missing.append(t.obj.name)
                    continue
                results.append(self.wrap(final(member), t.obj))
            elif t.kind in ("python", "dict"):
                if t.obj.__module__ != "builtins":
                    return None  # e.g. CompletedProcess.returncode is set per instance
                if not hasattr(t.obj, node.attr):
                    missing.append(getattr(t.obj, "__name__", str(t.obj)))
                    continue
                results.append(None)
            else:
                return None
        if missing and len(missing) == len(value):
            suggestions = [
                name
                for t in value
                if t.kind in ("class", "instance")
                for name in t.obj.all_members
                if not name.startswith("_")
            ]
            close = difflib.get_close_matches(node.attr, suggestions, n=1)
            hint = f"; did you mean '{close[0]}'?" if close else ""
            self.report(
                node,
                "unknown-attribute",
                f"{' or '.join(dict.fromkeys(missing))} has no attribute '{node.attr}'{hint}",
            )
            return None
        return union(*results)

    def subscript(self, value: Value) -> Value:
        """Infer ``value[...]``."""
        if value is None or len(value) != 1:
            return None
        t = value[0]
        if t.kind == "instance":
            getitem = final(t.obj.all_members.get("__getitem__"))
            if getitem is not None and getitem.is_function:
                return self.returns(getitem, t.obj)
        if t.kind == "python":
            return t.item
        return None

    def iterate(self, value: Value) -> Value:
        """Infer the items of ``for x in value``."""
        if value is None or len(value) != 1:
            return None
        t = value[0]
        if t.kind == "instance":
            method = final(t.obj.all_members.get("__iter__"))
            if method is not None and method.is_function:
                iterator = self.returns(method, t.obj)
                if iterator and len(iterator) == 1 and iterator[0].kind == "python":
                    return iterator[0].item
        if t.kind == "python":
            return t.item
        return None

    def enter(self, value: Value) -> Value:
        """Infer the target of ``with value as x``."""
        if value is None or len(value) != 1 or value[0].kind != "instance":
            return None
        cls = value[0].obj
        method = final(cls.all_members.get("__enter__"))
        if method is None or not method.is_function:
            return None
        return (
            self.returns(method, cls) or value
        )  # an unannotated __enter__ returns self

    def call(self, node: ast.Call) -> Value:
        """Check a call against its signature and infer what it returns."""
        callee = self.expr(node.func)
        for arg in node.args:
            self.expr(arg)
        keywords = {kw.arg: (kw, self.expr(kw.value)) for kw in node.keywords}
        if callee is None or len(callee) != 1:
            return None
        t = callee[0]
        if t.kind == "class":
            init = final(t.obj.all_members.get("__init__"))
            if init is not None and init.is_function:
                self.check_arguments(
                    node, init, keywords, f"{t.obj.name}()", skip_first=True
                )
            return instance(t.obj)
        if t.kind != "function":
            return None
        function = t.obj
        skip_first = t.owner is not None and "staticmethod" not in function.labels
        label = (
            f"{t.owner.name}.{function.name}()"
            if t.owner is not None
            else f"{function.name}()"
        )
        self.check_arguments(node, function, keywords, label, skip_first)
        result = self.returns(function, t.owner)
        self.track_query(node, function, t.owner, result)
        return result

    def check_arguments(
        self,
        node: ast.Call,
        function: Any,
        keywords: dict[str | None, tuple[ast.keyword, Value]],
        label: str,
        skip_first: bool,
    ) -> None:
        """Check a call's arguments against a griffe signature."""
        if getattr(function, "overloads", None):
            return
        parameters = list(function.parameters)
        if skip_first and parameters:
            parameters = parameters[1:]
        kinds = griffe.ParameterKind
        var_positional = any(p.kind is kinds.var_positional for p in parameters)
        var_keyword = any(p.kind is kinds.var_keyword for p in parameters)
        positional = [
            p
            for p in parameters
            if p.kind in (kinds.positional_only, kinds.positional_or_keyword)
        ]
        by_name = {
            p.name: p
            for p in parameters
            if p.kind in (kinds.positional_or_keyword, kinds.keyword_only)
        }
        splat = any(isinstance(arg, ast.Starred) for arg in node.args)
        given: dict[str, ast.expr] = {}
        if not splat:
            if len(node.args) > len(positional) and not var_positional:
                self.report(
                    node,
                    "too-many-arguments",
                    f"{label} takes {len(positional)} positional arguments, "
                    f"{len(node.args)} given",
                )
            for parameter, arg in zip(positional, node.args, strict=False):
                given[parameter.name] = arg
        names: list[tuple[str, ast.expr]] = []
        unknown_splat = False
        for name, (keyword, value) in keywords.items():
            if name is not None:
                names.append((name, keyword.value))
            elif value and len(value) == 1 and value[0].kind == "dict":
                names.extend((key, keyword.value) for key in value[0].keys or ())
            else:
                unknown_splat = True
        for name, value_node in names:
            parameter = by_name.get(name)
            if parameter is None:
                if not var_keyword:
                    close = difflib.get_close_matches(
                        name, list(by_name), n=1, cutoff=0.5
                    )
                    hint = f"; did you mean '{close[0]}'?" if close else ""
                    self.report(
                        value_node,
                        "unknown-keyword",
                        f"{label} has no parameter '{name}'{hint}",
                    )
                continue
            given[name] = value_node
        for name, value_node in given.items():
            parameter = next((p for p in parameters if p.name == name), None)
            allowed = literal_values(parameter.annotation) if parameter else None
            if (
                allowed is not None
                and isinstance(value_node, ast.Constant)
                and value_node.value not in allowed
            ):
                choices = ", ".join(repr(v) for v in allowed if v is not None)
                self.report(
                    value_node,
                    "invalid-literal",
                    f"{label}: {name}={value_node.value!r} is not one of {choices}",
                )
        if splat or unknown_splat:
            return
        missing = [
            p.name
            for p in parameters
            if p.default is None
            and p.kind not in (kinds.var_positional, kinds.var_keyword)
            and p.name not in given
        ]
        if missing and not self.snippet.inline:
            self.report(
                node,
                "missing-argument",
                f"{label} is missing {', '.join(repr(m) for m in missing)}",
            )

    def returns(self, function: Any, owner: Any) -> Value:
        """Infer a function's return value from its annotation or its Returns section."""
        if function.returns is not None:
            return self.annotation(function.returns, owner)
        if function.docstring is not None:
            for section in function.docstring.parsed:
                if (
                    section.kind is griffe.DocstringSectionKind.returns
                    and section.value
                ):
                    annotation = section.value[0].annotation
                    if str(annotation).strip().lower() == "self":
                        return instance(owner) if owner is not None else None
                    return self.annotation(annotation, owner)
        return None

    def annotation(self, expr: Any, owner: Any) -> Value:
        """Turn a griffe annotation into a value; unknown for anything unrecognised."""
        if expr is None or isinstance(expr, str):
            return None
        if isinstance(expr, griffe.ExprBinOp) and expr.operator == "|":
            return self.drop_none(self.annotation(expr.left, owner), expr.right, owner)
        if isinstance(expr, griffe.ExprBoolOp) and expr.operator == "or":
            parts = [p for p in expr.values if str(p) != "None"]
            return union(*(self.annotation(p, owner) for p in parts))
        if isinstance(expr, griffe.ExprSubscript):
            left = getattr(expr.left, "canonical_path", "")
            if left in CONTAINERS:
                item_expr = expr.slice
                if isinstance(item_expr, griffe.ExprTuple):
                    item_expr = item_expr.elements[0]
                container = (
                    list if left in ("list", "typing.List") else collections.abc.Iterable
                )
                return (
                    Type("python", container, item=self.annotation(item_expr, owner)),
                )
            if left in ("typing.Optional",):
                return self.annotation(expr.slice, owner)
            return self.annotation(expr.left, owner)
        if isinstance(expr, griffe.ExprName):
            path = expr.canonical_path
            if path in ("typing.Self", "typing_extensions.Self", "Self"):
                return instance(owner) if owner is not None else None
            if path.startswith(f"{PACKAGE}."):
                obj = self.package.get(path)
                return instance(obj) if obj is not None and obj.is_class else None
            real = python_type(path)
            if not isinstance(real, type) or real in (object, type):
                return None  # an object or type[X] may have any attribute
            return instance(real)
        return None

    def drop_none(self, left: Value, right: Any, owner: Any) -> Value:
        """Join the two sides of ``X | Y``, ignoring a ``None`` side."""
        if str(right) == "None":
            return left
        return union(left, self.annotation(right, owner))

    def track_query(
        self, node: ast.Call, function: Any, owner: Any, result: Value
    ) -> None:
        """Report a query variable that runs a second time."""
        if owner is None or not is_query(owner):
            return
        root = self.same_object_root(
            node.func.value if isinstance(node.func, ast.Attribute) else None
        )
        if root is None:
            return
        if function.name in QUERY_RESET_METHODS:
            if not self.snippet.commented:
                self.ran.pop(root, None)
            return
        if (
            result
            and len(result) == 1
            and result[0].kind == "instance"
            and result[0].obj is owner
        ):
            return  # a builder method: returns the same query
        if root in self.ran:
            self.report(
                node,
                "query-reused",
                f"query '{root}' already ran on line {self.ran[root]}; a query runs once "
                "(RuntimeError), so build a new one or call reset()",
            )
        elif not self.snippet.commented:
            # Commented-out code is an alternative to the live code, not a step before it.
            self.ran[root] = self.snippet.line + self.offset + node.lineno - 1

    def same_object_root(self, node: ast.expr | None) -> str | None:
        """Return the variable a chain of builder calls starts from, if any."""
        while isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            node = node.func.value
        if isinstance(node, ast.Name):
            value = self.env.get(node.id)
            if (
                value
                and len(value) == 1
                and value[0].kind == "instance"
                and is_query(value[0].obj)
            ):
                return node.id
        return None


# --- Docstring sections ---------------------------------------------------------------


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


class GriffeWarnings(logging.Handler):
    """Collect griffe's warnings about Parameters entries missing from the signature."""

    PATTERN = re.compile(
        r"^(?P<path>.+?):(?P<line>\d+): (?P<message>.*does not appear in the.*)$"
    )

    def __init__(self) -> None:
        """Start with no findings."""
        super().__init__(logging.WARNING)
        self.findings: list[Finding] = []

    def emit(self, record: logging.LogRecord) -> None:
        """Turn a matching warning into a finding."""
        match = self.PATTERN.match(record.getMessage())
        if match:
            path = (ROOT / match.group("path")).resolve()
            if not path.is_file():
                path = (ROOT / PACKAGE / match.group("path")).resolve()
            self.findings.append(
                Finding(
                    path,
                    int(match.group("line")),
                    "docstring-params",
                    match.group("message"),
                )
            )


def parse_all_docstrings(package: Package) -> list[Finding]:
    """Parse every docstring, collecting griffe's signature warnings."""
    handler = GriffeWarnings()
    logger = logging.getLogger("griffe")
    logger.addHandler(handler)
    try:
        for obj in walk(package.root):
            if obj.docstring is not None:
                obj.docstring.parsed  # noqa: B018 - parsing is what logs the warnings
    finally:
        logger.removeHandler(handler)
    return handler.findings


# --- Main -----------------------------------------------------------------------------


def lint(verbose: bool = False) -> list[Finding]:
    """Run every check and return the findings."""
    package = Package()
    findings = parse_all_docstrings(package)
    findings += check_docstring_sections(package)
    for page in [*doc_pages(), *docstring_pages(package)]:
        checker = Checker(package, page)
        skipped = checker.run()
        findings += checker.findings
        if verbose:
            for line in skipped:
                print(f"{page.path.relative_to(ROOT)}:{line}: skipped (does not parse)")
    return sorted(
        set(findings), key=lambda f: (str(f.path), f.line, f.check, f.message)
    )


def main() -> int:
    """Print the findings; return 1 if there are any."""
    findings = lint(verbose="--verbose" in sys.argv[1:])
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
