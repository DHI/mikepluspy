"""Check that the linters are run only through ``just lint``.

The justfile is the single way in: one recipe runs ``python -m scripts.linters`` and
passes its arguments on, so ``just lint`` runs every linter and ``just lint <name>``
one of them, and a new linter needs no new recipe. The checks:

justfile-runner   exactly one recipe runs ``-m scripts.linters``, ending in
                  ``{{ args }}`` for its variadic parameter, so the recipe names no
                  linter
justfile-direct   no recipe runs a linter script or ruff's checks itself
direct            outside the justfile and ``scripts/linters/``, nothing runs a linter,
                  ruff, pyrefly or ast-grep itself: workflows, hooks, scripts and docs
                  call ``just``

Tests are not checked; they import the linters to test them.

Usage
-----
    just lint entrypoints
"""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

TEXT_SUFFIXES = {".py", ".yml", ".yaml", ".json", ".toml", ".md", ".qmd", ".cfg", ".sh"}
SKIPPED = ("justfile", "scripts/linters/", "tests/", "CHANGELOG.md")

TOOLS = {"ruff", "pyrefly", "ast-grep"}
SUBCOMMANDS = {"check", "format", "scan", "run"}
TOOL_COMMAND = re.compile(
    r"\b(?:ruff\s+(?:check|format)|pyrefly\s+check|ast-grep\s+(?:scan|run))\b"
)
LINTER_SCRIPT = re.compile(r"\bscripts[/\\.]linters\b")
PYTHON_LINTER = re.compile(r"\bpython3?(?:\.exe)?\b[^\n]*\bscripts[/\\.]linters\b")

RECIPE = re.compile(r"^@?(?P<name>[A-Za-z_][\w-]*)(?P<params>[^:\n]*):(?!=)")
VARIADIC = re.compile(r"[*+](\w+)")
RUNNER = re.compile(r"-m\s+scripts\.linters\b")
RUNNER_PASSTHROUGH = re.compile(r"-m\s+scripts\.linters\s+\{\{\s*(\w+)\s*\}\}\s*$")
RUFF_CHECK = re.compile(r"\bruff\s+(?:check(?![^\n]*--fix)|format\s[^\n]*--check)")


@dataclass(frozen=True)
class Finding:
    """A linter run outside ``just lint``."""

    path: str
    line: int
    check: str
    message: str

    def __str__(self) -> str:
        """Format as ``path:line: check message``."""
        return f"{self.path}:{self.line}: {self.check} {self.message}"


def check_justfile(text: str, path: str = "justfile") -> list[Finding]:
    """Check that one recipe runs the linters and passes its arguments on unchanged."""
    findings, runners = [], []
    recipe, variadic = None, None
    for number, line in enumerate(text.splitlines(), start=1):
        header = RECIPE.match(line)
        if header:
            recipe = header.group("name")
            found = VARIADIC.search(header.group("params"))
            variadic = found.group(1) if found else None
            continue
        if not line[:1].isspace() or recipe is None:
            continue
        if RUNNER.search(line):
            runners.append(recipe)
            passed = RUNNER_PASSTHROUGH.search(line)
            if not (passed and variadic and passed.group(1) == variadic):
                findings.append(
                    Finding(
                        path,
                        number,
                        "justfile-runner",
                        f"recipe '{recipe}' must pass its arguments on unchanged, as "
                        "`*args` and `python -m scripts.linters {{ args }}`",
                    )
                )
        elif LINTER_SCRIPT.search(line) or RUFF_CHECK.search(line):
            findings.append(
                Finding(
                    path,
                    number,
                    "justfile-direct",
                    f"recipe '{recipe}' runs a linter itself; add it to scripts/linters "
                    "so `just lint` runs it",
                )
            )
    if len(runners) != 1:
        findings.append(
            Finding(
                path,
                1,
                "justfile-runner",
                "exactly one recipe must run `python -m scripts.linters`, found "
                f"{len(runners)}: {', '.join(runners) or 'none'}",
            )
        )
    return findings


def docstrings(tree: ast.AST) -> set[int]:
    """Return the ids of the docstring nodes in a module."""
    found = set()
    for node in ast.walk(tree):
        if isinstance(
            node, ast.Module | ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef
        ):
            body = node.body
            if body and isinstance(body[0], ast.Expr):
                found.add(id(body[0].value))
    return found


def word(node: ast.expr) -> str | None:
    """Return a string constant, or the constant of a call like ``tool("ruff")``."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if (
        isinstance(node, ast.Call)
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value in TOOLS
    ):
        return node.args[0].value
    return None


def check_python(text: str, path: str) -> list[Finding]:
    """Find commands in Python that run a linter or a lint tool."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    skip = docstrings(tree)
    lines = set()
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Constant)
            and isinstance(node.value, str)
            and id(node) not in skip
            and (TOOL_COMMAND.search(node.value) or LINTER_SCRIPT.search(node.value))
        ):
            lines.add(node.lineno)
        # Looking a tool up, e.g. `ruff = shutil.which("ruff")`, to run it later.
        if isinstance(node, ast.Call) and word(node) in TOOLS:
            lines.add(node.lineno)
        sequence = (
            node.args
            if isinstance(node, ast.Call)
            else node.elts
            if isinstance(node, ast.List | ast.Tuple)
            else []
        )
        words = [word(element) for element in sequence]
        for first, second in zip(words, words[1:], strict=False):
            if first in TOOLS and second in SUBCOMMANDS:
                lines.add(node.lineno)
    return [
        Finding(path, line, "direct", "runs a linter itself; call `just` instead")
        for line in sorted(lines)
    ]


def check_text(text: str, path: str) -> list[Finding]:
    """Find command lines in a config or docs file that run a linter or a lint tool."""
    return [
        Finding(path, number, "direct", "runs a linter itself; call `just` instead")
        for number, line in enumerate(text.splitlines(), start=1)
        if TOOL_COMMAND.search(line) or PYTHON_LINTER.search(line)
    ]


def tracked_files() -> list[str]:
    """Return the tracked text files that are checked, relative to the repository."""
    output = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return [
        path
        for path in output.splitlines()
        if Path(path).suffix in TEXT_SUFFIXES
        and not path.startswith(SKIPPED)
        and "/auto_generated/" not in path
    ]


def lint() -> list[Finding]:
    """Run every check and return the findings."""
    findings = check_justfile((ROOT / "justfile").read_text(encoding="utf-8"))
    for path in tracked_files():
        file = ROOT / path
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8", errors="replace")
        check = check_python if path.endswith(".py") else check_text
        findings += check(text, path)
    return findings


def main() -> int:
    """Print the findings; return 1 if there are any."""
    findings = lint()
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
