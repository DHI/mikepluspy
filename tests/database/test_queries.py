"""
Tests for the query classes implementing the fluent SQL API.
"""
import pytest
import pandas as pd

from mikeplus.database import Database


class TestBaseQuery:
    """Tests for the BaseQuery class."""
    
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
        # Use one that's guaranteed to exist
        return db.tables.msm_Link
    
    def test_where_clause(self, table):
        """Test adding where clauses."""
        query = table.select().where("Diameter > 10")
        assert "Diameter > 10" in query._where_clauses
        
        # Test that it's chainable
        result = query.execute()
        assert isinstance(result, dict)
        
        # Check if filtering worked correctly
        for muid, values in result.items():
            assert values['Diameter'] > 10
    
    def test_and_where_clause(self, table):
        """Test adding AND where clauses."""
        query = table.select().where("Diameter > 5").where("Diameter < 20")
        assert len(query._where_clauses) == 2
        
        result = query.execute()
        for muid, values in result.items():
            assert 5 < values['Diameter'] < 20
    
    def test_or_where_clause(self, table):
        """Test adding OR where clauses."""
        query = table.select().where("Diameter < 5").or_where("Diameter > 20")
        
        # The query should contain OR
        assert "OR" in query.build_query()
        
        result = query.execute()
        for muid, values in result.items():
            assert values['Diameter'] < 5 or values['Diameter'] > 20
    
    def test_parameters(self, table):
        """Test query parameters."""
        diameter_value = 15
        query = table.select().where("Diameter > ?", diameter_value)
        
        # Check parameters are stored
        assert query._parameters == [diameter_value]
        
        result = query.execute()
        for muid, values in result.items():
            assert values['Diameter'] > diameter_value
    
    def test_build_query(self, table):
        """Test building the complete query."""
        query = table.select('MUID', 'Diameter').where("Diameter > 10").order_by("Diameter")
        
        sql = query.build_query()
        assert "SELECT" in sql
        assert "MUID" in sql
        assert "Diameter" in sql
        assert "WHERE" in sql
        assert "ORDER BY" in sql


class TestSelectQuery:
    """Tests for the SelectQuery class."""
    
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
    
    def test_select_all_columns(self, table):
        """Test selecting all columns."""
        query = table.select()
        result = query.execute()
        
        assert isinstance(result, dict)
        assert len(result) > 0
        
        # Check that we have key data
        first_muid = next(iter(result))
        assert 'MUID' in result[first_muid]
        assert 'Diameter' in result[first_muid]
    
    def test_select_specific_columns(self, table):
        """Test selecting specific columns."""
        query = table.select('MUID', 'Diameter')
        result = query.execute()
        
        # Check that we only have the requested columns
        first_muid = next(iter(result))
        data = result[first_muid]
        assert len(data) == 2
        assert 'MUID' in data
        assert 'Diameter' in data
    
    def test_order_by(self, table):
        """Test ordering results."""
        query = table.select('MUID', 'Diameter').order_by('Diameter DESC')
        result = query.execute()
        
        # Get diameter values
        diameters = [data['Diameter'] for data in result.values()]
        
        # Check ordering is descending
        assert all(diameters[i] >= diameters[i+1] for i in range(len(diameters)-1))
    
    def test_limit(self, table):
        """Test limiting results."""
        limit = 5
        query = table.select().limit(limit)
        result = query.execute()
        
        assert len(result) <= limit
    
    def test_offset(self, table):
        """Test result offset."""
        # First get all results
        all_results = table.select('MUID').execute()
        all_muids = list(all_results.keys())
        
        # Then get with offset
        offset = 2
        offset_results = table.select('MUID').offset(offset).execute()
        offset_muids = list(offset_results.keys())
        
        # The offset results should match the original results offset by 'offset'
        assert offset_muids == all_muids[offset:]
    
    def test_execute(self, table):
        """Test query execution."""
        result = table.select('MUID', 'Diameter').execute()
        
        assert isinstance(result, dict)
        assert len(result) > 0
        
        # Get first record
        first_muid = next(iter(result))
        assert isinstance(result[first_muid], dict)
        assert 'MUID' in result[first_muid]
        assert 'Diameter' in result[first_muid]
    
    def test_to_pandas(self, table):
        """Test converting query result to pandas DataFrame."""
        df = table.select('MUID', 'Diameter').to_pandas()
        
        assert isinstance(df, pd.DataFrame)
        assert 'MUID' in df.columns
        assert 'Diameter' in df.columns
        assert len(df) > 0
    
    def test_get_muids(self, table):
        """Test the get_muids method."""
        muids = table.get_muids()
        
        assert isinstance(muids, list)
        assert len(muids) > 0
        
        # Check that all returned values are strings (MUIDs)
        assert all(isinstance(muid, str) for muid in muids)
    
    def test_get_muids_with_ordering(self, table):
        """Test get_muids with ordering."""
        muids = table.get_muids(order_by='MUID')
        
        # Check that the list is sorted
        assert muids == sorted(muids)


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
