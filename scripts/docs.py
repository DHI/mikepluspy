"""Build and check the documentation site with great-docs.

Usage
-----
    python scripts/docs.py build    # build the site into great-docs/_site
    python scripts/docs.py check    # great-docs lint, and proofread with Harper
    python scripts/docs.py links    # check links in the docs and the source

Run from the repository root, in an environment with the ``docs`` dependency group.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICTIONARY = ROOT / "docs" / "dictionary.txt"

# Rules that misfire on code in docstrings and inline code: identifiers such as
# `mikeplus` and `min_slope`, doctest ellipses, `.NET`, `TODO(2027)` tags.
IGNORED_PROOFREAD_RULES = [
    "AnA",
    "ExpandConfiguration",
    "ExpandMinimum",
    "ExpandTimeShorthands",
    "MissingTo",
    "Nowhere",
    "SplitWords",
    "ToDoHyphen",
    "UseEllipsisCharacter",
    "WrongNegative",
]


def great_docs(*args: str) -> int:
    """Run great-docs from the repository root and return its exit code."""
    # great-docs writes generated pages in the locale encoding, which breaks non-ASCII
    # docstrings on Windows.
    env = {**os.environ, "PYTHONUTF8": "1"}
    return subprocess.run(["great-docs", *args], cwd=ROOT, env=env).returncode


def proofread_files() -> list[str]:
    """Return absolute paths of the prose to proofread; great-docs needs them absolute."""
    tracked = subprocess.run(
        ["git", "ls-files", "README.md", "docs/user_guide", "mikeplus"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split()
    return [
        str(ROOT / path)
        for path in tracked
        if path.endswith((".md", ".qmd", ".py")) and "/auto_generated/" not in path
    ]


def build() -> int:
    """Build the site and check that it produced a home page."""
    code = great_docs("build")
    if code == 0 and not (ROOT / "great-docs" / "_site" / "index.html").is_file():
        print("great-docs build produced no great-docs/_site/index.html", file=sys.stderr)
        return 1
    return code


def check() -> int:
    """Lint the docs and proofread them in British English."""
    lint = great_docs("lint")
    proofread = great_docs(
        "proofread",
        "--dialect=uk",
        "--include-docstrings",
        "--compact",
        f"--dictionary-file={DICTIONARY}",
        f"--ignore={','.join(IGNORED_PROOFREAD_RULES)}",
        *proofread_files(),
    )
    return lint or proofread


def links() -> int:
    """Check links in the docs and the source."""
    return great_docs("check-links")


COMMANDS = {"build": build, "check": check, "links": links}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]]())
