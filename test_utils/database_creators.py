from pathlib import Path

import mikeplus  # noqa: F401
from DHI.Amelia.DataModule.Services.DataSource import BaseDataSource


def create_sqlite_db(db_path: str | Path, srid: int = 25832):
    """
    Create a sqlite database for testing purposes.

    Parameters
    ----------
    db_path : str | Path
        Path to the sqlite database.
    srid : int, optional
        Spatial reference system identifier. The default is 25832.
    """
    db_path = str(Path(db_path))
    data_source = BaseDataSource.Create(str(db_path))
    data_source.CreateDatabase()
    data_source.OpenDatabase()
    data_source.CreateModelTables(srid, "")
    data_source.CloseDatabase()
