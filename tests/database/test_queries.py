"""
Tests for the query classes implementing the fluent SQL API.
"""
import pytest
import pandas as pd

from mikeplus.database import Database
from mikeplus.queries import BaseQuery
from mikeplus.queries import SelectQuery
from mikeplus.queries import InsertQuery
from mikeplus.queries import UpdateQuery
from mikeplus.queries import DeleteQuery
from mikeplus.tables.base_table import BaseTable


class TestBaseQuery:
    """Tests for the BaseQuery class."""

    class BaseQueryTest(BaseQuery[bool]):
        """Test class for BaseQuery."""
        def _execute_impl(self) -> bool:
            return True

    @pytest.fixture
    def base_query(self, session_sirius_db):
        """Fixture providing a BaseQuery instance."""
        db = Database(session_sirius_db)
        table = db.tables.msm_Link
        return self.BaseQueryTest(table)
    
    def test_where_clause(self, base_query: BaseQueryTest):
        """Test adding where clauses."""
        query = base_query.where("Diameter > 10")
        assert "Diameter > 10" in query._conditions
        assert query._params == {}
    
    def test_and_where_clause(self, base_query: BaseQueryTest):
        """Test adding AND where clauses."""
        query = base_query.where("Diameter > 5").where("Diameter < 20")
        assert len(query._conditions) == 2
        assert query._params == {}    

    def test_parameters(self, base_query: BaseQueryTest):
        """Test query parameters."""
        diameter_value = 15
        query = base_query.where("Diameter > :diameter", {"diameter": diameter_value})
        
        # Check parameters are stored
        assert query._params == {"diameter": diameter_value}
    
    def test_execute(self, base_query: BaseQueryTest):
        """Test query execution."""
        assert base_query.execute()


class TestSelectQuery:
    """Tests for the SelectQuery class."""
    
    @pytest.fixture(scope="class")
    def table(self, session_sirius_db):
        """Fixture providing a real table from the database."""
        db = Database(session_sirius_db)
        yield db.tables.msm_Link
        db.close()
    
    def test_select_all_columns(self, table: BaseTable):
        """Test selecting all columns validates correctly."""
        query = SelectQuery(table)
        all_columns = list(table.columns)
        assert query._columns == all_columns
    
    def test_select_specific_columns(self, table):
        """Test selecting specific columns validates correctly."""
        query = SelectQuery(table, ["MUID", "Diameter"])
        assert query._columns == ['MUID', 'Diameter']
    
    def test_invalid_columns(self, table):
        """Test selecting invalid columns raises a ValueError."""
        with pytest.raises(ValueError):
            SelectQuery(table, ["NonExistentColumn"])
    
    def test_order_by(self, table):
        """Test setting order_by clause."""
        query = SelectQuery(table, ["MUID", "Diameter"])
        query.order_by('Diameter')
        assert query._order_by is not None
    
    def test_execute_all_columns(self, table):
        """Test execution with all columns selected."""
        query = SelectQuery(table)
        result = query.execute()
        
        assert isinstance(result, dict)
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, list) for value in result.values())
        
        expected_number_row = 8
        assert len(result) == expected_number_row
        expected_number_columns = len(list(table.columns))
        assert len(list(result.values())[0]) == expected_number_columns
        assert "Link_2" in result
    
    def test_execute_specific_columns(self, table):
        """Test execution with specific columns selected."""
        query = SelectQuery(table, ["MUID", "Diameter"])
        result = query.execute()
        
        assert isinstance(result, dict)
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, list) for value in result.values())
        
        expected_number_columns = 2
        assert len(list(result.values())[0]) == expected_number_columns
        assert "Link_2" in result
        assert result["Link_2"] == ["Link_2", 1.0]
    
    def test_execute_with_ordering(self, table: BaseTable):
        """Test execution with order_by clause."""
        muids = table.get_muids()
        assert len(muids) > 0

        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.order_by('MUID')
        result = query.execute()
        
        result_keys = list(result.keys())
        assert result_keys == sorted(muids)

        query.reset().order_by('MUID', descending=True)
        result = query.execute()
        
        result_keys = list(result.keys())
        assert result_keys == sorted(muids, reverse=True)

        query = SelectQuery(table, ["Length"])
        lengths = query.execute()
        max_length = max(lengths.values())
        min_length = min(lengths.values())

        assert max_length > min_length
        
        query.reset().order_by('Length', descending=True)
        lengths = list(query.execute().values())
        
        assert lengths[0] == max_length

        query.reset().order_by('Length', descending=False)
        lengths = list(query.execute().values())
        
        assert lengths[0] == min_length
        

    def test_execute_with_where(self, table):
        """Test execution with where clause."""
        # Test basic where clause
        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.where("Diameter = 1.0")
        result = query.execute()
        
        # Verify we only get links with Diameter = 1.0
        assert isinstance(result, dict)
        assert all(row[1] == 1.0 for row in result.values())
        
        # Test where clause with parameters
        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.where("Diameter > :min_diameter", {"min_diameter": 0.5})
        result = query.execute()
        
        # Verify we only get links with Diameter > 0.5
        assert isinstance(result, dict)
        assert all(row[1] > 0.5 for row in result.values())

        # Verify we get no links for an unreasonable high Diameter
        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.where("Diameter > 100.0")
        result = query.execute()
        assert isinstance(result, dict)
        assert len(result) == 0
        
        # Test getting a single row
        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.where("MUID = 'Link_2'")
        result = query.execute()
        
        # Verify we only get the row with MUID = Link_2
        assert isinstance(result, dict)
        assert len(result) == 1
        assert result["Link_2"] == ["Link_2", 1.0]

        # Test getting multiple MUIDs with IN clause
        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.where("MUID IN ('Link_2', 'Link_29')")
        result = query.execute()
        
        # Verify we get the rows with MUID = Link_2 and MUID = Link_29
        assert isinstance(result, dict)
        assert len(result) == 2
        assert result["Link_2"] == ["Link_2", 1.0]
        assert result["Link_29"] == ["Link_29", 1.0]

        # Test an empty result
        query = SelectQuery(table, ["MUID", "Diameter"])
        query = query.where("MUID = 'Link_2'")
        query = query.where("MUID = 'Link_29'")
        result = query.execute()
        
        # Verify we get no rows
        assert isinstance(result, dict)
        assert len(result) == 0
        
    
    def test_to_pandas(self, table):
        """Test converting query result to pandas DataFrame."""
        df = SelectQuery(table, ["MUID", "Diameter"]).to_pandas()
        
        assert isinstance(df, pd.DataFrame)
        assert list(df.columns) == ["MUID", "Diameter"]
        assert len(df) == 8
        assert "Link_2" in df.index
        assert df['Diameter'].sum() == 8.0


class TestInsertQuery:
    """Tests for the InsertQuery class."""
    
    @pytest.fixture(scope="class")
    def table(self, class_sirius_db):
        """Fixture providing a real table from the database."""
        db = Database(class_sirius_db)
        yield db.tables.msm_Link
        db.close()
    
    def test_insert(self, table: BaseTable):
        """Test inserting with keyword arguments."""
        values = {
            "MUID" : "my_test_link",
            "Diameter" : 12.5,
            "Length" : 100.0,
            "Description" : "Test link"
        }
        query = InsertQuery(table, values)
        inserted_muid = query.execute()
        
        assert inserted_muid == values["MUID"]
        assert inserted_muid in table.get_muids()

        inserted_values = table.select(list(values.keys())).execute()[values["MUID"]]
        inserted_values = dict(zip(list(values.keys()), inserted_values))
        assert values == inserted_values
    
    def test_insert_auto_muid(self, table):
        """Test inserting without specifying MUID."""
        values = {
            "Diameter" : 12.5,
            "Length" : 100.0,
            "Description" : "Test link"
        }
        query = InsertQuery(table, values)
        inserted_muid = query.execute()
        
        assert inserted_muid is not None
        assert isinstance(inserted_muid, str)
        
        assert inserted_muid in table.get_muids()

    def test_insert_empty_values(self, table):
        """Test inserting with empty values."""
        values = {}
        query = InsertQuery(table, values)
        inserted_muid = query.execute()
        
        assert inserted_muid is not None
        assert isinstance(inserted_muid, str)
        
        assert inserted_muid in table.get_muids()


class TestUpdateQuery:
    """Tests for the UpdateQuery class."""
    
    @pytest.fixture(scope="class")
    def table(self, class_sirius_db):
        """Fixture providing a real table from the database."""
        db = Database(class_sirius_db)
        yield db.tables.msm_Link
        db.close()

    def test_safety_check(self, table):
        """Test that trying to update all rows without all() raises an error."""
        values = {
            "Diameter" : 99.0,
        }
        query = UpdateQuery(table, values)
        with pytest.raises(ValueError):
            query.execute()  
    
    def test_set_values_all(self, table):
        """Test setting values to update all rows with explicit all() call."""
        values = {
            "Diameter" : 42.0,
            "Description" : "Updated link",
        }

        existing_values = table.select(list(values.keys())).execute()
        for muid in existing_values:
            existing_values[muid] = dict(zip(list(values.keys()), existing_values[muid]))
            

        for muid, existing_value in existing_values.items():
            assert values != existing_value, f"Values do not match for MUID {muid}"

        query = UpdateQuery(table, values)
        # Call all() to explicitly update all rows
        muids_updated = query.all().execute()
        assert muids_updated == table.get_muids(), "All records should have been updated"

        updated_values = table.select(list(values.keys())).execute()
        for muid, updated_value in updated_values.items():
            updated_value = dict(zip(list(values.keys()), updated_value))
            assert values == updated_value, f"Values do not match for MUID {muid}"
    
    def test_update_with_where_clause(self, table):
        """Test updating rows with a where clause to filter them."""
        # Get all MUIDs first to check the count
        all_muids = table.get_muids()
        assert len(all_muids) > 1, "Need at least 2 rows for testing where clause"
        
        # Define the values to update
        values = {
            "Diameter": 99.9,
            "Description": "test_update_with_where_clause"
        }
        
        # Get a specific MUID to filter on
        target_muid = all_muids[0]
        
        # Create the update query with a where clause
        query = UpdateQuery(table, values)
        muids_updated = query.where("MUID = :muid", {"muid": target_muid}).execute()
        
        # Verify only one row was updated
        assert len(muids_updated) == 1, "Only one row should be updated"
        assert muids_updated[0] == target_muid, "The targeted MUID should be updated"
        
        # Verify the values were updated for the target MUID
        updated_data = table.select(list(values.keys())).where("MUID = :muid", {"muid": target_muid}).execute()
        updated_row = dict(zip(list(values.keys()), updated_data[target_muid]))
        assert updated_row == values, "The values should be updated for the targeted row"
        
        # Verify other rows were not updated
        other_muid = all_muids[1]  # Get another MUID
        other_data = table.select(list(values.keys())).where("MUID = :muid", {"muid": other_muid}).execute()
        other_row = dict(zip(list(values.keys()), other_data[other_muid]))
        assert other_row != values, "Other rows should not be updated"


class TestDeleteQuery:
    """Tests for the DeleteQuery class."""
    
    @pytest.fixture(scope="class")
    def table(self, class_sirius_db):
        """Fixture providing a real table from the database."""
        db = Database(class_sirius_db)
        yield db.tables.msm_Link
        db.close()

    def test_safety_check(self, table):
        """Test that trying to delete all rows without all() raises an error."""
        query = DeleteQuery(table)
        with pytest.raises(ValueError):
            query.execute()
    
    def test_delete_all(self, table):
        """Test deleting all rows with explicit all() call."""
        initial_muids = table.get_muids()
        assert len(initial_muids) > 0, "Table needs to have rows for test"
        
        query = DeleteQuery(table)
        # Call all() to explicitly delete all rows
        deleted_muids = query.all().execute()
        
        assert sorted(deleted_muids) == sorted(initial_muids), "All records should have been deleted"
        assert len(table.get_muids()) == 0, "Table should be empty after delete"
    
    def test_delete_with_where_clause(self, table):
        """Test deleting rows with a where clause to filter them."""
        # First, ensure we have at least a couple of rows to work with
        # Insert some test data
        link1 = {
            "Diameter": 100.0,
            "Description": "test_delete_with_where_clause_1"
        }
        link2 = {
            "Diameter": 200.0,
            "Description": "test_delete_with_where_clause_2"
        }
        
        muid1 = table.insert(link1)
        muid2 = table.insert(link2)
        
        # Confirm both records exist
        all_muids = table.get_muids()
        assert muid1 in all_muids, "First test record should exist"
        assert muid2 in all_muids, "Second test record should exist"
        
        # Delete only the first record using a where clause
        query = DeleteQuery(table)
        deleted_muids = query.where("MUID = :muid", {"muid": muid1}).execute()
        
        # Verify only the first record was deleted
        assert len(deleted_muids) == 1, "Only one row should be deleted"
        assert deleted_muids[0] == muid1, "The targeted MUID should be deleted"
        
        # Verify the first record is gone
        new_muids = table.get_muids()
        assert muid1 not in new_muids, "First record should be deleted"
        assert muid2 in new_muids, "Second record should still exist"
        
        # Delete the second row by diameter filter
        query = DeleteQuery(table)
        deleted_muids = query.where("Diameter = :diameter", {"diameter": 200.0}).execute()
        
        # Verify only the second record was deleted
        assert len(deleted_muids) == 1, "Only one row should be deleted"
        assert deleted_muids[0] == muid2, "The targeted MUID should be deleted"
        
        # Verify the second record is gone
        new_muids = table.get_muids()
        assert muid2 not in new_muids, "Second record should be deleted"
