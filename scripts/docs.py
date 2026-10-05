"""Build and check the documentation site with great-docs.

Usage
-----
    python scripts/docs.py build    # build the site into great-docs/_site
    python scripts/docs.py check    # great-docs lint, and proofread with Harper
    python scripts/docs.py links    # check links in the docs and the source
    python scripts/docs.py preview <pr>  # serve the site CI built for a pull request

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
    "ExpandAlloc",
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
    # great-docs has no __main__, so call its entry point with this interpreter, which
    # finds it in this environment whether or not the environment is on PATH.
    cli = "from great_docs.cli import main; main()"
    command = [sys.executable, "-c", cli, *args]
    return subprocess.run(command, cwd=ROOT, env=env).returncode


def proofread_files() -> list[str]:
    """Return absolute paths of the prose to proofread; great-docs needs them absolute."""
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "README.md", "docs/user_guide", "mikeplus"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split("\0")
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


def gh(*args: str) -> str:
    """Run the GitHub CLI and return its output."""
    return subprocess.run(
        ["gh", *args], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


def preview(pr: str) -> int:
    """Serve the newest successful docs build of a pull request locally."""
    # `great-docs preview --pr` takes the newest run for the PR's head commit, which has
    # no site yet while it is still building, so pick the run here.
    branch, head_repo = gh(
        "pr", "view", pr,
        "--json=headRefName,headRepositoryOwner,headRepository",
        "--jq=.headRefName, .headRepositoryOwner.login + \"/\" + .headRepository.name",
    ).splitlines()  # fmt: skip
    # Match the head repository too: a fork's branch can share a name with one here.
    run = gh(
        "api", "--method=GET",
        "repos/{owner}/{repo}/actions/workflows/docs.yml/runs",
        "-f", "event=pull_request",
        "-f", "status=success",
        "-f", f"branch={branch}",
        "-f", "per_page=100",
        "--jq",
        f'[.workflow_runs[] | select(.head_repository.full_name == "{head_repo}")][0].id // empty',
    )  # fmt: skip
    if not run:
        print(f"PR #{pr} has no successful docs build yet.", file=sys.stderr)
        return 1
    return great_docs("preview", "--run", run, "--use-gh")


COMMANDS = {"build": build, "check": check, "links": links}

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "preview":
        sys.exit(preview(sys.argv[2]))
    if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]]())
