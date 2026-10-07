# MIKE+Py Changelog

All notable changes to MIKE+Py are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow the MIKE+ year (`2026.x.x`) rather than [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [2026.1.0] - 2026-10-07

### Added

- Support for MIKE+ 2026 Update 1, including its new tables (such as `mss_InletConduitCon` and `mw_WDOAmi`) and columns.
- `mikeplus.utilities.get_nearest_river_at` and `get_nearest_river_chainage_at`, which find the river (and chainage) nearest to a point, for example to couple river junction nodes to rivers (#112).
- `Database.begin_transaction()` and `Database.end_transaction(commit)`, which group many updates into one transaction and make batch edits much faster (#112).
- `mikeplus.DatabaseError`, raised when creating, opening, closing or importing into a database fails. It subclasses `Exception`, so existing `except Exception` handlers still catch it.
- `Database.ensure_mupp()`, which returns a database's MIKE+ project file (`.mupp`), writing one beside it if it has none (#121).
- `mikeplus.tools.DemandConnectionTool`, the MIKE+ connection tool for demand allocations: connects `mw_DemAlloc` points to the nearest junction, a junction of the nearest pipe or the nearest pipe (part of #120). Failures raise `mikeplus.DatabaseError`.
- `mikeplus.tools.DemandAggregationTool`, the water distribution Aggregation tool: aggregates demand allocations to junction demands or pipe demand coefficients, rejecting unknown allocation MUIDs (#120).
- `mikeplus.tools.CreateValvesFromPointsTool`, the MIKE+ tool that creates water distribution valves from a point shapefile, snapping each point to a nearby junction or pipe (#120).
- Linux x64 support. There is no default install path on Linux, so set `MIKEPLUSPY_INSTALL_ROOT`.
- An optional `muids` argument on the `InterpolationTool` methods, such as `interpolate_from_DEM`, which restricts them to the given elements (#115).
- User-defined columns are managed from `table.columns` (#124): `add_user_defined` creates, restores or leaves a column unchanged and returns its `m_UserDefinedColumn` MUID; `remove_user_defined` hides a column as MIKE+ does, keeping its data, and `restore_user_defined` brings it back; `user_defined` and `detached` list the shown and restorable columns.

### Changed

- `Database.create()` also writes a `.mupp` project file beside the database, so a new model opens in MIKE+, and it accepts a `.mupp` path. It raises `FileExistsError` if a `.mupp` of that name already exists, and `overwrite=True` deletes that `.mupp` too, losing its map layers and other settings (#121).
- Table and column names in `select`, `insert`, `update` and `order_by` are matched case-insensitively (#119). Two field names that differ only in casing now raise `ValueError`, and `order_by` raises `ValueError` for an unknown column, as `select` does.
- Strings are converted only when the destination column needs it. DateTime columns parse them; Double columns accept a single `.` or `,` as the decimal separator, so `"1,234"` is 1.234, and anything else raises `ValueError` naming the field. An empty string becomes `None` for both. Strings bound for other columns are passed through unchanged.
- Minimum versions now follow [SPEC 0](https://scientific-python.org/specs/spec-0000/): numpy 2.3, pandas 2.3 and pythonnet 3.0.5.
- Importing `mikeplus` with anything other than x64 Python on Windows or Linux now raises `ImportError`.
- `Database.run()` raises `RuntimeError` when the engine exits with an error or doesn't write its result files, naming the engine's logs (#143).
- `TopoRepairTool.run()` raises `ValueError` unless the active model is CS_MIKE1D or WD_EPANET, instead of doing nothing (#146).
- `CathSlopeLengthProcess.run()` reports the tool's warnings with `warnings.warn` (#145).
- `ScenarioCollection.find_by_name()` returns every scenario with the name, not at most one (#146).
- `Database.close()` returns `None` whether or not the database was open (#146).
- The documentation site moved to great-docs. API reference pages moved from `api/` to `reference/`, and the auto-generated table classes no longer have their own pages. User guide URLs are unchanged.

### Removed

- Support for Python 3.10, 3.11 and 3.12. MIKE+Py now requires Python 3.13 or later.

### Fixed

- `create()` stores the SRID, so `Database.srid` and new geometry use it instead of -1. It is also derived from `projection_string` when MIKE+ recognises it. A geographic or unknown `srid` (such as 4326, which MIKE+ silently turned into Google Maps - Mercator) raises `ValueError` before any file is touched (#141).
- Opening a `.mupp` file that has no `.sqlite` of the same name beside it failed to find the database it refers to.
- `select()` accepts a single column name instead of splitting it into characters (#44).
- `BaseTable.add_user_defined_column()` no longer writes a duplicate `m_UserDefinedColumn` record when called again for the same column. It now returns the record's MUID, and raises `ValueError` if the column already exists with a different data type (#124).
- `table.columns` and `insert`/`update` see user-defined columns added or removed after the table was first read, and `insert`/`update` set values in user-defined columns that were already in the database when it was opened (#124).
- `SelectQuery.execute()` is annotated as returning each row's values as a list keyed by MUID, which is what it returns, instead of a dict of dicts.
- Strings that look like numbers, such as `"760309"`, were written to text columns as datetimes.
- Geometry updates through `update()` were not saved. They now go through MIKE+'s geometry command and raise `RuntimeError` if it doesn't commit.
- `from mikeplus.tables import *` raised `AttributeError`, and the table classes couldn't be imported from `mikeplus.tables`.
- Inserting a row with no field values on MIKE+ 2026 Update 1.
- `InterpolationTool.interpolate_from_neighobour` always raised `AttributeError`; it now honours `alongPath`.
- The `InterpolationTool` methods raised `TypeError` when `value_as_missing` was a number.
- `Database.create(overwrite=True)` deleted the existing database before rejecting `srid` together with `projection_string` (#140).
- `to_sql()` and `by_muid()` didn't escape single quotes, and `to_sql(True)` gave `True` rather than `1` (#144).
- Progress from `CathSlopeLengthProcess` and `ConnectionRepairTool` was never printed, because the handler was attached after the tool ran (#145).
- `Alternative.scenarios` raised `AttributeError` when the model had a scenario other than Base, and it, like `Alternative ==`, confused alternatives of different groups that share an id (#142).
- Iterating `db.scenarios` returned scenarios with the same name as one scenario repeated, and iterating an `AlternativeGroup` skipped alternatives below the base's children (#146).
- User guide examples and docstrings that raised or contradicted the code, notably `db.run(sim_option=...)` (not `model_option`), `insert()` running immediately, single-use queries, and `db.alternative_groups` (not `db.scenarios.alternative_groups`).

## [2026.0.0] - 2026-01-29

### Added

- Support for MIKE+ 2026.
- Improved developer documentation for releases.

### Removed

- DataTableAccess: this was previously marked for deprecation and is now replaced by Database.
- Engine classes (FloodEngine, EPANET, MIKE1D): these were previously marked for deprecation and are now replaced by SimulationRunner.

## [2025.6.0] - 2025-12-12

### Added

- Import EPANET models
- Import SWMM models

### Fixed

- Handle user-defined columns: track added columns and apply values outside command for inserts and updates to comply with .NET restrictions.

## [2025.5.0] - 2025-08-26

### Added
- Support for MIKE+ 2025 Update 1

### Changed
- Pythonnet now targets .NET 8.0

## [2025.4.0] - 2025-06-18

### Changes
- Update Windows DLL Search Directory with MIKE+ bin path (in addition to PATH)

## [2025.3.1] - 2025-06-11

### Fixed
- Fix AddReference for DHI.Mike.Install causing warning

## [2025.3.0] - 2025-06-11

### Added

- MIKEPLUSPY_INSTALL_ROOT to provide custom path to MIKE+ installation (also with default)

## [2025.2.0] - 2025-06-11

### Added
- Support for updating datetime values using strings.
- Run LTS job list generation simulation.
- Better error message when executing queries on unopened database.

## [2025.1.2] - 2025-06-10

### Fixed
- Allow importing mikeio after mikeplus

## [2025.1.1] - 2025-06-10

### Fixed
- More robust bin path setup, reduces the risk of conflicts with other software

## [2025.1.0] - 2025-06-09

### Added
- Fluent SQL API for chainable operations (select, insert, update, delete) on database tables
- `to_dataframe()` alias for `to_pandas()` and table-level shortcut method for pandas integration
- Convenience methods `open()` and `create()` for cleaner database access syntax
- Methods for listing available tables and their fields for discovery
- Scenario and alternative management
- `by_muid()` method to `BaseQuery` (inherited by `SelectQuery`, `UpdateQuery`, `DeleteQuery`) for convenient filtering by MUID(s).
- `to_sql()` utility function in `mikeplus.utils` (and exposed as `mikeplus.to_sql()`) for converting Python values to their SQL string representations.

### Changed
- Engine1D now uses EngineTool for more efficient simulation execution
- Redesigned database access architecture with new Database, TableCollection, and Table classes
- Automated table class generation with Jinja2 templates for maintainability
- Improved type handling for Python/C# interoperability
- Enhanced test isolation with database fixtures

### Deprecated
- Package 'mikeplus.engines' and all engine classes (removal planned in 2026.0.0)
- 'DataTableAccess' class, replaced with new 'Database', 'TableCollection', and 'Table' classes
- Use 'SimulationRunner' or 'Database.run()' methods instead of deprecated engine classes

### Developer
- Static type checking with mypy for improved code reliability
- Stricter linting rules for better code quality
- Improved error handling for database operations

## [2025.0.2] - 2025-02-18

### Added
- Support for Python 3.13

## [2025.0.1] - 2025-02-12

### Added
- Better compatibility warnings for MIKE IO and MIKE IO 1D.
- Override of compatibiltiy warnings with environment variable "MIKEPLUSPY_DISABLE_CONFLICT_CHECKS"

## [2025.0.0] - 2024-11-28

### Added
- Support for MIKE+ 2025.

## [2024.1.1] - 2024-11-28

### Added
- Run 2D and coupled simulations.
- Support for working with geometries via WKT.
- Shapely integration for creating and updating geometries.
- Edit date and timestamp values using python datetime objects.
- Possibility to switch active scenario, with notebook example.
- Published to PyPI (installalable via `pip install mikeplus`).
- CI testing for tests not requiring a license.

### Changed
- Upgraded test databases to MIKE+ 2024 Update 1.
- Converted test EPANET model to fit within demo license restrictions.
- Warn users trying to use MIKE IO and MIKE+Py together.
- Ruff for linting and formatting.

### Fixed
- get_field_values properly handles a single field passed as string.
- several ruff linting errors.

### Removed
- Support for Python 3.8.

## [2024.1.0] - 2024-06-13

### Added
- Example notebook for running MIKE+ simulation with multiple rainfalls.
- Example notebook for showing node connectivity information.
- Example notebook of how to create a new MIKE+ database.
- Example notebook of adding multiple section discharge result specifications.

### Changed
- Possible to run engines in silent mode without printing log to console.
- Replace DomainServices with EngineTool (.NET API) for running engines.

## [2024.0.0] - 2024-01-31

### Added
- Ability to read/write MIKE+ database.
- Ability to run engines (MIKE 1D, EPANET, SWMM).
- Ability to run some initial tools.

### Changed
- Handle Nullable value more user friendly.

### Fixed
- Fix Opening and closing a database in a loop takes increasingly long time.
- Fix setting the value of a database does not auto cast values. Int value can accept as double value now.
- Fix inserting fails silently when no value is provided for 'Seq'.

[Unreleased]: https://github.com/DHI/mikepluspy/compare/v2026.1.0...HEAD
[2026.1.0]: https://github.com/DHI/mikepluspy/compare/v2026.0.0...v2026.1.0
[2026.0.0]: https://github.com/DHI/mikepluspy/compare/v2025.6.0...v2026.0.0
[2025.6.0]: https://github.com/DHI/mikepluspy/compare/v2025.5.0...v2025.6.0
[2025.5.0]: https://github.com/DHI/mikepluspy/compare/v2025.4.0...v2025.5.0
[2025.4.0]: https://github.com/DHI/mikepluspy/compare/v2025.3.1...v2025.4.0
[2025.3.1]: https://github.com/DHI/mikepluspy/compare/v2025.3.0...v2025.3.1
[2025.3.0]: https://github.com/DHI/mikepluspy/compare/v2025.2.0...v2025.3.0
[2025.2.0]: https://github.com/DHI/mikepluspy/compare/v2025.1.1...v2025.2.0
[2025.1.1]: https://github.com/DHI/mikepluspy/compare/v2025.1.0...v2025.1.1
[2025.1.0]: https://github.com/DHI/mikepluspy/compare/v2025.0.2...v2025.1.0
[2025.0.2]: https://github.com/DHI/mikepluspy/compare/v2025.0.1...v2025.0.2
[2025.0.1]: https://github.com/DHI/mikepluspy/compare/v2025.0.0...v2025.0.1
[2025.0.0]: https://github.com/DHI/mikepluspy/compare/v2024.1.1...v2025.0.0
[2024.1.1]: https://github.com/DHI/mikepluspy/compare/v2024.1.0...v2024.1.1
[2024.1.0]: https://github.com/DHI/mikepluspy/compare/v2024.0.0...v2024.1.0
[2024.0.0]: https://github.com/DHI/mikepluspy/releases/tag/v2024.0.0
