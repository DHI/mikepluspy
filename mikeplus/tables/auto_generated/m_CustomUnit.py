from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_CustomUnitTableColumns(BaseColumns):
    """Column names for m_CustomUnit (m_CustomUnit)."""
    MUID = "MUID"
    UnitSystemNo = "UnitSystemNo"
    EumTypeNo = "EumTypeNo"
    TableName = "TableName"
    FieldName = "FieldName"
    CustomUnitNo = "CustomUnitNo"

class m_CustomUnitTable(BaseTable):
    """Table for m_CustomUnit (m_CustomUnit)."""
    
    @property
    def columns(self) -> m_CustomUnitTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_CustomUnitTableColumns(self)
        return self._columns