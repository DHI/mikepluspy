"""Convenience functions for MIKE+Py accessible from the root package.

This module provides simple shortcuts for creating and opening MIKE+ databases
without having to directly instantiate the Database class.
"""

from __future__ import annotations

from pathlib import Path

from .database import Database


def open(model_path: str | Path, **kwargs) -> Database:
    """Open an existing MIKE+ model database.

    Parameters
    ----------
    model_path : str or Path
        Path to the model database file (e.g. "model.sqlite" or "model.mupp")
    **kwargs : dict
        Additional keyword arguments to pass to the Database constructor.
        Common options include:
        - auto_open : bool
            If True, immediately open the database connection

    Returns
    -------
    Database
        A Database object connected to the specified model

    Raises
    ------
    FileNotFoundError
        If the database file doesn't exist
    DatabaseError
        If MIKE+ fails to open the database

    """
    return Database(model_path, **kwargs)


def create(
    model_path: str | Path,
    *,
    projection_string: str = "",
    srid: int = -1,
    auto_open: bool = True,
    **kwargs,
) -> Database:
    """Create a new MIKE+ model database.

    Alias for Database.create()

    Parameters
    ----------
    model_path : str or Path
        Path where the new database will be created
    projection_string : str, optional
        The projection string for the database
    srid : int, optional
        The SRID for the database, e.g. 25832 for ETRS89 / UTM zone 32N
    auto_open : bool, optional
        If True, immediately open the database connection
    **kwargs : dict
        Additional keyword arguments to pass to the Database.create method,
        i.e. `overwrite` (bool): if True, replace an existing database file

    Returns
    -------
    Database
        A Database object for the newly created database

    Raises
    ------
    FileExistsError
        If the database already exists (except if overwrite is True)
    ValueError
        If both `projection_string` and `srid` are given
    DatabaseError
        If MIKE+ fails to create the database

    """
    return Database.create(
        model_path,
        projection_string=projection_string,
        srid=srid,
        auto_open=auto_open,
        **kwargs,
    )


__all__ = [
    "create",
    "open",
]
