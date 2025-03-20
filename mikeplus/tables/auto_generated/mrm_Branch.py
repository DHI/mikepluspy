from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class mrm_BranchTableColumns(BaseColumns):
    """Column names for mrm_Branch (Rivers)."""
    MUID = "MUID"
    Name = "Name"
    Enabled = "Enabled"
    UpstrID = "UpstrID"
    UpstrTypeNo = "UpstrTypeNo"
    UpstrChainage = "UpstrChainage"
    DwnstrID = "DwnstrID"
    DwnstrTypeNo = "DwnstrTypeNo"
    DwnstrChainage = "DwnstrChainage"
    TopographyID = "TopographyID"
    MaxDx = "MaxDx"
    FlowDirectionTypeNo = "FlowDirectionTypeNo"
    StartChainage = "StartChainage"
    EndChainage = "EndChainage"
    TypeNo = "TypeNo"
    DataSource = "DataSource"
    AssetName = "AssetName"
    Element_S = "Element_S"
    NetTypeNo = "NetTypeNo"
    SpecLocalWaveNo = "SpecLocalWaveNo"
    WaveApproximationTypeNo = "WaveApproximationTypeNo"
    Description = "Description"

class mrm_BranchTable(BaseTable):
    """Table for mrm_Branch (Rivers)."""
    
    @property
    def columns(self) -> mrm_BranchTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BranchTableColumns(self)
        return self._columns