from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mw_PipeTableColumns(BaseColumns):
    """Column names for mw_Pipe (Pipes)."""
    MUID = "MUID"
    FromNodeID = "FromNodeID"
    ToNodeID = "ToNodeID"
    L = "L"
    Diameter = "Diameter"
    Thickness = "Thickness"
    Inner_Diameter = "Inner_Diameter"
    GeometricLength = "GeometricLength"
    StatusNo = "StatusNo"
    ZoneID = "ZoneID"
    Enabled = "Enabled"
    RCoeff = "RCoeff"
    LCoeff = "LCoeff"
    PN = "PN"
    Material = "Material"
    CDate = "CDate"
    Coeff1 = "Coeff1"
    Coeff2 = "Coeff2"
    Coeff3 = "Coeff3"
    Coeff4 = "Coeff4"
    Bulk_Coeff = "Bulk_Coeff"
    Wall_Coeff = "Wall_Coeff"
    WaveSpeed = "WaveSpeed"
    CVTimeOpen = "CVTimeOpen"
    CVTimeClose = "CVTimeClose"
    CVPressure = "CVPressure"
    CVVelocity = "CVVelocity"
    CVStatOpen = "CVStatOpen"
    CVReverseQ = "CVReverseQ"
    CVInterval = "CVInterval"
    CVCanReopen = "CVCanReopen"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    StreetName = "StreetName"
    Description = "Description"
    Note = "Note"
    GroupID = "GroupID"
    PMapZone = "PMapZone"
    UserLno = "UserLno"

class mw_PipeTable(BaseGeometryTable):
    """Table for mw_Pipe (Pipes)."""
    
    @property
    def columns(self) -> mw_PipeTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mw_PipeTableColumns(self)
        return self._columns