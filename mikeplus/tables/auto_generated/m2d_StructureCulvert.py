from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m2d_StructureCulvertTableColumns(BaseColumns):
    """Column names for m2d_StructureCulvert (2D culverts)."""
    MUID = "MUID"
    ApplyNo = "ApplyNo"
    CulvertType = "CulvertType"
    GeomTypeNo = "GeomTypeNo"
    Width = "Width"
    Height = "Height"
    Diameter = "Diameter"
    NumberCulverts = "NumberCulverts"
    USLevel = "USLevel"
    DSLevel = "DSLevel"
    Length = "Length"
    Manning = "Manning"
    DampDepth = "DampDepth"
    NonReturn = "NonReturn"
    FlowDistrib = "FlowDistrib"
    SectionType = "SectionType"
    Momentum = "Momentum"
    R2Lin = "R2Lin"
    R2Lout = "R2Lout"
    R2Lbend = "R2Lbend"
    L2Rin = "L2Rin"
    L2Rout = "L2Rout"
    L2Rbend = "L2Rbend"
    R2LCalibration = "R2LCalibration"
    L2RCalibration = "L2RCalibration"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class m2d_StructureCulvertTable(BaseTable):
    """Table for m2d_StructureCulvert (2D culverts)."""
    
    @property
    def columns(self) -> m2d_StructureCulvertTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureCulvertTableColumns(self)
        return self._columns