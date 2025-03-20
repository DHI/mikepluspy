from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_WeirTableColumns(BaseColumns):
    """Column names for mrm_Weir (Weirs)."""
    MUID = "MUID"
    Enabled = "Enabled"
    LinkID = "LinkID"
    Chainage = "Chainage"
    TypeNo = "TypeNo"
    GeomType = "GeomType"
    Datum = "Datum"
    GeomLinkID = "GeomLinkID"
    GeomTopoID = "GeomTopoID"
    GeomChainage = "GeomChainage"
    GeomWidth = "GeomWidth"
    GeomHeight = "GeomHeight"
    InvertLevel = "InvertLevel"
    CrestLevel = "CrestLevel"
    Coeff = "Coeff"
    ExpoCoeff = "ExpoCoeff"
    PO_i = "PO_i"
    PO_a = "PO_a"
    PO_b = "PO_b"
    PO_p = "PO_p"
    IO_Alpha = "IO_Alpha"
    IO_Beta = "IO_Beta"
    IO_q = "IO_q"
    SO_Gamma = "SO_Gamma"
    SO_Delta = "SO_Delta"
    SO_s = "SO_s"
    SO_r = "SO_r"
    HorizOffset = "HorizOffset"
    NonReturnNo = "NonReturnNo"
    NonReturnTypeNo = "NonReturnTypeNo"
    ApplyFactorNo = "ApplyFactorNo"
    FactorValue = "FactorValue"
    PosInflow = "PosInflow"
    PosOutflow = "PosOutflow"
    PosFreeOverflow = "PosFreeOverflow"
    NegInflow = "NegInflow"
    NegOutflow = "NegOutflow"
    NegFreeOverflow = "NegFreeOverflow"
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    AllowRecalculationNo = "AllowRecalculationNo"
    NoQhRelations = "NoQhRelations"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class mrm_WeirTable(BaseTable):
    """Table for mrm_Weir (Weirs)."""
    
    @property
    def columns(self) -> mrm_WeirTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_WeirTableColumns(self)
        return self._columns