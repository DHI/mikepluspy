"""Base table class for MIKE+ database tables."""

from __future__ import annotations

import warnings
from typing import Any

from DHI.Amelia.GlobalUtility.DataType import UserDefinedColumnType
from System import DateTime
from System.Data import DbType

from mikeplus.dotnet import get_implementation as impl
from mikeplus.queries import DeleteQuery, InsertQuery, SelectQuery, UpdateQuery

from .base_table_columns import BaseColumns


class BaseTable:
    """Base class representing a database table."""

    def __init__(self, net_table):
        """Initialize a new table wrapper.

        Parameters
        ----------
        net_table
            The underlying .NET IMuTable object

        """
        if net_table is None:
            warnings.warn(
                f"Could not intialize table: {self.__class__}. This is likely due to a mismatch between the model database and mikepluspy version."
            )
            return
        self._net_table = impl(net_table, raw=True)
        self._columns = None
        self._user_defined_columns = set()

    def __repr__(self) -> str:
        """Get string representation."""
        return f"{self.__class__.__name__}<{self.display_name}>"

    @property
    def columns(self) -> BaseColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = BaseColumns(self)
        return self._columns

    @property
    def name(self) -> str:
        """Get the table name."""
        return self._net_table.TableName

    @property
    def display_name(self) -> str:
        """Get the display name for the table."""
        return self._net_table.TableDisplayName

    @property
    def description(self) -> str:
        """Get the table description."""
        return self._net_table.Description

    def get_muids(
        self, order_by: str | None = None, descending: bool = False
    ) -> list[str]:
        """Get a list of MUIDs for the table.

        Parameters
        ----------
        order_by : str or None, optional
            Column to order the MUIDs by
        descending : bool, optional
            Whether to order in descending order

        Returns
        -------
        list of str
            A list of MUIDs

        """
        return list(self._net_table.GetMuids(order_by, descending))

    def select(self, columns: list[str] = []):
        """Create a SELECT query for this table.

        Parameters
        ----------
        columns : list of str, optional
            The columns to select

        Returns
        -------
        SelectQuery
            A new SelectQuery object

        """
        return SelectQuery(self, columns)

    def insert(self, values: dict[str, Any], execute=True):
        """Insert a row with given values.

        Parameters
        ----------
        values : dict[str, Any]
            Column-value pairs to insert.
        execute : bool, optional
            If True, executes immediately (default). If False, returns an InsertQuery.

        Returns
        -------
        str or InsertQuery
            When execute=True, returns the MUID of the inserted row.
            When execute=False, returns an InsertQuery instance.

        Notes
        -----
        User-defined columns cannot be set via command-based insert in the .NET application.
        Handling of user-defined columns is performed in InsertQuery when the query is executed.
        """
        query = InsertQuery(self, values=values)
        return query.execute() if execute else query

    def update(self, values: dict[str, Any]):
        """Create an UPDATE query for this table.

        Parameters
        ----------
        values : dict of str to Any
            Column-value pairs to set in the UPDATE

        Returns
        -------
        UpdateQuery
            A new UpdateQuery object

        """
        query = UpdateQuery(self, values)
        return query

    def delete(self):
        """Create a DELETE query for this table.

        Returns
        -------
        DeleteQuery
            A new DeleteQuery object

        """
        return DeleteQuery(self)

    def to_dataframe(self):
        """Convert the table data to a pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            A pandas DataFrame containing all table data

        """
        return self.select().to_dataframe()

    def add_user_defined_column(
        self,
        column_name: str,
        column_data_type: str,
        column_header: str | None = None,
    ):
        """Add a user defined column to table.

        Parameters
        ----------
        column_name : str
            Name of the column in the database.
        column_data_type : str
            Data type of the column. Must be one of 'integer', 'double', 'string', 'datetime'.
        column_header : str | None
            Name of the column as displayed in the MIKE+ GUI. None uses the column_name.

        """
        table = self._net_table

        column_data_type = column_data_type.lower()
        if column_data_type == "integer":
            column_data_type = DbType.Int32
        elif column_data_type == "double":
            column_data_type = DbType.Double
        elif column_data_type == "string":
            column_data_type = DbType.String
        elif column_data_type == "datetime":
            column_data_type = DbType.DateTime
        else:
            raise ValueError(
                f"Invalid column_data_type: {column_data_type}. Must be one of 'integer', 'double', 'string', 'datetime'."
            )

        if column_header is None:
            column_header = column_name

        ret = table.AddUserDefinedColumn(
            UserDefinedColumnType.NewDbField,  # Only NewDbField supported for now
            column_header,
            column_name,
            column_data_type,
            "",  # Expression columns not supported yet
            "",  # Result columns not supported yet
            "",  # Result columns not supported yet
            0,  # Result columns not supported yet
            DateTime.MinValue,  # Result columns not supported yet
            False,  # Reset from database
        )

        # Keep track so we can set values not-by-command for these columns

        self._user_defined_columns.add(column_name)
        return ret

        return ret
