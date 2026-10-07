"""Base class for column enumeration-like access."""

from typing import TYPE_CHECKING

from DHI.Amelia.GlobalUtility.DataType import UserDefinedColumnType
from System import DateTime
from System.Data import DbType

from mikeplus.utils import to_sql

if TYPE_CHECKING:
    from .base_table import BaseTable

_DB_TYPES = {
    "integer": DbType.Int32,
    "double": DbType.Double,
    "string": DbType.String,
    "datetime": DbType.DateTime,
}

_DATA_TYPE_FAMILIES = {
    DbType.Int16: "integer",
    DbType.Int32: "integer",
    DbType.Int64: "integer",
    DbType.Single: "double",
    DbType.Double: "double",
    DbType.Decimal: "double",
    DbType.String: "string",
    DbType.StringFixedLength: "string",
    DbType.AnsiString: "string",
    DbType.AnsiStringFixedLength: "string",
    DbType.DateTime: "datetime",
    DbType.DateTime2: "datetime",
    DbType.Date: "datetime",
}


def _to_db_type(data_type: str) -> DbType:
    try:
        return _DB_TYPES[data_type.lower()]
    except KeyError:
        raise ValueError(
            f"Invalid data_type: {data_type}. "
            "Must be one of 'integer', 'double', 'string', 'datetime'."
        ) from None


def _require_matching_type(name: str, data_type: str, existing: DbType) -> None:
    existing_family = _DATA_TYPE_FAMILIES.get(existing, str(existing))
    if data_type.lower() != existing_family:
        raise ValueError(
            f"Column '{name}' already exists as '{existing_family}', "
            f"not '{data_type}'. Leave out data_type to keep the existing type."
        )


class BaseColumns:
    """Base class for column enumeration-like access.

    Provides dictionary-like access to table columns.
    """

    def __init__(self, table: "BaseTable"):
        """Initialize with a reference to the parent table.

        Parameters
        ----------
        table : BaseTable
            Reference to the parent BaseTable instance

        """
        self._table = table
        self._net_table = table._net_table
        self._refresh()

    def _refresh(self) -> None:
        self._column_names: tuple[str, ...] = tuple(
            column.Field for column in self._net_table.Columns
        )
        self._columns_by_name = {name.casefold(): name for name in self._column_names}

    def add_user_defined(
        self,
        name: str,
        data_type: str,
        header: str | None = None,
    ) -> str:
        """Add a user-defined column, like "Add user defined column" in MIKE+.

        Safe to call repeatedly: the column is created if it doesn't exist,
        restored if it is in `detached`, and left unchanged if it is already
        user-defined.

        Parameters
        ----------
        name : str
            Field name of the column. Case-insensitive: an existing or detached
            column matches regardless of casing. A new or restored column is
            stored with the casing given here.
        data_type : str
            One of 'integer', 'double', 'string', 'datetime', in any casing. If
            the column already exists, it must match the existing type.
        header : str or None, optional
            Header shown in the MIKE+ GUI. Defaults to `name`. Ignored if the
            column is already user-defined.

        Returns
        -------
        str
            MUID of the column's record in `m_UserDefinedColumn`, the same
            whether the column was created, restored or already there.

        Raises
        ------
        ValueError
            If `name` is a standard MIKE+ column, or if `data_type` is invalid
            or doesn't match the existing column.

        Examples
        --------
        >>> pipes = db.tables.msm_Link
        >>> pipes.columns.add_user_defined("install_year", "integer")
        'udf_1'

        """
        db_type = _to_db_type(data_type)

        column = self._column_definition(name)
        if column is not None:
            if not column.IsUserDefined:
                raise ValueError(
                    f"'{column.Field}' is a standard MIKE+ column of "
                    f"{self._table.name}, not a user-defined one."
                )
            _require_matching_type(name, data_type, column.DbType)
            return self._record_muid(column.Field)

        detached_type = self._detached_type(name)
        if detached_type is not None:
            _require_matching_type(name, data_type, detached_type)
        return self._attach(name, db_type, header)

    def restore_user_defined(self, name: str) -> str:
        """Restore a detached column with its existing data type and data.

        Parameters
        ----------
        name : str
            Field name of a column in `detached`. Case-insensitive; the restored
            column is stored with the casing given here.

        Returns
        -------
        str
            MUID of the column's new record in `m_UserDefinedColumn`.

        Raises
        ------
        KeyError
            If `name` isn't in `detached`.

        Examples
        --------
        >>> pipes = db.tables.msm_Link
        >>> pipes.columns.add_user_defined("install_year", "integer")
        'udf_1'
        >>> pipes.columns.remove_user_defined("install_year")
        'udf_1'
        >>> pipes.columns.restore_user_defined("install_year")
        'udf_2'

        """
        db_type = self._detached_type(name)
        if db_type is None:
            raise KeyError(f"'{name}' is not a detached column of {self._table.name}.")
        return self._attach(name, db_type, header=None)

    def remove_user_defined(self, name: str) -> str:
        """Remove a user-defined column, like "Remove column" in MIKE+.

        The column is no longer shown in MIKE+, but it stays in the database
        with its data and appears in `detached`. Restore it with
        `restore_user_defined`.

        Parameters
        ----------
        name : str
            Field name of the column. Case-insensitive.

        Returns
        -------
        str
            MUID of the removed `m_UserDefinedColumn` record.

        Raises
        ------
        KeyError
            If `name` isn't a user-defined column of this table.

        Examples
        --------
        >>> pipes = db.tables.msm_Link
        >>> pipes.columns.add_user_defined("install_year", "integer")
        'udf_1'
        >>> pipes.columns.remove_user_defined("install_year")
        'udf_1'
        >>> pipes.columns.detached
        ['install_year']

        """
        column = self._column_definition(name)
        if column is None or not column.IsUserDefined:
            raise KeyError(
                f"'{name}' is not a user-defined column of {self._table.name}."
            )

        field = column.Field
        muid = self._record_muid(field)
        # MIKE+ leaves the m_UserDefinedColumn record behind unless the field
        # name's casing matches it exactly.
        self._net_table.RemoveUserDefinedColumn(field, False)
        self._refresh()
        return muid

    @property
    def detached(self) -> list[str]:
        """Columns in the database that `restore_user_defined` can restore.

        These are database columns of the table that are neither standard MIKE+
        columns nor currently user-defined, for example after
        `remove_user_defined`.

        Returns
        -------
        list[str]
            Column names in lower case, as MIKE+ reports them. Methods taking a
            column name match them regardless of casing.

        """
        return list(self._net_table.GetAttachableUserDefinedColumns())

    def _detached_type(self, name: str) -> DbType | None:
        key = name.casefold()
        if not any(field.casefold() == key for field in self.detached):
            return None
        db_fields = self._net_table.UserDefinedDBfields
        return next(db_fields[f] for f in db_fields.Keys if f.casefold() == key)

    def _attach(self, name: str, db_type: DbType, header: str | None) -> str:
        self._net_table.AddUserDefinedColumn(
            UserDefinedColumnType.NewDbField,
            name if header is None else header,
            name,
            db_type,
            # Expression and result columns aren't supported yet.
            "",
            "",
            "",
            0,
            DateTime.MinValue,
            False,  # Reset from database
        )
        self._refresh()
        return self._record_muid(name)

    def _column_definition(self, name: str):
        key = name.casefold()
        for column in self._net_table.Columns:
            if column.Field.casefold() == key:
                return column
        return None

    def _record_muid(self, field: str) -> str:
        records = self._net_table.DataTables.GetTable("m_UserDefinedColumn")
        where = (
            f"tablename = {to_sql(self._table.name)} "
            f"AND lower(fieldname) = lower({to_sql(field)}) AND active = 1"
        )
        muid = next(iter(records.GetMuidsWhere(where)), None)
        if muid is None:
            raise RuntimeError(
                f"No m_UserDefinedColumn record for {self._table.name}.{field}."
            )
        return muid

    @property
    def user_defined(self) -> list[str]:
        """Names of the user-defined columns currently shown in MIKE+.

        Returns
        -------
        list[str]
            Column names in canonical casing.

        """
        return [
            column.Field for column in self._net_table.Columns if column.IsUserDefined
        ]

    def __getitem__(self, column_name: str) -> str:
        """Resolve a column name to its canonical MIKE+ casing.

        Parameters
        ----------
        column_name : str
            Column name in any casing.

        Returns
        -------
        str
            The canonical MIKE+ column name.

        Raises
        ------
        KeyError
            If no column matches ``column_name``.

        """
        return self._columns_by_name[column_name.casefold()]

    def db_types(self) -> dict[str, "DbType"]:
        """Map casefolded column names to their database types.

        Read from the .NET table on each call, unlike the cached names, so
        user-defined columns added after construction are included.

        Returns
        -------
        dict[str, DbType]
            Casefolded column names mapped to their ``DbType``.

        """
        return {
            column.Field.casefold(): column.DbType for column in self._net_table.Columns
        }

    def __iter__(self):
        """Make the columns iterable.

        Returns
        -------
        Iterator[str]
            Iterator over column names

        """
        return iter(self._column_names)

    def __contains__(self, item: object) -> bool:
        """Check for a column using case-insensitive matching.

        Parameters
        ----------
        item : str
            Column name in any casing.

        Returns
        -------
        bool
            Whether a matching column exists.

        """
        return isinstance(item, str) and item.casefold() in self._columns_by_name
