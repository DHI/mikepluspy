"""Run stricter lint rules on the source files changed since a base ref.

The rules -- annotated arguments and return types, and Returns/Raises sections in
docstrings -- are not enforced repo-wide because of the existing backlog. Running
them only on changed files pays the backlog down as files are touched.

Changed means changed since the merge base with ``base``, committed or not, plus
untracked files. The auto-generated tables are skipped.

Usage
-----
    just lint-changed [base]          # base defaults to main
"""

from __future__ import annotations

import subprocess
import sys

# DOC rules are preview-only in ruff 0.16, so they are selected by exact code.
RULES = "ANN001,ANN201,DOC201,DOC501"

PATHSPEC = ["mikeplus/*.py", ":!mikeplus/tables/auto_generated/*"]


def git(*args: str) -> list[str]:
    """Run git and return its output lines.

    Returns
    -------
    list[str]
        The non-empty lines git printed.

    """
    output = subprocess.run(["git", *args], capture_output=True, text=True, check=True)
    return [line for line in output.stdout.splitlines() if line]


def main() -> int:
    """Lint the changed files and return ruff's exit code.

    Returns
    -------
    int
        0 when there are no findings.

    """
    base = sys.argv[1] if len(sys.argv) > 1 else "main"
    merge_base = git("merge-base", base, "HEAD")[0]
    changed = git("diff", "--name-only", "--diff-filter=d", merge_base, "--", *PATHSPEC)
    untracked = git("ls-files", "--others", "--exclude-standard", "--", *PATHSPEC)
    files = sorted(set(changed + untracked))
    if not files:
        print("No changed source files.")
        return 0
    command = [sys.executable, "-m", "ruff", "check", "--preview", "--select", RULES]
    return subprocess.run([*command, *files]).returncode


if __name__ == "__main__":
    sys.exit(main())
