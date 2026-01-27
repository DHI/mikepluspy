# MIKE+Py Changelog

## [Unreleased]

### Added

- Support for MIKE+ 2026.
- Improved developer documentation for releases.

### Changed

### Deprecated

### Removed

- DataTableAccess: this was previously marked for deprecation and is now replaced by Database.
- Engine classes (FloodEngine, EPANET, MIKE1D): these were previously marked for deprecation and are now replaced by SimulationRunner.

### Fixed

### Security

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
