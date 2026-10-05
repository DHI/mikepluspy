# AGENTS.md

MIKE+Py: a Python veneer (pythonnet) over the .NET assemblies of a local MIKE+ install. Windows and Linux, x64 only; most functionality needs a MIKE+ license.

## MIKE+ is a black box

This repo and everything around it (commits, PRs, issues, docs, releases) is public; MIKE+ source is DHI-internal. Work only from what a MIKE+ install exposes: public assembly members, signatures and observed behaviour. You may read MIKE+ source or decompiled assemblies to understand a behaviour, but write up only the observed behaviour and the fix. MIKE+ code, decompiled output or close paraphrases of either must never appear in anything you write here. See `adr/0004-mikeplus-is-a-black-box.md`.

## Environment

- Importing `mikeplus` loads coreclr and MIKE+ assemblies from `C:/Program Files (x86)/DHI/MIKE+/<year>`. Override with `MIKEPLUSPY_INSTALL_ROOT` (parent of `bin`), which is required on Linux.
- `major_assembly_version` in `mikeplus/__init__.py` must match the installed MIKE+ (23 = 2025, 24 = 2026). Package version tracks the MIKE+ year (`2026.x.x`).
- Import order is enforced by `mikeplus/conflicts.py`: `mikeio1d` before `mikeplus` raises; `mikeio` in the same process warns. `MIKEPLUSPY_DISABLE_CONFLICT_CHECKS=true` disables.

## Commands

Use the `just` recipes rather than the tools behind them; `just` lists them all.

```bash
just setup                  # create .venv and install .[dev]
just lint                   # ruff, formatting and the public API check; no MIKE+ needed
just lint-changed           # stricter annotation/docstring rules on files changed since main
just typecheck              # mypy
just fix                    # format and apply safe lint fixes
just test                   # addopts includes -m "not slow"; extra args go to pytest
just test -m slow           # slow tests only
just generate-tables        # regenerate mikeplus/tables/auto_generated/
just docs                   # great-docs site; needs Quarto and `just setup-docs`, not MIKE+
just docs-check             # docs lint
just check                  # lint + typecheck + test, before opening a PR
```

CI currently runs only `just lint` and `just typecheck`, so run the relevant tests locally before calling a change done. Files you touch should pass `just lint-changed`.

## Rules

- Never hand-edit `mikeplus/tables/auto_generated/`. Change `scripts/table_templates/` or `scripts/generate_tables.py` and regenerate with `just generate-tables`.
- Go through `mikeplus/dotnet.py` helpers for .NET type conversion instead of touching .NET types directly. Extend existing wrappers rather than adding parallel abstractions.
- No breaking changes within a MIKE+ year line (GA, U1, U2… must all keep working): new tables/columns must degrade gracefully, and changed .NET signatures get a try-new/fall-back-to-old path tagged `TODO(<next year>)`. See `DEVELOPMENT.md`, which also holds the release checklist.
- The public API is what `__all__` declares; see "Public API" in `DEVELOPMENT.md`. New public names need an `__all__` entry and docs. Public signatures must not expose .NET types except where marked `# api: allow-leaked-type`.
- User-visible changes add a line under `## [Unreleased]` in `CHANGELOG.md` in the same PR, in Keep a Changelog form. See `adr/0003-keep-a-changelog.md`.
- MIKE+Py writes `.sqlite`/`.mupp` files with no undo. Only operate on copies of example or user databases.

## Tests

`tests/conftest.py` provides each test DB at four scopes: `session_*_db`, `module_*_db`, `class_*_db` (shared copies, read-only by convention) and plain `*_db` (fresh per test). Use the coarsest scope that's safe; any test that mutates the DB needs the function-scoped one. Mark tests that run simulations or licensed APIs with `license_required` and, if slow, `slow`.

Don't mock, fake or monkeypatch .NET objects or `mikeplus/dotnet.py` helpers. Interop tests run against real MIKE+ and a fixture DB. Get speed from fixture scope, not stand-ins. See `adr/0001-no-mocking-dotnet.md`.
