from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_StructureWeirTableColumns(BaseColumns):
    """Column names for m2d_StructureWeir (2D weirs)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    WeirType = "WeirType"
    DampDepth = "DampDepth"
    NonReturn = "NonReturn"
    FlowDistrib = "FlowDistrib"
    Datum = "Datum"
    R2Lin = "R2Lin"
    R2Lout = "R2Lout"
    L2Rin = "L2Rin"
    L2Rout = "L2Rout"
    R2LCalibration = "R2LCalibration"
    L2RCalibration = "L2RCalibration"
    VillemonteCoef = "VillemonteCoef"
    VillemonteExp = "VillemonteExp"
    HonmaCoef = "HonmaCoef"
    Width = "Width"
    Height = "Height"
    InvertLevel = "InvertLevel"
    CrestLevel = "CrestLevel"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class m2d_StructureWeirTable(BaseGeometryTable):
    """Table for m2d_StructureWeir (2D weirs)."""
    
    @property
    def columns(self) -> m2d_StructureWeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureWeirTableColumns(self)
        return self._columns