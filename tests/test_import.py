"""`import mikeplus` against real MIKE+ installs, each in a fresh process.

The .NET runtime and MIKE+ assemblies load once per process, so each case
imports in a subprocess with its own ``MIKEPLUSPY_INSTALL_ROOT``.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from importlib.metadata import version
from pathlib import Path

import pytest

pytestmark = pytest.mark.license_required

# The package version tracks the MIKE+ year it supports
EXPECTED_YEAR = int(version("mikeplus").split(".")[0])
PREVIOUS_YEAR = EXPECTED_YEAR - 1

INSTALLS = Path("C:/Program Files (x86)/DHI/MIKE+")
MIKEPLUS_EXPECTED = INSTALLS / str(EXPECTED_YEAR)
MIKEPLUS_PREVIOUS = INSTALLS / str(PREVIOUS_YEAR)
BUNDLED_BIN = Path(__file__).resolve().parents[1] / "mikeplus" / "bin"

REPORT = """
import json, warnings
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    import mikeplus
from System import AppDomain, Environment
[datamodule] = [
    a for a in AppDomain.CurrentDomain.GetAssemblies()
    if a.GetName().Name == "DHI.Amelia.DataModule"
]
print(json.dumps({
    "warnings": [str(w.message) for w in caught],
    "install_root": str(mikeplus._install_root),
    "datamodule_major": datamodule.GetName().Version.Major,
    "runtime_major": Environment.Version.Major,
    "dhi_assemblies": {
        a.GetName().Name: a.Location
        for a in AppDomain.CurrentDomain.GetAssemblies()
        if a.GetName().Name.startswith("DHI.")
    },
}))
"""


def run_python(code: str, install_root: Path | None) -> subprocess.CompletedProcess:
    """Run code in a fresh process with only the given MIKEPLUSPY_INSTALL_ROOT."""
    env = dict(os.environ)
    env.pop("MIKEPLUSPY_INSTALL_ROOT", None)
    if install_root is not None:
        env["MIKEPLUSPY_INSTALL_ROOT"] = str(install_root)
    result = subprocess.run(
        [sys.executable, "-c", code],
        env=env,
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, result.stderr
    return result


def import_mikeplus(install_root: Path | None) -> dict:
    """Import mikeplus in a fresh process and report what it loaded."""
    result = run_python(REPORT, install_root)
    return json.loads(result.stdout.strip().splitlines()[-1])


def requires_install(root: Path):
    return pytest.mark.skipif(
        not (root / "bin" / "x64").is_dir(), reason=f"{root} is not installed"
    )


def year_mismatch_warnings(report: dict) -> list[str]:
    return [w for w in report["warnings"] if "MIKE+Py expects MIKE+" in w]


def fallback_warnings(report: dict) -> list[str]:
    return [w for w in report["warnings"] if "Failed to find MIKE+ installation" in w]


def registered_install_root(year: int) -> Path:
    """The install root the MIKE+ installer recorded in the registry."""
    import winreg  # Windows-only
    with winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, rf"SOFTWARE\WOW6432Node\DHI\MIKE+\{year}"
    ) as key:
        home_dir, _ = winreg.QueryValueEx(key, "HomeDir")
    return Path(home_dir)


def assert_loaded_from_expected_year(report: dict):
    """Every DHI assembly comes from the expected MIKE+, or is the bundled installer helper."""
    outside = {
        name: location
        for name, location in report["dhi_assemblies"].items()
        if not Path(location).is_relative_to(MIKEPLUS_EXPECTED)
        and Path(location).parent != BUNDLED_BIN
    }
    assert report["dhi_assemblies"]
    assert outside == {}


@requires_install(MIKEPLUS_EXPECTED)
def test_expected_install_root_loads_expected_year_on_dotnet_10():
    report = import_mikeplus(MIKEPLUS_EXPECTED)

    assert year_mismatch_warnings(report) == []
    assert_loaded_from_expected_year(report)
    assert report["runtime_major"] == 10


@requires_install(MIKEPLUS_PREVIOUS)
def test_previous_year_install_root_warns_naming_expected_and_found_versions():
    report = import_mikeplus(MIKEPLUS_PREVIOUS)

    [warning] = year_mismatch_warnings(report)
    assert f"expects MIKE+ {EXPECTED_YEAR}" in warning
    assert (
        f"loaded MIKE+ {PREVIOUS_YEAR} (assembly version {report['datamodule_major']})"
        in warning
    )
    assert str(MIKEPLUS_PREVIOUS) in warning


@requires_install(MIKEPLUS_EXPECTED)
def test_without_install_root_resolves_through_registry():
    report = import_mikeplus(None)

    assert fallback_warnings(report) == []
    assert year_mismatch_warnings(report) == []
    assert Path(report["install_root"]) == registered_install_root(EXPECTED_YEAR)
    assert_loaded_from_expected_year(report)


@requires_install(MIKEPLUS_EXPECTED)
def test_utilities_import_in_interactive_interpreter():
    # pythonnet preloads every type of an assembly when sys.ps1 is set, as in Jupyter
    run_python(
        "import sys; sys.ps1 = '>>> '\n"
        "from mikeplus.utilities import get_nearest_river_chainage_at\n",
        MIKEPLUS_EXPECTED,
    )
