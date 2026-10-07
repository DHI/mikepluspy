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

# Create .venv if needed and install the package with extras, e.g. `just setup dev,test`
setup extras="dev":
    uv venv --allow-existing
    uv pip install -e ".[{{ extras }}]"

# Create .venv if needed and install the docs tools; the package itself is not needed
setup-docs:
    uv venv --allow-existing
    uv pip install --group docs

# --- Fast tier: no MIKE+ install needed ---------------------------------------------

# Run every linter in scripts/linters, or one: `just lint docs_examples`, `just lint changed origin/main`
lint *args:
    uv run --no-sync python -m scripts.linters {{ args }}

# Type check the package, or the given files
typecheck *paths:
    uv run --no-sync pyrefly check {{ paths }}

# Apply formatting and safe lint fixes to the repository, or the given files
fix *paths=".":
    uv run --no-sync ruff format {{ paths }}
    uv run --no-sync ruff check --fix {{ paths }}

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

# --- Docs: needs Quarto and `just setup-docs` ------------------------------------

# Build the documentation site into great-docs/_site
docs:
    uv run --no-sync python scripts/docs.py build

# Lint the docs and proofread them (needs harper-cli on PATH)
docs-check:
    uv run --no-sync python scripts/docs.py check

# Check links in the docs and the source
docs-links:
    uv run --no-sync python scripts/docs.py links

# Serve the site CI built for a pull request, e.g. `just docs-preview 129` (needs `gh auth login`)
docs-preview pr:
    uv run --no-sync python scripts/docs.py preview {{ pr }}

# What to run before opening a PR
check: lint typecheck test
