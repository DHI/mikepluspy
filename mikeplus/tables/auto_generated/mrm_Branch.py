from mikeplus.tables.base_geometry_table import BaseGeometryTable
from mikeplus.tables.base_geometry_table import BaseColumns

class mrm_BranchTableColumns(BaseColumns):
    """Column names for mrm_Branch (Rivers)."""
    MUID = "MUID"
    """ID"""
    Name = "Name"
    """Name"""
    Enabled = "Enabled"
    """Apply"""
    UpstrID = "UpstrID"
    """Upstream"""
    UpstrTypeNo = "UpstrTypeNo"
    """Upstream type"""
    UpstrChainage = "UpstrChainage"
    """Chainage [m]"""
    DwnstrID = "DwnstrID"
    """Downstream"""
    DwnstrTypeNo = "DwnstrTypeNo"
    """Downstream type"""
    DwnstrChainage = "DwnstrChainage"
    """Chainage [m]"""
    TopographyID = "TopographyID"
    """Topo ID"""
    MaxDx = "MaxDx"
    """Max dx [m]"""
    FlowDirectionTypeNo = "FlowDirectionTypeNo"
    """Flow direction"""
    StartChainage = "StartChainage"
    """Start chainage [m]"""
    EndChainage = "EndChainage"
    """End chainage [m]"""
    TypeNo = "TypeNo"
    """River type"""
    DataSource = "DataSource"
    """Data source"""
    AssetName = "AssetName"
    """Asset ID"""
    Element_S = "Element_S"
    """Element status"""
    NetTypeNo = "NetTypeNo"
    """Network type"""
    SpecLocalWaveNo = "SpecLocalWaveNo"
    """Use specified local wave approximation"""
    WaveApproximationTypeNo = "WaveApproximationTypeNo"
    """WaveApproximationTypeNo"""
    Description = "Description"
    """Description"""

class mrm_BranchTable(BaseGeometryTable):
    """Table for mrm_Branch (Rivers)."""
    
    @property
    def columns(self) -> mrm_BranchTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = mrm_BranchTableColumns(self)
        return self._columns