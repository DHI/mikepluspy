"""
Tests for the model_database module functionality.
"""
import pytest
from pathlib import Path
from typing import TYPE_CHECKING

from mikeplus.model_database import ModelDatabase

class TestModelDatabaseOpen:
    """Tests for the model_database.open function."""

    def test_open_existing_model(self, session_sirius_db: Path):
        """Test opening an existing model database."""
        # Open via constructor
        mdb = ModelDatabase(session_sirius_db)
        assert isinstance(mdb, ModelDatabase)
        assert mdb.is_open
        assert mdb.db_path == session_sirius_db
        assert mdb.mupp_path == session_sirius_db.with_suffix(".mupp")
        mdb.close()
        assert not mdb.is_open

        # Open via constructor (without auto-open)
        mdb2 = ModelDatabase(session_sirius_db, auto_open=False)
        assert isinstance(mdb2, ModelDatabase)
        assert not mdb2.is_open
        assert mdb2.db_path == session_sirius_db
        assert mdb2.mupp_path == session_sirius_db.with_suffix(".mupp")
        mdb2.close()
        assert not mdb2.is_open

        # Open via context manager
        with ModelDatabase(session_sirius_db) as mdb3:
            assert mdb3.is_open
            assert mdb3.db_path == session_sirius_db
            assert mdb3.mupp_path == session_sirius_db.with_suffix(".mupp")

        assert not mdb3.is_open

    
    def test_open_nonexistent_model_raises_error(self):
        """Test that opening a non-existent model raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            ModelDatabase(Path("/path/to/nonexistent/model.mupp"))
    
    def test_open_with_create_if_not_exists(self, tmp_path):
        """Test opening with create_if_not_exists=True creates a new database."""
        # TODO: Implement test
        assert False

class TestModelDatabaseCreate:
    """Tests for the model_database.create function."""

    def test_create_new_model(self, tmp_path):
        """Test creating a new model database."""
        # TODO: Implement test
        assert False
    
    def test_create_existing_model_raises_error(self, sirius_db):
        """Test that creating an existing model raises FileExistsError."""
        # TODO: Implement test
        assert False
    
    def test_create_with_pathlib_path(self, tmp_path):
        """Test creating with a pathlib.Path object."""
        # TODO: Implement test
        assert False


class TestModelDatabase:
    """Tests for the ModelDatabase class."""

    @pytest.fixture
    def model_db(self, sirius_db):
        """Fixture providing a test ModelDatabase instance."""
        # TODO: Implement fixture to provide a test database using existing fixtures
        db = model_database.open(sirius_db)
        yield db
        db.close()
    
    def test_is_open(self, model_db):
        """Test is_open property."""
        # TODO: Implement test
        assert False
    
    def test_tables_property(self, model_db):
        """Test tables property returns a TableCollection."""
        # TODO: Implement test
        assert False
    
    def test_unit_system(self, model_db):
        """Test unit_system property."""
        # TODO: Implement test
        assert False
    
    def test_version(self, model_db):
        """Test version property."""
        # TODO: Implement test
        assert False
    
    def test_active_scenario(self, model_db):
        """Test active_scenario property."""
        # TODO: Implement test
        assert False
    
    def test_set_active_scenario(self, model_db):
        """Test set_active_scenario method."""
        # TODO: Implement test
        assert False
    
    def test_active_simulation(self, model_db):
        """Test active_simulation property."""
        # TODO: Implement test
        assert False
    
    def test_set_active_simulation(self, model_db):
        """Test set_active_simulation method."""
        # TODO: Implement test
        assert False
    
    def test_active_model(self, model_db):
        """Test active_model property."""
        # TODO: Implement test
        assert False
    
    def test_create_scenario(self, model_db):
        """Test create_scenario method."""
        # TODO: Implement test
        assert False
    
    def test_close(self, model_db):
        """Test close method."""
        # TODO: Implement test
        assert False
