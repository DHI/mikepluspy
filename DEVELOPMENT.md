# MIKE+Py for Development

This is a space for documenting standard development and maintenance processes.

## Task runner

Development tasks are [just](https://just.systems) recipes, run from the
repository root; `just` lists them. Recipes are the stable interface for
contributors, agents and CI, so call `just <recipe>` rather than the tools
behind it. You need `just` and [uv](https://docs.astral.sh/uv/) on your PATH.

```bash
just setup              # create .venv and install .[dev]
just lint               # ruff, formatting and the public API check; no MIKE+ needed
just lint-changed       # stricter rules on files changed since main; `just lint-changed <base>`
just typecheck          # mypy
just fix                # apply formatting and safe lint fixes
just test               # pytest; extra arguments go to pytest, e.g. `just test -m slow`
just check              # lint + typecheck + test: run before opening a PR
```

`lint-changed` adds annotation rules (ANN001, ANN201) and Returns/Raises
docstring sections (DOC201, DOC501). They are not enforced repo-wide because of
the existing backlog; make the files you touch pass so it shrinks.

## Compatibility principle: no breaking changes within a year line

Within a MIKE+ year (all `2026.x.x` releases), avoid changes that break users
regardless of which update (GA, U1, U2, …) of that year they have installed.
Save genuine breaks for the next year bump.

- Adding tables/columns is fine — they degrade gracefully against older
  assemblies (`GetTable` returns `None`, `BaseTable.__init__` warns and
  continues). Don't add code that hard-fails on a missing table/column. Avoid
  removing or renaming mid-year.
- For changed .NET signatures, support both forms (try new, fall back to old)
  rather than swapping. See `SimulationRunner.__init__`. Tag fallbacks with
  `TODO(<next year>)` for cleanup at the year bump.

## Public API

The public API is the names in `__all__` of `mikeplus`, of its public
subpackages, and of the public modules directly in `mikeplus/`, plus every
non-underscore member of an exported class. A module or package whose name
starts with a single underscore is private, along with everything in it.
Everything public is covered by the compatibility principle above; anything
else may change in any release.

`just api` checks this against the source and the docs, and runs in CI as
part of `just lint`. It reads files only, so it needs no MIKE+ install.

### What is public

- `mikeplus`: `open`, `create`, `Database`, `DatabaseError`, `to_sql`.
- `mikeplus.queries`: the query classes returned by `select`, `insert`,
  `update` and `delete` on a table.
- `mikeplus.scenarios`, `mikeplus.tools`, `mikeplus.utilities`: their
  `__all__`.
- `mikeplus.tables`: the base table classes and every auto-generated table
  class, which it re-exports from `mikeplus.tables.auto_generated`. The
  table classes are public but not in the API reference; the "Tables" user
  guide shows how to find tables and column descriptions at runtime.

Import from those packages, not from the modules that implement them
(`mikeplus.scenarios`, not `mikeplus.scenarios.scenario`). `mikeplus.shortcuts`,
`mikeplus.utils` and `mikeplus.database` list the names they define for
`mikeplus` to re-export, but `mikeplus` is the documented path.

### What is internal

`mikeplus.conflicts`, `mikeplus.dotnet` and `mikeplus.simulation_runner`
declare an empty `__all__`: they are the machinery behind `import mikeplus` and
`Database.run`, and they deal in .NET types. Their names still import, so no
caller breaks, but they may change without notice. Put new internal code in
underscore-prefixed modules so the name says it.

### Rules for public code

- A new public name goes in `__all__` and in the docs: the user guide, or the
  `reference` sections in `great-docs.yml`. The auto-generated tables are
  exempt.
- Public signatures must not mention .NET (`DHI.*`, `System.*`, `ThinkGeo.*`)
  or underscore-private types. A signature that exposes one on purpose, such
  as an escape hatch to the underlying .NET object, carries the comment
  `# api: allow-leaked-type` on its `def` line or on the line that closes it.
  The marker records a decision; it is not a way to silence the linter.
- The linter only sees .NET names imported with `from DHI... import X`, and
  only reads annotations, so unannotated signatures go unchecked.

## Release process for new MIKE+ versions

When a new version of MIKE+ is released, the following needs to be done before releasing a corresponing Python vesrion:

1. Setup a local test environment with the new version of MIKE+.
2. Set environment variable MIKEPLUSPY_INSTALL_ROOT to the root install directory of the new version (the parent folder of bin).
3. Confirm assemblies are loaded via procmon or similar when running test suite.
4. Update auto-generated tables (since database schema can change version to version)
    - Run `just generate-tables`
    - Check the git diff to see if the changes to auto generated tables make sense (it should be adding or removing columns)
5. Run test suite, `just test` and `just test -m slow` (make sure all green)
6. Run all notebooks (make sure all cells run with readable output)
7. Be aware that runtimeconfig.json *may* need to change if MIKE+ runtime changes, though that should not happen often.
8. Update the package init to link to the new version
    - Update DHI.Mike.Install.dll in bin folder (when officially released)
    - Update assembly version to match latest version (23 = 2025, 24 = 2026)
9. Bump package version to match year of MIKE+ (e.g. 2026.0.0 for the first 2026 release)
10. Update CI runner to use the new MIKE+ version
11. Do other changes associated with a standard MIKE+Py release that does not involve bumping MIKE+ versions.
Note that the above list is a guideline and may not be exaustive. Automation of these steps is welcome - consider the current process best efforts.

## Documentation

The site is built with [great-docs](https://posit-dev.github.io/great-docs/) on
top of [Quarto](https://quarto.org). It reads the source statically and does
not need `mikeplus` to be importable, so it builds without MIKE+, on Linux too.

- `great-docs.yml` (repository root) configures the site and lists the API
  reference sections.
- `docs/user_guide/` holds the user guide. The numeric prefixes set the order
  and are dropped from the URLs.
- `README.md` is the home page. Its centred block (logo, tagline, badges)
  becomes the hero.
- `docs/dictionary.txt` lists words the proofreader accepts.

To build locally:

1. Install [Quarto](https://quarto.org/docs/get-started/), and
   [harper-cli](https://github.com/Automattic/harper/releases) for `just docs-check`.
2. `just setup-docs`, which installs the `docs` dependency group into `.venv`.
3. `just docs` builds into `great-docs/_site`; `just docs-check` lints and
   proofreads (British English); `just docs-links` checks links.

The CI Docs workflow runs `docs-check` and `docs` on pull requests that
touch the docs, docstrings or docs tooling, deploys to GitHub Pages on push to
`main`, and checks links weekly. On those pull requests it uploads the built
site and comments how to view it: `great-docs preview --pr <number> --use-gh`.
On Windows, set `PYTHONUTF8=1` first; without it the command fails on
non-ASCII output. A build
takes under a minute on Linux; on Windows, Quarto and great-docs are several
times slower.
