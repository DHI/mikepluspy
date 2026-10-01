"""MIKE+Py package."""

__version__ = "2026.1.0"


import sys as _sys
import sysconfig as _sysconfig
from pathlib import Path

from .conflicts import check_conflicts as _check_conflicts

_check_conflicts()

# The interpreter's arch, not the CPU's, so emulated x64 Python on ARM64 isn't rejected
if _sysconfig.get_platform() not in ("win-amd64", "linux-x86_64"):
    raise ImportError(
        f"MIKE+Py requires x64 Python on Windows or Linux, not '{_sysconfig.get_platform()}'."
    )
if _sys.platform == "win32":
    _runtime_config = "runtimeconfig.json"
    _fallback_install_root: Path | None = Path("C:/Program Files (x86)/DHI/MIKE+/2026")
else:
    # Microsoft.WindowsDesktop.App does not exist on Linux
    _runtime_config = "runtimeconfig.linux.json"
    _fallback_install_root = None

from pythonnet import load

load(
    "coreclr",
    runtime_config=(
        (Path(__file__).parent / "bin" / _runtime_config).absolute().as_posix()
    ),
)
import clr

from .utils import setup_bin_path as _setup_bin_path

_install_root, _dll_dir_handle = _setup_bin_path(
    major_assembly_version=24,
    fallback_mikeplus_install_root=_fallback_install_root,
    env_var_name_install_root="MIKEPLUSPY_INSTALL_ROOT",  # set this environment variable to use custom install path
    bin_path=Path("bin/x64"),
)

#  keep here for backward compatibility (mikeio1d uses) ... remove in 2026.0.0
try:
    from DHI.Mike.Install import (
        MikeImport,
        MikeProducts,  # noqa: F401
    )
except ImportError:
    # mock this case:
    # mikeplus.MikeImport.ActiveProduct().InstallRoot
    # used by mikeio1d
    class _MockMikeImport:
        @staticmethod
        def ActiveProduct():
            return _MockMikeProduct()

    class _MockMikeProduct:
        InstallRoot = _install_root

    MikeImport = _MockMikeImport
    MikeProduct = _MockMikeProduct

clr.AddReference("System")
clr.AddReference("System.Runtime")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Data")
clr.AddReference("NetTopologySuite")
clr.AddReference("DHI.Amelia.DataModule")
clr.AddReference("DHI.Amelia.DataModule.Interface")
clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("DHI.Amelia.GlobalUtility")
clr.AddReference("DHI.Amelia.Tools.EngineTool")
clr.AddReference("DHI.Amelia.EPANETBridge")
clr.AddReference("DHI.Amelia.SWMMBridge")

from .database import Database, DatabaseError
from .shortcuts import create, open
from .utils import to_sql

__all__ = [
    "Database",
    "DatabaseError",
    "create",
    "open",
    "to_sql",
]
