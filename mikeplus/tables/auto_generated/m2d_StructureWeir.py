from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class m2d_StructureWeirTableColumns(BaseColumns):
    """Column names for m2d_StructureWeir (2D weirs)."""
    MUID = "MUID"
    """ID"""
    ApplyNo = "ApplyNo"
    """Apply"""
    WeirType = "WeirType"
    """Weir type"""
    DampDepth = "DampDepth"
    """Dampening delta depth [m]"""
    NonReturn = "NonReturn"
    """Non return flap"""
    FlowDistrib = "FlowDistrib"
    """Flow distribution"""
    Datum = "Datum"
    """Datum [m]"""
    R2Lin = "R2Lin"
    """LI, R-L"""
    R2Lout = "R2Lout"
    """LO, R-L"""
    L2Rin = "L2Rin"
    """LI, L-R"""
    L2Rout = "L2Rout"
    """LO, L-R"""
    R2LCalibration = "R2LCalibration"
    """CF,R-L"""
    L2RCalibration = "L2RCalibration"
    """CF, L-R"""
    VillemonteCoef = "VillemonteCoef"
    """Villemonte coeff."""
    VillemonteExp = "VillemonteExp"
    """Villemonte exponent."""
    HonmaCoef = "HonmaCoef"
    """Honma coeff."""
    Width = "Width"
    """Width [m]"""
    Height = "Height"
    """Height [m]"""
    InvertLevel = "InvertLevel"
    """Invert level [m]"""
    CrestLevel = "CrestLevel"
    """Crest level [m]"""
    DataSource = "DataSource"
    """Data source"""
    Element_S = "Element_S"
    """Status"""
    Description = "Description"
    """Description"""

class m2d_StructureWeirTable(BaseGeometryTable):
    """Table for m2d_StructureWeir (2D weirs)."""
    
    @property
    def columns(self) -> m2d_StructureWeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m2d_StructureWeirTableColumns(self)
        return self._columns