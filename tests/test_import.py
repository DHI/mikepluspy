"""`import mikeplus` against real MIKE+ installs, each in a fresh process.

The .NET runtime and MIKE+ assemblies load once per process, so each case
imports in a subprocess with its own ``MIKEPLUSPY_INSTALL_ROOT``.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.license_required

INSTALLS = Path("C:/Program Files (x86)/DHI/MIKE+")
MIKEPLUS_2026 = INSTALLS / "2026"
MIKEPLUS_2027 = INSTALLS / "2027"
BUNDLED_BIN = Path(__file__).resolve().parents[1] / "mikeplus" / "bin"

REPORT = """
import json, warnings
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    import mikeplus
from System import AppDomain, Environment
print(json.dumps({
    "warnings": [str(w.message) for w in caught],
    "runtime_major": Environment.Version.Major,
    "dhi_assemblies": {
        a.GetName().Name: a.Location
        for a in AppDomain.CurrentDomain.GetAssemblies()
        if a.GetName().Name.startswith("DHI.")
    },
}))
"""


def import_mikeplus(install_root: Path | None) -> dict:
    """Import mikeplus in a fresh process and report what it loaded."""
    env = dict(os.environ)
    env.pop("MIKEPLUSPY_INSTALL_ROOT", None)
    if install_root is not None:
        env["MIKEPLUSPY_INSTALL_ROOT"] = str(install_root)
    result = subprocess.run(
        [sys.executable, "-c", REPORT],
        env=env,
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout.strip().splitlines()[-1])


def requires_install(root: Path):
    return pytest.mark.skipif(
        not (root / "bin" / "x64").is_dir(), reason=f"{root} is not installed"
    )


def wrong_year_warnings(report: dict) -> list[str]:
    return [w for w in report["warnings"] if "MIKE+ 2027" in w]


def assert_loaded_from_2027(report: dict):
    """Every DHI assembly comes from MIKE+ 2027, or is the bundled installer helper."""
    outside = {
        name: location
        for name, location in report["dhi_assemblies"].items()
        if not Path(location).is_relative_to(MIKEPLUS_2027)
        and Path(location).parent != BUNDLED_BIN
    }
    assert report["dhi_assemblies"]
    assert outside == {}


@requires_install(MIKEPLUS_2027)
def test_2027_install_root_loads_2027_on_dotnet_10():
    report = import_mikeplus(MIKEPLUS_2027)

    assert wrong_year_warnings(report) == []
    assert_loaded_from_2027(report)
    assert report["runtime_major"] == 10


@requires_install(MIKEPLUS_2026)
def test_2026_install_root_warns_naming_expected_year_and_path():
    report = import_mikeplus(MIKEPLUS_2026)

    [warning] = wrong_year_warnings(report)
    assert str(MIKEPLUS_2026) in warning
