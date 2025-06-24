"""MIKE+Py package."""

__version__ = "2025.4.0"

from pathlib import Path

from .conflicts import check_conflicts as _check_conflicts
_check_conflicts()

from pythonnet import load # noqa: E402
load(
    "coreclr", 
    runtime_config=(
        (Path(__file__).parent / "bin" / "runtimeconfig.json")
        .absolute()
        .as_posix()
    )
)
import clr  # noqa: E402

from .utils import setup_bin_path as _setup_bin_path # noqa: E402
_install_root, _dll_dir_handle = _setup_bin_path(
    major_assembly_version=23,
    fallback_mikeplus_install_root=Path("C:/Program Files (x86)/DHI/MIKE+/2025"),
    env_var_name_install_root="MIKEPLUSPY_INSTALL_ROOT",  # set this environment variable to use custom install path
    bin_path=Path("bin/x64"),
)

#  keep here for backward compatibility (mikeio1d uses) ... remove in 2026.0.0
try:
    from DHI.Mike.Install import MikeImport  # noqa: E402, F401
    from DHI.Mike.Install import MikeProducts  # noqa: E402, F401
except ImportError:
    # mock this case:
    # mikeplus.MikeImport.ActiveProduct().InstallRoot
    # used by mikeio1d
    class _MockMikeImport:   # noqa: E402, F401
        @staticmethod
        def ActiveProduct():
            return _MockMikeProduct()
    class _MockMikeProduct:  # noqa: E402, F401
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

from .datatableaccess import DataTableAccess  # noqa: E402
from .datatableaccess import DataTableDemoAccess  # noqa: E402
from .database import Database  # noqa: E402
from .shortcuts import open, create  # noqa: E402
from .utils import to_sql  # noqa: E402

__all__ = [
    "Database",
    "DataTableAccess",
    "DataTableDemoAccess",
    "open",
    "create",
    "to_sql",
]
