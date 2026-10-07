"""Tests for scripts/linters/lint_entrypoints.py and the linter runner."""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.linters.__main__ import runs_by_default, scripts
from scripts.linters.lint_entrypoints import check_justfile, check_python, check_text

RUNNER = """
lint *args:
    uv run --no-sync python -m scripts.linters {{ args }}

fix *paths=".":
    uv run --no-sync ruff format {{ paths }}
    uv run --no-sync ruff check --fix {{ paths }}

typecheck *paths:
    uv run --no-sync pyrefly check {{ paths }}
"""


def checks(findings) -> list[str]:
    """Return the findings as ``line check``."""
    return [f"{f.line} {f.check}" for f in findings]


def test_the_repository_passes():
    """The repository runs its linters only through `just lint`."""
    result = subprocess.run(
        [sys.executable, "scripts/linters/lint_entrypoints.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout


def test_one_passthrough_recipe_passes():
    """A single recipe forwarding its arguments, plus fix and typecheck, is fine."""
    assert check_justfile(RUNNER) == []


def test_a_recipe_per_linter_is_reported():
    """A recipe that runs a linter script, or names one, is reported."""
    text = RUNNER + textwrap.dedent(
        """
        api:
            uv run --no-sync python scripts/linters/lint_public_api.py

        docs-examples:
            uv run --no-sync python -m scripts.linters docs_examples
        """
    )
    assert checks(check_justfile(text)) == [
        "13 justfile-direct",
        "16 justfile-runner",
        "1 justfile-runner",  # two recipes run the linters
    ]


def test_ruff_checks_in_the_justfile_are_reported():
    """ruff's checks belong to the runner; its fixes may stay in a recipe."""
    text = RUNNER + textwrap.dedent(
        """
        lint-ruff:
            uv run --no-sync ruff check .
            uv run --no-sync ruff format --check .
        """
    )
    assert checks(check_justfile(text)) == ["13 justfile-direct", "14 justfile-direct"]


def test_no_runner_is_reported():
    """A justfile without the runner recipe is reported."""
    assert checks(check_justfile("check:\n    just test\n")) == ["1 justfile-runner"]


def test_python_that_runs_a_tool_is_reported():
    """Running a lint tool from Python is reported; calling just with its name is not."""
    source = textwrap.dedent(
        '''
        """Docstrings may say `ruff check .`."""
        import shutil, subprocess
        subprocess.run(["ruff", "check", "."])
        ruff = shutil.which("ruff")
        subprocess.run([sys.executable, "-m", "scripts.linters"])
        subprocess.run(["just", "lint", "ruff", "path.py"])
        subprocess.run(["just", "typecheck"])
        '''
    )
    assert [f.line for f in check_python(source, "x.py")] == [4, 5, 6]


def test_config_that_runs_a_tool_is_reported():
    """A workflow or hook running a linter is reported; one calling just is not."""
    text = textwrap.dedent(
        """
        - run: just lint
        - run: uv run ruff check .
        - run: python scripts/linters/lint_public_api.py
        - run: uv run pyrefly check
        # griffe is used by scripts/linters/lint_docs_examples.py
        """
    )
    assert [f.line for f in check_text(text, "ci.yml")] == [3, 4, 5]


def test_runner_finds_the_linters_and_their_default():
    """Every lint_*.py is a linter; lint_changed opts out of the default run."""
    found = scripts()
    assert {"public_api", "docs_examples", "changed", "entrypoints"} <= set(found)
    assert not runs_by_default(found["changed"])
    assert runs_by_default(found["entrypoints"])


def test_runner_rejects_an_unknown_linter():
    """An unknown name lists the linters."""
    result = subprocess.run(
        [sys.executable, "-m", "scripts.linters", "nope"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "unknown linter 'nope'" in result.stderr
    assert "docs_examples" in result.stderr
