# ADR 0005: Python support follows SPEC 0, dropped at year lines

- Status: Accepted
- Date: 2026-10-08
- Supersedes: ADR 0002

## Context

ADR 0002 adopted [SPEC 0](https://scientific-python.org/specs/spec-0000/) and raised every floor in the first release of each quarter. SPEC 0 drops Python 3.12 in Q4 2026, so 2026.1.0 would have required Python 3.13.

That conflicts with the year-line rule in `DEVELOPMENT.md`. A user on Python 3.12 who installed 2026.0.0 would get no later 2026 release, including support for a later MIKE+ 2026 update, without first changing their Python. pip resolving to an older release hides that, but it doesn't make it any less of a break. A Python upgrade is costly for our users: MIKE+Py often runs inside a managed environment or next to other tools tied to one interpreter. A numpy or pandas upgrade is not, because pip does it as part of installing MIKE+Py.

## Decision

MIKE+Py follows SPEC 0, with one change to when Python versions are dropped:

- **Python versions are dropped only in the first release of a MIKE+ year line** (`YYYY.0.0`). That release drops every Python version that SPEC 0 has dropped by its release date. Within a year line, the minimum Python never rises.
- **SPEC 0 core packages** that we depend on (currently numpy and pandas) keep SPEC 0's schedule: their floors are raised in the first release of each quarter, using the [drop schedule](https://scientific-python.org/specs/spec-0000/#drop-schedule). The floor must still support our minimum Python.
- **Dependencies outside SPEC 0** (pythonnet) get the oldest release that supports every Python we support. We raise that floor when we need a newer feature or fix.
- **Runtime dependencies have no upper bounds.** A cap stops users from installing MIKE+Py next to newer packages, and it can't be lifted for releases already on PyPI. Pins on development tools stay.
- **CI tests the oldest and the newest supported Python.** Every workflow's Python matrix moves when the floor does.

SPEC 0 is a lower bound on support, so keeping a Python past its SPEC 0 date until the next year line still complies with it.

The 2026 year line supports Python 3.12 and later: 2026.0.0 should already have dropped 3.10 and 3.11, which SPEC 0 dropped in Q4 2024 and Q4 2025, and numpy 2.3 needs 3.11 or later anyway. 2027.0.0 drops 3.12. The other floors are numpy 2.3, pandas 2.3 and pythonnet 3.0.5.

## Consequences

- A user can move between all releases of a year line without changing Python.
- Python support lasts up to a year longer than SPEC 0 requires, so CI covers one more Python version for part of each year.
- The `YYYY.0.0` release checklist in `DEVELOPMENT.md` includes dropping Python versions; the quarterly check covers only numpy and pandas.
- CI resolves the newest numpy and pandas, so the floors themselves still go untested. A job that installs with `uv pip install --resolution lowest-direct` would test them. It needs MIKE+, so it belongs with the self-hosted full test.
