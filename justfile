# Task runner for MIKE+Py. Run `just` to list recipes.
#
# The recipes are the stable interface for contributors, agents and CI: call
# `just <recipe>` rather than the tools behind it, so a tool can be swapped here
# without touching the docs, settings or workflows.
#
# Recipes run tools from .venv without syncing it (there is no lockfile), so run
# `just setup` first.

set windows-shell := ["powershell.exe", "-NoLogo", "-NoProfile", "-Command"]

default:
    @just --list

# Create .venv if needed and install the package with extras, e.g. `just setup dev,docs`
setup extras="dev":
    uv venv --allow-existing
    uv pip install -e ".[{{ extras }}]"

# --- Fast tier: no MIKE+ install needed ---------------------------------------------

# Lint, check formatting and check the public API
lint:
    uv run --no-sync ruff check .
    uv run --no-sync ruff format --check .
    uv run --no-sync python scripts/lint_public_api.py

# Check the public API (__all__) against the source and the docs
api:
    uv run --no-sync python scripts/lint_public_api.py

# Stricter rules (annotations, Returns/Raises sections) on files changed since `base`
lint-changed base="main":
    uv run --no-sync python scripts/lint_changed.py {{ base }}

# Type check
typecheck:
    uv run --no-sync mypy mikeplus

# Apply formatting and safe lint fixes
fix:
    uv run --no-sync ruff format .
    uv run --no-sync ruff check --fix .

# --- Slow tier: needs MIKE+ installed -----------------------------------------------

# Run tests; extra arguments go to pytest, e.g. `just test -m slow` or `just test tests/test_scenarios.py -v`
test *args:
    uv run --no-sync pytest {{ args }}

# Run tests the way the MIKE+ CI runner does
test-ci *args:
    uv run --no-sync pytest -m "not skip_ci" {{ args }}

# Run the tests that need neither a MIKE+ license nor much time
test-unlicensed *args:
    uv run --no-sync pytest -m "not license_required and not slow" {{ args }}

# Regenerate mikeplus/tables/auto_generated/; extra arguments go to the script
generate-tables *args:
    uv run --no-sync python scripts/generate_tables.py {{ args }}

# Regenerate the quartodoc table sections in docs/_table_generated_sections.yml
table-docs:
    uv run --no-sync python docs/generate_table_docs.py

# Build the documentation site into docs/_site (needs quarto and `just setup dev,docs`)
[working-directory: 'docs']
docs:
    uv run --no-sync quartodoc build
    uv run --no-sync quartodoc interlinks
    uv run --no-sync quarto render
    uv run --no-sync python -c "import pathlib, sys; sys.exit('quarto render produced no _site/index.html' if not pathlib.Path('_site/index.html').is_file() else 0)"

# What to run before opening a PR
check: lint typecheck test
