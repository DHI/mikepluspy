from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table import BaseColumns

class m_BookmarkTableColumns(BaseColumns):
    """Column names for m_Bookmark (m_Bookmark)."""
    MUID = "MUID"
    BottomLeftXCoor = "BottomLeftXCoor"
    BottomLeftYCoor = "BottomLeftYCoor"
    TopRightXCoor = "TopRightXCoor"
    TopRightYCoor = "TopRightYCoor"

class m_BookmarkTable(BaseTable):
    """Table for m_Bookmark (m_Bookmark)."""
    
    @property
    def columns(self) -> m_BookmarkTableColumns:
        """Get the columns for the table."""
        if self._columns is None:
            self._columns = m_BookmarkTableColumns(self)
        return self._columns