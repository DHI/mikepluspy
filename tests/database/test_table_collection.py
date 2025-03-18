"""
Tests for the table collection classes.
"""
import pytest

from mikeplus.database import Database
from mikeplus.tables import BaseTable
from mikeplus.tables.auto_generated import msm_LinkTable

class TestBaseTableCollection:
    """Tests for the BaseTableCollection class."""
    
    @pytest.fixture(scope="class")
    def table_collection(self, session_sirius_db):
        """Fixture providing a TableCollection instance."""
        db = Database(session_sirius_db)
        yield db.tables
        db.close()
    
    def test_initialize_tables(self, table_collection):
        """Test initialize_tables method."""
        assert len(table_collection._tables) > 0
    
    def test_keys(self, table_collection):
        """Test keys method."""
        assert len(table_collection.keys()) > 0
        assert "msm_Link" in table_collection.keys()
        expected_tables = {t.TableName for t in table_collection._data_table_container.AllTables}
        assert set(table_collection.keys()) == expected_tables
    
    def test_values(self, table_collection):
        """Test values method."""
        assert len(table_collection.values()) > 0
        assert all(isinstance(t, BaseTable) for t in table_collection.values())
    
    def test_items(self, table_collection):
        """Test items method."""
        assert len(table_collection.items()) > 0
        for table_name, table in table_collection.items():
            assert isinstance(table_name, str)
            assert isinstance(table, BaseTable)
    
    def test_getitem(self, table_collection):
        """Test __getitem__ method."""
        assert isinstance(table_collection["msm_Link"], BaseTable)
        assert isinstance(table_collection["msm_Link"], msm_LinkTable)
    
    def test_getitem_nonexistent_table(self, table_collection):
        """Test __getitem__ with non-existent table name."""
        with pytest.raises(KeyError):
            table_collection["NonExistentTable"]
    
    def test_contains(self, table_collection):
        """Test __contains__ method."""
        assert "msm_Link" in table_collection
        assert "NonExistentTable" not in table_collection
    
    def test_iter(self, table_collection):
        """Test __iter__ method."""
        assert len(list(iter(table_collection))) > 0
    
    def test_table_access(self, table_collection):
        """Test accessing tables through the collection."""
        assert table_collection.msm_Link is table_collection["msm_Link"]
