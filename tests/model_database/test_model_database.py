"""
Tests for the model_database module functionality.
"""
import pytest
from pathlib import Path
from typing import TYPE_CHECKING

from mikeplus.model_database import ModelDatabase
from mikeplus.tables.auto_generated import TableCollection

class TestModelDatabaseOpen:
    """Tests for the ModelDatabase opening functionality."""

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

        with pytest.raises(FileNotFoundError):
            ModelDatabase(Path("/path/to/nonexistent/model.sqlite"))

class TestModelDatabaseCreate:
    """Tests for the ModelDatabase creation functionality."""

    def test_create_new_model(self, tmp_path: Path):
        """Test creating a new model database."""
        db_path = tmp_path / "model.sqlite"

        # Create model database
        mdb = ModelDatabase.create(db_path)
        assert isinstance(mdb, ModelDatabase)
        assert mdb.is_open
        assert mdb.db_path == db_path
        mdb.close()
        assert not mdb.is_open

        # Check that the database file was created
        assert db_path.exists()
    
    def test_create_existing_model_raises_error(self, sirius_db: Path):
        """Test that creating an existing model raises FileExistsError."""
        with pytest.raises(FileExistsError):
            ModelDatabase.create(sirius_db)


class TestModelDatabase:
    """Tests for the ModelDatabase class."""

    @pytest.fixture
    def model_db(self, class_sirius_db: Path):
        """Fixture providing a test ModelDatabase instance."""
        db = ModelDatabase(class_sirius_db)
        yield db
        db.close()
    
    def test_is_open(self, model_db):
        """Test is_open property."""
        assert model_db.is_open
    
    def test_tables_property(self, model_db):
        """Test tables property returns a TableCollection."""
        assert isinstance(model_db.tables, TableCollection)
    
    def test_unit_system(self, model_db):
        """Test unit_system property."""
        assert model_db.unit_system == "MU_CS_SI"
    
    def test_version(self, model_db):
        """Test version property."""
        assert model_db.version == "2025.0.0"
    
    def test_active_scenario(self, model_db):
        """Test active_scenario property."""
        assert model_db.active_scenario == "Base"

    def test_scenarios(self, model_db):
        assert model_db.scenarios == ["Base", "sub_scenario"]
    
    def test_set_active_scenario(self, model_db):
        """Test set_active_scenario method."""
        model_db.active_scenario = "sub_scenario"
        assert model_db.active_scenario == "sub_scenario"
        model_db.active_scenario = "Base"
        assert model_db.active_scenario == "Base"
        with pytest.raises(ValueError):
            model_db.active_scenario = "this_does_not_exist"
        assert model_db.active_scenario == "Base"
    
    
    def test_active_model(self, model_db):
        """Test active_model property."""
        assert model_db.active_model == "CS_MIKE1D"
    
    
    def test_close(self, model_db):
        """Test close method."""
        model_db.close()
        assert not model_db.is_open
