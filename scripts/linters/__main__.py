"""Run the linters; ``just lint`` is the only caller.

With no arguments, runs ruff's lint and format checks and then every ``lint_*.py`` in
this folder, except those that set ``RUN_BY_DEFAULT = False``. ``just lint <name> ...``
runs one, ``<name>`` being ``ruff`` or a script's name without ``lint_``, and passes it
the remaining arguments. A linter exits non-zero when it has findings.

Adding a linter means adding a ``lint_<name>.py`` here; the justfile does not change.

Usage
-----
    just lint                       # everything run by default
    just lint docs_examples         # one linter
    just lint changed origin/main   # one linter, with arguments
"""

from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def scripts() -> dict[str, Path]:
    """Return the linter scripts in this folder by name."""
    return {
        path.stem.removeprefix("lint_"): path for path in sorted(HERE.glob("lint_*.py"))
    }


def runs_by_default(path: Path) -> bool:
    """Whether a script leaves ``RUN_BY_DEFAULT`` unset or true."""
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == "RUN_BY_DEFAULT"
                for t in node.targets
            )
            and isinstance(node.value, ast.Constant)
        ):
            return bool(node.value.value)
    return True


def ruff(args: list[str]) -> int:
    """Run ruff's lint and format checks on ``args``, the repository by default."""
    paths = args or ["."]
    ruff = [sys.executable, "-m", "ruff"]
    codes = [
        subprocess.run([*ruff, "check", *paths], cwd=ROOT).returncode,
        subprocess.run([*ruff, "format", "--check", *paths], cwd=ROOT).returncode,
    ]
    return max(codes)


def run(name: str, args: list[str]) -> int:
    """Run one linter by name and return its exit code."""
    if name == "ruff":
        return ruff(args)
    found = scripts()
    if name not in found:
        names = ", ".join(["ruff", *found])
        raise SystemExit(f"unknown linter {name!r}; the linters are: {names}")
    return subprocess.run([sys.executable, str(found[name]), *args], cwd=ROOT).returncode


def main() -> int:
    """Run the linter named in the arguments, or all default ones; return 1 on findings."""
    if len(sys.argv) > 1:
        return run(sys.argv[1], sys.argv[2:])
    names = ["ruff", *(n for n, p in scripts().items() if runs_by_default(p))]
    failed = []
    for name in names:
        print(f"--- {name}", flush=True)
        if run(name, []) != 0:
            failed.append(name)
    if failed:
        print(f"\nFailed: {', '.join(failed)}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
