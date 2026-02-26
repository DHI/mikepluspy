# MIKE+Py for Development

This is a space for documenting standard development and maintenance processes.

## Release process for new MIKE+ versions

When a new version of MIKE+ is released, the following needs to be done before releasing a corresponing Python vesrion:

1. Setup a local test environment with the new version of MIKE+.
2. Set environment variable MIKEPLUSPY_INSTALL_ROOT to the root install directory of the new version (the parent folder of bin).
3. Confirm assemblies are loaded via procmon or similar when running test suite.
4. Update auto-generated tables (since database schema can change version to version)
    - Run `python scripts/generate_tables.py` from root directory
    - Check the git diff to see if the changes to auto generated tables make sense (it should be adding or removing columns)
5. Run test suite (make sure all green)
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

To build the documentation locally, follow these steps:

1. Install quarto
2. Run the following from `docs` as the root:
    - `uv run quartodoc build`
    - `uv run quarto render`


