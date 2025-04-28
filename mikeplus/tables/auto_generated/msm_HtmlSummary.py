from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class msm_HtmlSummaryTableColumns(BaseColumns):
    """Column names for msm_HtmlSummary (Network summary)."""
    MUID = "MUID"
    SummaryNodeNo = "SummaryNodeNo"
    SummaryWeirNo = "SummaryWeirNo"
    SummaryPumpNo = "SummaryPumpNo"
    SummaryLinkNo = "SummaryLinkNo"
    SummaryLinkLevelNo = "SummaryLinkLevelNo"
    SummaryLinkDischargeNo = "SummaryLinkDischargeNo"
    SummaryLinkVelocityNo = "SummaryLinkVelocityNo"
    SummaryLinkInputNo = "SummaryLinkInputNo"
    NodeSelectionNo = "NodeSelectionNo"
    NodeSelectionName = "NodeSelectionName"
    LinkSelectionNo = "LinkSelectionNo"
    LinkSelectionName = "LinkSelectionName"

class msm_HtmlSummaryTable(BaseTable):
    """Table for msm_HtmlSummary (Network summary)."""
    
    @property
    def columns(self) -> msm_HtmlSummaryTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = msm_HtmlSummaryTableColumns(self)
        return self._columns