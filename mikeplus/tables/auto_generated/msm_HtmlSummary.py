from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HtmlSummaryTableColumns(BaseColumns):
    """Column names for msm_HtmlSummary (Network summary)."""
    MUID = "MUID"
    """ID"""
    SummaryNodeNo = "SummaryNodeNo"
    """Nodes"""
    SummaryWeirNo = "SummaryWeirNo"
    """Weirs & orifices"""
    SummaryPumpNo = "SummaryPumpNo"
    """Pumps"""
    SummaryLinkNo = "SummaryLinkNo"
    """Links"""
    SummaryLinkLevelNo = "SummaryLinkLevelNo"
    """Grid points, water levels"""
    SummaryLinkDischargeNo = "SummaryLinkDischargeNo"
    """Grid points, discharges"""
    SummaryLinkVelocityNo = "SummaryLinkVelocityNo"
    """Links, velocity"""
    SummaryLinkInputNo = "SummaryLinkInputNo"
    """Link input"""
    NodeSelectionNo = "NodeSelectionNo"
    """Node selection"""
    NodeSelectionName = "NodeSelectionName"
    """Node selection name"""
    LinkSelectionNo = "LinkSelectionNo"
    """Link selection"""
    LinkSelectionName = "LinkSelectionName"
    """Link selection name"""

class msm_HtmlSummaryTable(BaseTable):
    """Table for msm_HtmlSummary (Network summary)."""
    
    @property
    def columns(self) -> msm_HtmlSummaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HtmlSummaryTableColumns(self)
        return self._columns