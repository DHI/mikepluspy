# AGENTS.md

MIKE+Py: a Python veneer (pythonnet) over the .NET assemblies of a local MIKE+ install. Windows-only; most functionality needs a MIKE+ license.

## Environment

- Importing `mikeplus` loads coreclr and MIKE+ assemblies from `C:/Program Files (x86)/DHI/MIKE+/<year>`. Override with `MIKEPLUSPY_INSTALL_ROOT` (parent of `bin`).
- `major_assembly_version` in `mikeplus/__init__.py` must match the installed MIKE+ (23 = 2025, 24 = 2026). Package version tracks the MIKE+ year (`2026.x.x`).
- Import order is enforced by `mikeplus/conflicts.py`: `mikeio1d` before `mikeplus` raises; `mikeio` in the same process warns. `MIKEPLUSPY_DISABLE_CONFLICT_CHECKS=true` disables.

## Commands

```bash
uv pip install -e ".[dev]"
pytest                                   # addopts includes -m "not slow"
pytest -m slow                           # slow tests only
ruff check . && ruff format . && mypy mikeplus
python scripts/generate_tables.py        # regenerate mikeplus/tables/auto_generated/
python scripts/lint_public_api.py        # check __all__ against source and docs; no MIKE+ needed
```

CI currently runs only ruff, mypy and the public API check, so run the relevant tests locally before calling a change done.

## Rules

- Never hand-edit `mikeplus/tables/auto_generated/`. Change `scripts/table_templates/` or `scripts/generate_tables.py` and regenerate.
- Go through `mikeplus/dotnet.py` helpers for .NET type conversion instead of touching .NET types directly. Extend existing wrappers rather than adding parallel abstractions.
- No breaking changes within a MIKE+ year line (GA, U1, U2… must all keep working): new tables/columns must degrade gracefully, and changed .NET signatures get a try-new/fall-back-to-old path tagged `TODO(<next year>)`. See `DEVELOPMENT.md`, which also holds the release checklist.
- The public API is what `__all__` declares; see "Public API" in `DEVELOPMENT.md`. New public names need an `__all__` entry and docs. Public signatures must not expose .NET types except where marked `# api: allow-leaked-type`.
- MIKE+Py writes `.sqlite`/`.mupp` files with no undo. Only operate on copies of example or user databases.

## Tests

`tests/conftest.py` provides each test DB at four scopes: `session_*_db`, `module_*_db`, `class_*_db` (shared copies, read-only by convention) and plain `*_db` (fresh per test). Use the coarsest scope that's safe; any test that mutates the DB needs the function-scoped one. Mark tests that run simulations or licensed APIs with `license_required` and, if slow, `slow`.
