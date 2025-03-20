from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_CulvertTableColumns(BaseColumns):
    """Column names for msm_Culvert (Culverts)."""
    MUID = "MUID"
    Enabled = "Enabled"
    LinkID = "LinkID"
    Chainage = "Chainage"
    GeomType = "GeomType"
    IrregularTypeNo = "IrregularTypeNo"
    GeomWidth = "GeomWidth"
    GeomHeight = "GeomHeight"
    GeomDiameter = "GeomDiameter"
    GeomLinkID = "GeomLinkID"
    GeomTopoID = "GeomTopoID"
    GeomChainage = "GeomChainage"
    UpstreamInvert = "UpstreamInvert"
    DownstreamInvert = "DownstreamInvert"
    Length = "Length"
    NumOfCulvert = "NumOfCulvert"
    HorizOffset = "HorizOffset"
    NonReturnNo = "NonReturnNo"
    NonReturnTypeNo = "NonReturnTypeNo"
    SectionTypeNo = "SectionTypeNo"
    ApplyFactorNo = "ApplyFactorNo"
    FactorValue = "FactorValue"
    ManningN = "ManningN"
    PosInflow = "PosInflow"
    PosOutflow = "PosOutflow"
    PosFreeOverflow = "PosFreeOverflow"
    PosBends = "PosBends"
    NegInflow = "NegInflow"
    NegOutflow = "NegOutflow"
    NegFreeOverflow = "NegFreeOverflow"
    NegBends = "NegBends"
    HeadLossCmTypeNo = "HeadLossCmTypeNo"
    AllowRecalculationNo = "AllowRecalculationNo"
    NoQhRelations = "NoQhRelations"
    DataSource = "DataSource"
    Element_S = "Element_S"
    Description = "Description"

class msm_CulvertTable(BaseTable):
    """Table for msm_Culvert (Culverts)."""
    
    @property
    def columns(self) -> msm_CulvertTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_CulvertTableColumns(self)
        return self._columns