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

    class BaseQueryTest(BaseQuery):
        """Test class for BaseQuery."""
        def execute(self):
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
        query = base_query.where("Diameter > :diameter", diameter=diameter_value)
        
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
    
    def test_execute_with_ordering(self, table):
        """Test execution with order_by clause."""
        return False

    def test_execute_with_where(self, table):
        """Test execution with where clause."""
        return False
    
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
        existing_muids = table.get_muids()
        query = DeleteQuery(table)
        # Call all() to explicitly delete all rows
        deleted_muids = query.all().execute()
        assert deleted_muids == existing_muids
        assert table.get_muids() == []
    
