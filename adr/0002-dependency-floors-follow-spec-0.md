# ADR 0002: Python and dependency floors follow SPEC 0

- Status: Superseded by ADR 0005
- Date: 2026-10-01

## Context

MIKE+Py had no rule for its minimum versions. `requires-python` stayed at 3.10 because nobody raised it, and numpy and pandas had no lower bound at all. Raising the 3.10 floor in PR #129 raised the question of how far to go.

[SPEC 0](https://scientific-python.org/specs/spec-0000/) is the scientific Python ecosystem's time-based policy for dropping support. numpy, scipy, matplotlib, xarray and other core projects endorse it, and our users install MIKE+Py next to those packages. If we follow the same schedule, users get a Python and a numpy that the rest of their stack also supports.

## Decision

MIKE+Py follows SPEC 0:

- A Python version is dropped 3 years after its first release.
- A SPEC 0 core package that we depend on (currently numpy and pandas) is supported for 2 years after each feature release. Its floor is the oldest feature release that is not yet 2 years old.
- Floors are raised in the first release of each quarter, using the [drop schedule](https://scientific-python.org/specs/spec-0000/#drop-schedule).

SPEC 0 lets a project keep an old Python until the newest one works. We don't need that while CI already passes on the newest Python.

The rules that SPEC 0 leaves to us:

- **Dependencies outside SPEC 0** (pythonnet) get the oldest release that supports our minimum Python. We raise that floor when we need a newer feature or fix, or when the old release can't run on our supported Pythons. pythonnet 3.0.5 is the first release that supports Python 3.13.
- **Runtime dependencies have no upper bounds.** A cap stops users from installing MIKE+Py next to newer packages, and it can't be lifted for releases already on PyPI. Pins on development tools (ruff, mypy, great-docs) are a different matter, because only contributors install them. Those stay.
- **CI tests the oldest and the newest supported Python.** Every workflow's Python matrix moves when the floor does.

Raising a floor is not a break under the year-line rule in `DEVELOPMENT.md`. Code that already works keeps working: on an older Python, pip and uv install the last MIKE+Py release that still supports it. Floors move with the calendar, not with MIKE+ year lines.

As of this ADR (Q4 2026), the floors are Python 3.13, numpy 2.3, pandas 2.3 and pythonnet 3.0.5.

## Consequences

- PR #129 moves from Python 3.10 to 3.13. That skips 3.11 and 3.12, which SPEC 0 dropped in Q4 2025 and Q4 2026.
- Someone stuck on an older Python gets no new MIKE+Py releases. That includes support for a later update in the same MIKE+ year (for example U2), which arrives only in a new release. They have to upgrade Python to get it.
- Each quarter's first release needs a check against the schedule. `DEVELOPMENT.md` lists this check.
- CI resolves the newest numpy and pandas, so the floors themselves still go untested. A job that installs with `uv pip install --resolution lowest-direct` would test them. It needs MIKE+, so it belongs with the self-hosted full test.
