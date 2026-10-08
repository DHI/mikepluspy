"""Build and check the documentation site with great-docs.

Usage
-----
    python scripts/docs.py build    # build the site into great-docs/_site
    python scripts/docs.py check    # great-docs lint, and proofread with Harper
    python scripts/docs.py links    # check links in the docs and the source
    python scripts/docs.py preview <pr>  # serve the site CI built for a pull request

Run from the repository root, in an environment with the ``docs`` dependency group.
"""

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICTIONARY = ROOT / "docs" / "dictionary.txt"

DOCUMENTED = (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
UNDERLINE = re.compile(r"-{3,}")
# numpy docstring sections whose unindented lines are names, types or signatures
TERM_SECTIONS = {
    "Attributes",
    "Methods",
    "Other Parameters",
    "Parameters",
    "Raises",
    "Receives",
    "Returns",
    "See Also",
    "Warns",
    "Yields",
}

# The docs use sentence case for headings.
IGNORED_PROOFREAD_RULES = ["UseTitleCase"]


def great_docs(*args: str, capture: bool = False) -> subprocess.CompletedProcess[str]:
    """Run great-docs from the repository root."""
    # great-docs writes generated pages in the locale encoding, which breaks non-ASCII
    # docstrings on Windows.
    env = {**os.environ, "PYTHONUTF8": "1"}
    # great-docs has no __main__, so call its entry point with this interpreter, which
    # finds it in this environment whether or not the environment is on PATH.
    cli = "from great_docs.cli import main; main()"
    command = [sys.executable, "-c", cli, *args]
    return subprocess.run(
        command, cwd=ROOT, env=env, capture_output=capture, text=True, encoding="utf-8"
    )


def proofread_files() -> list[Path]:
    """Return the tracked prose and modules to proofread."""
    tracked = subprocess.run(
        ["git", "ls-files", "-z", "README.md", "docs/user_guide", "mikeplus"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split("\0")
    return [
        ROOT / path
        for path in tracked
        if path.endswith((".md", ".qmd", ".py")) and "/auto_generated/" not in path
    ]


def as_markdown(path: Path) -> str:
    """Return the prose of a file as Markdown, each line where it is in the file.

    Harper skips inline code only in Markdown files: it reads Python, and the stdin
    great-docs pipes ``.qmd`` pages through, as plain text. So every file is
    proofread as a Markdown copy, which lets prose quote `names` in backticks.
    """
    text = path.read_text(encoding="utf-8")
    return docstring_markdown(text) if path.suffix == ".py" else text


def docstring_markdown(source: str) -> str:
    """Return a module's docstrings as Markdown, each on the lines it has in the module.

    Every other line is blank, so comments are not proofread. Doctests are blanked, and
    the entries that name parameters, types and objects in the term sections go in
    backticks, as the site shows them.
    """
    lines = [""] * len(source.splitlines())
    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, DOCUMENTED) or not node.body:
            continue
        first = node.body[0]
        if not (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
        ):
            continue
        for offset, line in enumerate(docstring_lines(first.value.value)):
            lines[first.lineno - 1 + offset] = line
    return "\n".join(lines) + "\n"


def docstring_lines(docstring: str) -> list[str]:
    """Return a docstring's lines as Markdown prose, one for each line of the docstring."""
    lines = docstring.splitlines()
    indent = min((len(s) - len(s.lstrip()) for s in lines[1:] if s.strip()), default=0)
    lines = lines[:1] + [s[indent:] for s in lines[1:]]
    out, section, in_doctest = [], None, False
    for index, line in enumerate(lines):
        stripped = line.strip()
        following = lines[index + 1].strip() if index + 1 < len(lines) else ""
        if stripped.startswith(">>>"):
            in_doctest = True
        elif not stripped:
            in_doctest = False
        if in_doctest:
            out.append("")
        elif stripped and UNDERLINE.fullmatch(following):
            section = stripped
            out.append(stripped)
        elif (
            section in TERM_SECTIONS
            and stripped
            and not line[0].isspace()
            and not UNDERLINE.fullmatch(stripped)
        ):
            out.append(f"`` {stripped} ``" if "`" in stripped else f"`{stripped}`")
        else:
            # Indented prose would be an indented code block, which Harper skips.
            out.append(stripped)
    return out


def proofread() -> int:
    """Proofread the docs and docstrings in British English, one line per finding."""
    with tempfile.TemporaryDirectory() as tmp:
        sources, copies = {}, []
        for path in proofread_files():
            relative = path.relative_to(ROOT).as_posix()
            copy = Path(tmp) / f"{relative.replace('/', '.')}.md"
            copy.write_text(as_markdown(path), encoding="utf-8")
            sources[copy.name] = relative
            copies.append(str(copy))
        result = great_docs(
            "proofread",
            "--dialect=uk",
            "--json-output",
            f"--dictionary-file={DICTIONARY}",
            f"--ignore={','.join(IGNORED_PROOFREAD_RULES)}",
            *copies,
            capture=True,
        )
    try:
        issues = json.loads(result.stdout)["issues"]
    except (json.JSONDecodeError, KeyError):
        print(result.stdout, result.stderr, sep="\n", file=sys.stderr)
        return 1
    for issue in issues:
        print(
            f"{sources.get(Path(issue['file']).name, issue['file'])}:"
            f"{issue['line']}:{issue['column']}: "
            f"{issue['kind']}::{issue['rule']}: {issue['message']}"
        )
    return int(bool(issues))


def build() -> int:
    """Build the site and check that it produced a home page."""
    code = great_docs("build").returncode
    if code == 0 and not (ROOT / "great-docs" / "_site" / "index.html").is_file():
        print("great-docs build produced no great-docs/_site/index.html", file=sys.stderr)
        return 1
    return code


def check() -> int:
    """Lint the docs and proofread them in British English."""
    lint = great_docs("lint").returncode
    return lint or proofread()


def links() -> int:
    """Check links in the docs and the source."""
    return great_docs("check-links").returncode


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
    return great_docs("preview", "--run", run, "--use-gh").returncode


COMMANDS = {"build": build, "check": check, "links": links}

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "preview":
        sys.exit(preview(sys.argv[2]))
    if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]]())
