"""
Tests for the database module functionality.
"""

from __future__ import annotations

import pytest
from pathlib import Path

from mikeplus.database import Database
from mikeplus.tables.auto_generated import TableCollection


class TestDatabaseOpen:
    """Tests for the Database opening functionality."""

    def test_open_existing_model(self, session_sirius_db: Path):
        """Test opening an existing model database."""
        # Open via constructor
        db = Database(session_sirius_db)
        assert isinstance(db, Database)
        assert db.is_open
        assert db.db_path == session_sirius_db
        assert db.mupp_path == session_sirius_db.with_suffix(".mupp")
        db.close()
        assert not db.is_open

        # Open via constructor (without auto-open)
        db2 = Database(session_sirius_db, auto_open=False)
        assert isinstance(db2, Database)
        assert not db2.is_open
        assert db2.db_path == session_sirius_db
        assert db2.mupp_path == session_sirius_db.with_suffix(".mupp")
        db2.close()
        assert not db2.is_open

        # Open via context manager
        with Database(session_sirius_db) as db3:
            assert db3.is_open
            assert db3.db_path == session_sirius_db
            assert db3.mupp_path == session_sirius_db.with_suffix(".mupp")

        assert not db3.is_open

    def test_open_nonexistent_model_raises_error(self):
        """Test that opening a non-existent model raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            Database(Path("/path/to/nonexistent/model.mupp"))

        with pytest.raises(FileNotFoundError):
            Database(Path("/path/to/nonexistent/model.sqlite"))


class TestDatabaseCreate:
    """Tests for the Database creation functionality."""

    def test_create_new_model(self, tmp_path: Path):
        """Test creating a new model database."""
        db_path = tmp_path / "model.sqlite"

        # Create model database
        db = Database.create(db_path)
        assert isinstance(db, Database)
        assert db.is_open
        assert db.db_path == db_path
        db.close()
        assert not db.is_open

        # Check that the database file was created
        assert db_path.exists()

    def test_create_existing_model_raises_error(self, sirius_db: Path):
        """Test that creating an existing model raises FileExistsError."""
        with pytest.raises(FileExistsError):
            Database.create(sirius_db)

    def test_import_epanet(self, tmp_path: Path):
        """Test importing from an EPANET .inp file."""
        db_path = tmp_path / "model.sqlite"
        inp_path = Path("tests/testdata/Db/Epanet_Demo/Epanet_Demo.inp")

        # Create model database and import from EPANET
        db = Database.create(db_path)
        db.import_from_epanet(inp_path)

        # Check that some expected tables exist
        df = db.tables.mw_Pipe.to_dataframe()
        assert not df.empty

        db.close()
        assert not db.is_open


class TestDatabase:
    """Tests for the Database class."""

    @pytest.fixture
    def db(self, class_sirius_db: Path):
        """Fixture providing a test Database instance."""
        db = Database(class_sirius_db)
        yield db
        db.close()

    def test_is_open(self, db):
        """Test is_open property."""
        assert db.is_open

    def test_tables_property(self, db):
        """Test tables property returns a TableCollection."""
        assert isinstance(db.tables, TableCollection)

    def test_unit_system(self, db):
        """Test unit_system property."""
        assert db.unit_system == "MU_CS_SI"

    def test_version(self, db):
        """Test version property."""
        assert isinstance(db.version, str)
        parts = db.version.split(".")
        assert len(parts) == 3
        assert all(part.isdigit() for part in parts)
        assert int(parts[0]) >= 2025

    def test_active_scenario(self, db):
        """Test active_scenario property."""
        assert db.active_scenario.name == "Base"

    def test_scenarios(self, db):
        assert [s.name for s in db.scenarios] == ["Base", "sub_scenario"]

    def test_set_active_scenario(self, db: Database):
        """Test set_active_scenario method."""
        db.active_scenario = db.scenarios.by_name("sub_scenario")
        assert db.active_scenario.name == "sub_scenario"
        db.active_scenario = db.scenarios.by_name("Base")
        assert db.active_scenario.name == "Base"
        with pytest.raises(ValueError):
            db.active_scenario = db.scenarios.by_name("this_does_not_exist")
        assert db.active_scenario.name == "Base"

    def test_active_model(self, db):
        """Test active_model property."""
        assert db.active_model == "CS_MIKE1D"

    def test_projection_string(self, db):
        """Test projection_string property."""
        projection = db.projection_string
        expected = (
            r"""PROJCS["ETRS89 / UTM zone 32N","""
            r"""GEOGCS["ETRS89",DATUM["European_Terrestrial_Reference_System_1989","""
            r"""SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],"""
            r"""TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6258"]],"""
            r"""PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree","""
            r"""0.0174532925199433,AUTHORITY["EPSG","9122"]],"""
            r"""AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4258"]],"""
            r"""PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",0],"""
            r"""PARAMETER["central_meridian",9],PARAMETER["scale_factor",0.9996],"""
            r"""PARAMETER["false_easting",500000],PARAMETER["false_northing",0],"""
            r"""UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Easting",EAST],"""
            r"""AXIS["Northing",NORTH],AUTHORITY["EPSG","25832"]]"""
        )
        assert projection == expected

    def test_srid(self, db):
        """Test srid property."""
        srid = db.srid
        assert srid == 25832

    def test_active_simulation(self, db):
        """Test active_simulation property."""
        simulation = db.active_simulation
        assert simulation == "Sirius_1_DEMO"

    def test_close(self, db):
        """Test close method."""
        db.close()
        assert not db.is_open

    def test_top_level_imports(self, tmp_path: Path):
        """Test that top-level imports work correctly."""
        from mikeplus import Database
        from mikeplus import open
        from mikeplus import create

        new_db_path = tmp_path / "new_test_db.sqlite"
        db = create(new_db_path)
        assert db.is_open
        assert new_db_path.exists()
        db.close()

        db = Database(new_db_path)
        assert db.is_open
        db.close()

        db = open(new_db_path)
        assert db.is_open
        db.close()
