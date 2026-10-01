# ADR 0001: Test against real MIKE+ assemblies, not mocks

- Status: Accepted
- Date: 2026-10-01

## Context

MIKE+Py is a thin layer over the MIKE+ .NET assemblies, reached through pythonnet. Most of its bugs show up where the two meet: implicit conversions by pythonnet, `DbType` values, the `CmdCommitted`/`Msg` objects that commands return, canonical field casing, and signatures that change between MIKE+ releases within the same year line. The Python logic on either side of that boundary is usually trivial.

PR #128 added unit tests that swap the .NET table for `SimpleNamespace` fakes (`_fake_table`) and monkeypatch `DotNetConverter`. Those tests are fast and don't need a database, but each one asserts behaviour that it set up itself:

- Fake columns have `DbType=None`, so the `DbType`-driven string conversion that the PR introduces is never exercised. The fake reaches the "pass the string through" path, which a real table would never take.
- `test_geometry_command_failure_raises` gives `UpdateGeomByCommand` a hand-written `CmdCommitted`/`Msg` result. The PR itself lists those attributes as unverified on MIKE+ 2026 GA. The test would keep passing on a release where they don't exist.
- `DotNetConverter.to_dotnet_geometry` is monkeypatched out, so the geometry conversion that ends up reaching MIKE+ is never tested.
- `values.Keys` is read from a real .NET `Dictionary`, but the fake methods accept whatever is passed to them. A wrong argument order or type would never raise the error that pythonnet raises against the real method.

A mock of a foreign API encodes what we believe that API does. At this boundary our beliefs are the thing under test, so a mocked test can't fail for the reasons that matter.

## Decision

Tests do not mock, fake or monkeypatch MIKE+ .NET objects, or the `mikeplus/dotnet.py` conversion helpers. Tests that touch the interop boundary run against the installed MIKE+ assemblies and a real test database from `tests/conftest.py`.

Allowed:

- Pure-Python unit tests of code that never calls into .NET, such as string parsing and argument validation that runs before any .NET call.
- Faking things outside MIKE+, such as the filesystem, environment variables (for example `MIKEPLUSPY_INSTALL_ROOT`) or the import order in `conflicts.py`.
- Getting failure paths through real inputs that MIKE+ rejects. When MIKE+ can't be made to fail on demand, leave the path untested and say so in the PR instead of faking it.

## Speed

Agents run the suite constantly, so it has to stay fast. Get that speed from the fixtures, not from mocks:

- Use the coarsest safe DB scope (`session_*_db`, `module_*_db`, `class_*_db`) for read-only tests. Use the function-scoped `*_db` only for tests that mutate.
- Mark simulation and licensed-API tests `license_required`, and mark them `slow` if they are slow. The default run (`-m "not slow"`) stays quick, and `pytest -m slow` runs the rest.
- When a test is slow, first ask whether it can share a fixture or assert something smaller, then whether it belongs under `slow`. Don't replace MIKE+ with a stand-in.

When speed and correctness conflict, correctness wins.

## Consequences

- The mocked tests in PR #128 are rewritten against `sirius_db`, or the fixture fitting their scope, before merge. The case-insensitive insert/update tests and the duplicate-casing `ValueError` test convert directly. The geometry failure test is either reproduced with real input that MIKE+ rejects, or dropped and noted as untested.
- Developers and CI need a local MIKE+ install to run most tests. CI already only runs ruff and mypy, so nothing changes there.
- Running the suite on each supported release in a year line (GA, U1, U2…) catches .NET signature drift. Mocks would hide it.
