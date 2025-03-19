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
    def base_query(self, module_sirius_db):
        """Fixture providing a BaseQuery instance."""
        db = Database(module_sirius_db)
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
    
    @pytest.fixture
    def db(self, sirius_db):
        """Fixture providing a Database instance."""
        # Use the sirius_db fixture from conftest.py
        db = Database(sirius_db)
        yield db
        db.close()
    
    @pytest.fixture
    def table(self, db):
        """Fixture providing a real table from the database."""
        # Get a real table from the database
        return db.tables.msm_Link
    
    def test_insert_with_kwargs(self, table):
        """Test inserting with keyword arguments."""
        test_muid = 'test_insert_query'
        result_muid = table.insert(
            MUID=test_muid,
            Diameter=12.5
        )
        
        assert result_muid == test_muid
        
        # Verify the insertion
        result = table.select().where(f"MUID='{test_muid}'").execute()
        assert test_muid in result
        assert result[test_muid]['Diameter'] == 12.5
        
        # Clean up
        table.delete().where(f"MUID='{test_muid}'").execute()
    
    def test_insert_auto_muid(self, table):
        """Test inserting without specifying MUID."""
        muid = table.insert(Diameter=99.9)
        
        assert muid is not None
        assert isinstance(muid, str)
        
        # Verify the insertion
        result = table.select().where(f"MUID='{muid}'").execute()
        assert muid in result
        assert result[muid]['Diameter'] == 99.9
        
        # Clean up
        table.delete().where(f"MUID='{muid}'").execute()


class TestUpdateQuery:
    """Tests for the UpdateQuery class."""
    
    @pytest.fixture
    def db(self, sirius_db):
        """Fixture providing a Database instance."""
        # Use the sirius_db fixture from conftest.py
        db = Database(sirius_db)
        yield db
        db.close()
    
    @pytest.fixture
    def table(self, db):
        """Fixture providing a real table from the database."""
        # Get a real table from the database
        return db.tables.msm_Link
    
    @pytest.fixture
    def test_record(self, table):
        """Fixture providing a test record that will be cleaned up."""
        test_muid = 'test_update_query'
        table.insert(
            MUID=test_muid,
            Diameter=10.0
        )
        
        yield test_muid
        
        # Clean up
        table.delete().where(f"MUID='{test_muid}'").execute()
    
    def test_set_values(self, table, test_record):
        """Test setting values to update."""
        # Update the test record
        query = table.update().set(Diameter=20.0).where(f"MUID='{test_record}'")
        
        # Check query properties
        assert query._set_values == {'Diameter': 20.0}
        assert f"MUID='{test_record}'" in query._where_clauses
        
        # Execute the update
        rows_affected = query.execute()
        assert rows_affected == 1
        
        # Verify the update
        result = table.select().where(f"MUID='{test_record}'").execute()
        assert test_record in result
        assert result[test_record]['Diameter'] == 20.0
    
    def test_multiple_set_values(self, table, test_record):
        """Test setting multiple values to update."""
        # Update with multiple values
        rows_affected = (
            table.update()
            .set(Diameter=30.0, DwLevel=5.5)
            .where(f"MUID='{test_record}'")
            .execute()
        )
        
        assert rows_affected == 1
        
        # Verify the update
        result = table.select().where(f"MUID='{test_record}'").execute()
        assert result[test_record]['Diameter'] == 30.0
        assert result[test_record]['DwLevel'] == 5.5


class TestDeleteQuery:
    """Tests for the DeleteQuery class."""
    
    @pytest.fixture
    def db(self, sirius_db):
        """Fixture providing a Database instance."""
        # Use the sirius_db fixture from conftest.py
        db = Database(sirius_db)
        yield db
        db.close()
    
    @pytest.fixture
    def table(self, db):
        """Fixture providing a real table from the database."""
        # Get a real table from the database
        return db.tables.msm_Link
    
    def test_execute(self, table):
        """Test query execution."""
        # First insert a test record
        test_muid = 'test_delete_query'
        table.insert(
            MUID=test_muid,
            Diameter=42.0
        )
        
        # Verify it exists
        result = table.select().where(f"MUID='{test_muid}'").execute()
        assert test_muid in result
        
        # Delete it
        rows_affected = table.delete().where(f"MUID='{test_muid}'").execute()
        assert rows_affected == 1
        
        # Verify it's gone
        result = table.select().where(f"MUID='{test_muid}'").execute()
        assert test_muid not in result
    
    def test_chained_delete(self, table):
        """Test chained delete query."""
        # Insert two test records
        test_muid1 = 'test_delete_query1'
        test_muid2 = 'test_delete_query2'
        
        table.insert(MUID=test_muid1, Diameter=50.0)
        table.insert(MUID=test_muid2, Diameter=50.0)
        
        # Delete with chained conditions
        rows_affected = (
            table.delete()
            .where(f"MUID='{test_muid1}'")
            .or_where(f"MUID='{test_muid2}'")
            .execute()
        )
        
        assert rows_affected == 2
        
        # Verify both are gone
        result = table.select().where(f"MUID='{test_muid1}' OR MUID='{test_muid2}'").execute()
        assert len(result) == 0
