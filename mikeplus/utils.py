"""General utilities for mikepluspy."""

import os
from pathlib import Path

import clr

clr.AddReference(
    "DHI.Mike.Install, Version=1.0.0.0, Culture=neutral, PublicKeyToken=c513450b5d0bf0bf"
)

import System  # noqa: E402
from DHI.Mike.Install import MikeImport  # noqa: E402
from DHI.Mike.Install import MikeProducts  # noqa: E402


def setup_bin_path():
    """Set up the bin path for mikepluspy."""
    MikeImport.Setup(23, MikeProducts.MikePlus)
    mikeplus_install_root = Path(MikeImport.ActiveProduct().InstallRoot)

    # MikeImport adds install bin to end of PATH, this brings it to the front
    env_path = System.Environment.GetEnvironmentVariable("PATH")
    all_paths = [Path(p) for p in env_path.split(";")]
    mikeplus_env_paths = [
        str(p) for p in all_paths if p.is_relative_to(mikeplus_install_root)
    ]
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
