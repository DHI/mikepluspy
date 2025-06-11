"""General utilities for mikepluspy."""

import os
from pathlib import Path
import warnings

import clr

_setup_called = False


def setup_bin_path(
    major_assembly_version: int,
    fallback_mikeplus_install_root: str | Path,
    env_var_name_install_root: str,
    bin_path: str | Path,
):
    """Set up the bin path for mikepluspy."""
    global _setup_called
    if _setup_called:
        return
    _setup_called = True

    fallback_mikeplus_install_root = Path(fallback_mikeplus_install_root)
    bin_path = Path(bin_path)

    mikeplus_install_root: Path | None = None
    mikeplus_env_paths: list[str] = []

    env_var_install_root: str | None = os.getenv(env_var_name_install_root)
    if env_var_install_root is not None:
        mikeplus_install_root = Path(env_var_install_root)
        mikeplus_install_bin = mikeplus_install_root / bin_path
        if not mikeplus_install_bin.exists():
            raise FileNotFoundError(
                f"{env_var_name_install_root} {bin_path} does not exist: {mikeplus_install_bin}"
            )
        mikeplus_env_paths.append(str(mikeplus_install_bin))
    else:
        # this can fail if DHI.Mike.Install can't be found
        try:
            clr.AddReference(
                "DHI.Mike.Install, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c513450b5d0bf0bf"
            )
            import System  # noqa: E402
            from DHI.Mike.Install import MikeImport  # noqa: E402
            from DHI.Mike.Install import MikeProducts  # noqa: E402

            MikeImport.Setup(major_assembly_version, MikeProducts.MikePlus)
            mikeplus_install_root = Path(MikeImport.ActiveProduct().InstallRoot)

            # MikeImport adds install bin to end of PATH, this brings it to the front
            env_path = System.Environment.GetEnvironmentVariable("PATH")
            all_paths = [Path(p) for p in env_path.split(";")]
            mikeplus_env_paths = [
                str(p) for p in all_paths if p.is_relative_to(mikeplus_install_root)
            ]
            os.environ["PATH"] = ";".join(mikeplus_env_paths) + ";" + os.environ["PATH"]
        except Exception as e:
            mikeplus_install_root = fallback_mikeplus_install_root
            mikeplus_install_bin = fallback_mikeplus_install_root / bin_path
            warnings.warn(
                f"Failed to find MIKE+ installation. Using default path: {mikeplus_install_root}. "
                f"If you want to use a different path, set the {env_var_name_install_root} environment variable. "
                f"{e}",
                category=UserWarning,
                stacklevel=2,
            )
            if not mikeplus_install_root.exists():
                raise FileNotFoundError(
                    f"Default MIKE+ installation does not exist: {mikeplus_install_root}"
                )
            if not mikeplus_install_bin.exists():
                raise FileNotFoundError(
                    f"Default MIKE+ installation bin {bin_path} does not exist: {mikeplus_install_bin}"
                )
            mikeplus_env_paths.append(str(mikeplus_install_bin))

    os.environ["PATH"] = ";".join(mikeplus_env_paths) + ";" + os.environ["PATH"]


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
