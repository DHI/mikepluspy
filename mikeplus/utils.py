"""General utilities for mikepluspy."""

from __future__ import annotations

import os
import sys
from pathlib import Path
import warnings
from typing import Any
import clr

from System import AppDomain
from System import Reflection

_setup_called = False


def setup_bin_path(
    major_assembly_version: int,
    fallback_mikeplus_install_root: Path,
    env_var_name_install_root: str,
    bin_path: Path,
) -> tuple[Path | None, Any]:
    """Set up the bin path for mikepluspy."""
    global _setup_called
    if _setup_called:
        return None, None
    _setup_called = True

    fallback_mikeplus_install_root = Path(fallback_mikeplus_install_root)
    bin_path = Path(bin_path)

    # bin path for DHI.Mike.Install (required for versions before MIKE+ 2025 Update 1)
    sys.path.append(str(Path(__file__).parent / "bin"))

    # order is important
    install_root, dll_dir_handle = _try_setup_custom_bin_path(
        env_var_name_install_root, bin_path
    )
    if install_root is not None:
        return install_root, dll_dir_handle

    install_root, dll_dir_handle = _try_mike_install_bin_setup(major_assembly_version)
    if install_root is not None:
        return install_root, dll_dir_handle

    install_root, dll_dir_handle = _try_setup_default_bin_path(
        fallback_mikeplus_install_root, bin_path, env_var_name_install_root
    )
    return install_root, dll_dir_handle


def _try_setup_custom_bin_path(
    env_var_name_install_root: str, bin_path: Path
) -> tuple[Path | None, Any]:
    env_var_install_root: str | None = os.getenv(env_var_name_install_root)
    if env_var_install_root is None:
        return None, None

    mikeplus_install_root = Path(env_var_install_root)
    mikeplus_install_bin = mikeplus_install_root / bin_path
    if not mikeplus_install_bin.exists():
        raise FileNotFoundError(
            f"{env_var_name_install_root}={env_var_install_root!r}: bin path does not exist: '{mikeplus_install_bin}'. "
            f"Ensure the path is correct or unset {env_var_name_install_root} to use auto-detection."
        )

    warnings.warn(
        f"Using custom MIKE+ installation from {env_var_name_install_root}='{mikeplus_install_root}' "
        f"(bin: '{mikeplus_install_bin}').",
        category=UserWarning,
        stacklevel=2,
    )
    _update_python_env_path([str(mikeplus_install_bin)])
    _update_clr_assembly_resolve(str(mikeplus_install_bin))
    dll_dir_handle = os.add_dll_directory(str(mikeplus_install_bin)) if sys.platform == "win32" else None  # type: ignore
    return mikeplus_install_root, dll_dir_handle


def _update_python_env_path(mikeplus_env_paths: list[str]):
    os.environ["PATH"] = os.pathsep.join(mikeplus_env_paths) + os.pathsep + os.environ["PATH"]


def _update_clr_assembly_resolve(mikeplus_install_bin: str):
    def assembly_resolver(sender, args):
        assembly_name = args.Name.split(",")[0] + ".dll"
        assembly_path = os.path.join(mikeplus_install_bin, assembly_name)
        if os.path.isfile(assembly_path):
            return Reflection.Assembly.LoadFrom(assembly_path)
        return None

    AppDomain.CurrentDomain.AssemblyResolve += assembly_resolver


def _try_mike_install_bin_setup(major_assembly_version: int):
    try:
        clr.AddReference("DHI.Mike.Install")
        import System  # noqa: E402
        from DHI.Mike.Install import MikeImport  # noqa: E402
        from DHI.Mike.Install import MikeProducts  # noqa: E402

        MikeImport.Setup(major_assembly_version, MikeProducts.MikePlus)
        mikeplus_install_root = Path(MikeImport.ActiveProduct().InstallRoot)

        # MikeImport adds install bin to end of PATH, this brings it to the front
        env_path = System.Environment.GetEnvironmentVariable("PATH")
        all_paths = [Path(p) for p in env_path.split(os.pathsep)]
        mikeplus_env_paths = [
            str(p) for p in all_paths if p.is_relative_to(mikeplus_install_root)
        ]
        _update_python_env_path(mikeplus_env_paths)
        dll_dir_handle = os.add_dll_directory(str(mikeplus_env_paths[0])) if sys.platform == "win32" else None  # type: ignore
        return mikeplus_install_root, dll_dir_handle
    except Exception as e:
        warnings.warn(
            f"DHI.Mike.Install auto-detection failed ({e}). Falling back to default MIKE+ installation path.",
            category=UserWarning,
            stacklevel=2,
        )
        return None, None


def _try_setup_default_bin_path(
    fallback_mikeplus_install_root: Path, bin_path: Path, env_var_name_install_root: str
) -> tuple[Path | None, Any]:
    warnings.warn(
        f"Failed to find MIKE+ installation. Using default path: '{fallback_mikeplus_install_root}'. "
        f"If you want to use a different path, set the {env_var_name_install_root} environment variable. ",
        category=UserWarning,
        stacklevel=2,
    )
    if not fallback_mikeplus_install_root.exists():
        raise FileNotFoundError(
            f"Default MIKE+ installation does not exist: '{fallback_mikeplus_install_root}'"
        )
    if not (fallback_mikeplus_install_root / bin_path).exists():
        raise FileNotFoundError(
            f"Default MIKE+ installation bin {bin_path} does not exist: '{fallback_mikeplus_install_root / bin_path}'"
        )
    _update_python_env_path([str(fallback_mikeplus_install_root / bin_path)])
    _update_clr_assembly_resolve(str(fallback_mikeplus_install_root / bin_path))
    dll_dir_handle = (
        os.add_dll_directory(str(fallback_mikeplus_install_root / bin_path))  # type: ignore
        if sys.platform == "win32"
        else None
    )
    return fallback_mikeplus_install_root, dll_dir_handle


def to_sql(value) -> str:
    """Convert a Python value to its SQL string representation.

    Parameters
    ----------
    value
        The value to convert.

    Returns
    -------
    str
        The SQL string representation of the value.

    Examples
    --------
    >>> to_sql(10)
    '10'
    >>> to_sql(10.5)
    '10.5'
    >>> to_sql("test_muid")
    "'test_muid'"
    >>> to_sql(None)
    'NULL'
    """
    if value is None:
        return "NULL"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return f"'{str(value)}'"
