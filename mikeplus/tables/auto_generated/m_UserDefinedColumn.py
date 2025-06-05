from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_UserDefinedColumnTableColumns(BaseColumns):
    """Column names for m_UserDefinedColumn (m_UserDefinedColumn)."""
    MUID = "MUID"
    """ID"""
    TableName = "TableName"
    """Table name"""
    FieldName = "FieldName"
    """Field name"""
    TypeNo = "TypeNo"
    """TypeNo"""
    HeaderText = "HeaderText"
    """HeaderText"""
    DataType = "DataType"
    """DataType"""
    Expression = "Expression"
    """Expression"""
    ResultFile = "ResultFile"
    """ResultFile"""
    ResultItem = "ResultItem"
    """ResultItem"""
    ResultValueType = "ResultValueType"
    """ResultValueType"""
    ResultTimeStep = "ResultTimeStep"
    """ResultTimeStep"""

class m_UserDefinedColumnTable(BaseTable):
    """Table for m_UserDefinedColumn (m_UserDefinedColumn)."""
    
    @property
    def columns(self) -> m_UserDefinedColumnTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_UserDefinedColumnTableColumns(self)
        return self._columns