# MIKE+Py Changelog

## [Unreleased]

## [2024.1.0] - 2024-01-30

### Added

- Ability to read/write MIKE+ database
- Ability to run engines (MIKE 1D, EPANET, SWMM)
- Ability to run some initial tools

## [2024.1.0] - 2024-06-02

### Added

- Fix Opening and closing a database in a loop takes increasingly long time 
- Fix setting the value of a database does not auto cast values. Int value can accept as double value now.
- Fix inserting fails silently when no value is provided for 'Seq'
- Handle Nullable value more user friendly
