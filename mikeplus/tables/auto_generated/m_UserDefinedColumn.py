from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_UserDefinedColumnTableColumns(BaseColumns):
    """Column names for m_UserDefinedColumn (m_UserDefinedColumn)."""
    MUID = "MUID"
    TableName = "TableName"
    FieldName = "FieldName"
    TypeNo = "TypeNo"
    HeaderText = "HeaderText"
    DataType = "DataType"
    Expression = "Expression"
    ResultFile = "ResultFile"
    ResultItem = "ResultItem"
    ResultValueType = "ResultValueType"
    ResultTimeStep = "ResultTimeStep"

class m_UserDefinedColumnTable(BaseTable):
    """Table for m_UserDefinedColumn (m_UserDefinedColumn)."""
    
    @property
    def columns(self) -> m_UserDefinedColumnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_UserDefinedColumnTableColumns(self)
        return self._columns