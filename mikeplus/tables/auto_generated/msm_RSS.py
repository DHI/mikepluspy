from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_RSSTableColumns(BaseColumns):
    """Column names for msm_RSS (Result selections)."""
    MUID = "MUID"
    ResultSpecID = "ResultSpecID"
    SelectionNo = "SelectionNo"
    SubsetNo = "SubsetNo"
    IndividualNo = "IndividualNo"
    SelectionListID = "SelectionListID"
    ElementID = "ElementID"
    GridPointNo = "GridPointNo"
    Chainage = "Chainage"
    InterpolationTypeNo = "InterpolationTypeNo"
    GridPointWettingNo = "GridPointWettingNo"
    CellSize = "CellSize"
    Rotation = "Rotation"
    ExtentDef = "ExtentDef"
    LowerLeftX = "LowerLeftX"
    LowerLeftY = "LowerLeftY"
    LengthX = "LengthX"
    LengthY = "LengthY"
    NoCellsX = "NoCellsX"
    NoCellsY = "NoCellsY"
    WQComponentID = "WQComponentID"
    ItemNo = "ItemNo"
    TypeNo = "TypeNo"
    DrawOnMap = "DrawOnMap"
    FormatNo = "FormatNo"
    FormatDelimiter = "FormatDelimiter"
    FormatColumnWidth = "FormatColumnWidth"
    FormatDecimalNum = "FormatDecimalNum"
    FormatMaxNo = "FormatMaxNo"
    FormatTimeMaxNo = "FormatTimeMaxNo"
    FormatMinNo = "FormatMinNo"
    FormatTimeMinNo = "FormatTimeMinNo"

class msm_RSSTable(BaseTable):
    """Table for msm_RSS (Result selections)."""
    
    @property
    def columns(self) -> msm_RSSTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_RSSTableColumns(self)
        return self._columns