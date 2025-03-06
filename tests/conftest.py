import pytest
import shutil
import tempfile
import uuid
from pathlib import Path


"""
Test Database Fixture System
===========================

This module provides both session-scoped and function-scoped database fixtures:

1. Session-level fixtures (`session_*_db`):
   - Created once per test session (all tests run)
   - Suitable for tests that only read from the database or don't require isolation
   - Changes to these databases will persist across tests in the same session
   - Use these for better performance when test isolation isn't needed

2. Function-level fixtures (e.g., `sirius_db`, `epanet_demo_db`):
   - Created freshly for each test function
   - Provide a clean, isolated database for each test
   - Changes made in one test won't affect other tests
   - Use these when your test modifies the database

Usage examples:
--------------
```python
# Use session fixture for read-only operations (faster)
def test_read_only_example(session_sirius_db):
    # This test only reads from the database, so isolation isn't needed
    ...

# Use function fixture when modifying the database (isolated)
def test_write_example(sirius_db):
    # This test modifies the database, so it needs isolation
    ...
```

The utility functions in this module make it easy to extend with other scopes if needed.
"""

TEST_DATA_DIR = Path("tests") / "testdata"
DB_DIR = TEST_DATA_DIR / "Db"

SIRIUS_DB = DB_DIR / "Sirius" / "Sirius.sqlite"
EPANET_DEMO_DB = DB_DIR / "Epanet_Demo" / "Epanet_Demo.sqlite"
SWMM_DB = DB_DIR / "SWMM" / "Simple_Network.sqlite"
FLOOD_DB = DB_DIR / "2D Blue Beach" / "100y_combined.sqlite"
REPAIR_TOOL_DB = TEST_DATA_DIR / "repairToolData" / "RepairTestCase.sqlite"
INTERPOLATE_DB = TEST_DATA_DIR / "interpolate" / "inter.sqlite"
CONNECTION_REPAIR_DB = TEST_DATA_DIR / "connectionRepair" / "repair.sqlite"
CATCH_SLOPE_LEN_DB = TEST_DATA_DIR / "catchSlopeLen" / "catch.sqlite"
IMPORT_DB = TEST_DATA_DIR / "import" / "import.sqlite"


def copy_database_folder(source_db_path, target_dir):
    """
    Copy a database folder to a target directory recursively.
    
    Args:
        source_db_path (Path): Path to the source database file
        target_dir (Path): Target directory to copy the database folder to
        
    Returns:
        Path: Path to the copied database file
    """
    source_dir = source_db_path.parent
    
    if not target_dir.exists():
        shutil.copytree(source_dir, target_dir)
    
    return target_dir / source_db_path.name


def create_test_specific_db_copy(source_db_path, tmp_path, prefix):
    """
    Create a test-specific copy of a database folder.
    
    Args:
        source_db_path (Path): Path to the source database file
        tmp_path (Path): Temporary path for test
        prefix (str): Prefix for the directory name
        
    Returns:
        Path: Path to the test-specific database file
    """
    test_db_dir = tmp_path / f"{prefix}_{uuid.uuid4()}"
    source_dir = source_db_path.parent
    shutil.copytree(source_dir, test_db_dir)
    return test_db_dir / source_db_path.name


@pytest.fixture(scope="session")
def session_temp_dir():
    """Create a temporary directory for test files that persists for the entire test session."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)


@pytest.fixture(scope="session")
def session_sirius_db(session_temp_dir):
    """Copy the Sirius database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "Sirius"
    return copy_database_folder(SIRIUS_DB, target_dir)


@pytest.fixture(scope="session")
def session_epanet_demo_db(session_temp_dir):
    """Copy the Epanet_Demo database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "Epanet_Demo"
    return copy_database_folder(EPANET_DEMO_DB, target_dir)


@pytest.fixture(scope="session")
def session_swmm_db(session_temp_dir):
    """Copy the SWMM database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "SWMM"
    return copy_database_folder(SWMM_DB, target_dir)


@pytest.fixture(scope="session")
def session_flood_db(session_temp_dir):
    """Copy the 2D Blue Beach database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "2D Blue Beach"
    return copy_database_folder(FLOOD_DB, target_dir)


@pytest.fixture(scope="session")
def session_repair_tool_db(session_temp_dir):
    """Copy the RepairTestCase database folder once per test session."""
    target_dir = session_temp_dir / "session" / "repairToolData"
    return copy_database_folder(REPAIR_TOOL_DB, target_dir)


@pytest.fixture(scope="session")
def session_interpolate_db(session_temp_dir):
    """Copy the interpolate database folder once per test session."""
    target_dir = session_temp_dir / "session" / "interpolate"
    return copy_database_folder(INTERPOLATE_DB, target_dir)


@pytest.fixture(scope="session")
def session_connection_repair_db(session_temp_dir):
    """Copy the connection repair database folder once per test session."""
    target_dir = session_temp_dir / "session" / "connectionRepair"
    return copy_database_folder(CONNECTION_REPAIR_DB, target_dir)


@pytest.fixture(scope="session")
def session_catch_slope_len_db(session_temp_dir):
    """Copy the catch slope length database folder once per test session."""
    target_dir = session_temp_dir / "session" / "catchSlopeLen"
    return copy_database_folder(CATCH_SLOPE_LEN_DB, target_dir)


@pytest.fixture(scope="session")
def session_import_db(session_temp_dir):
    """Copy the import database folder once per test session."""
    target_dir = session_temp_dir / "session" / "import"
    return copy_database_folder(IMPORT_DB, target_dir)


@pytest.fixture(scope="function")
def sirius_db(tmp_path):
    """Create a test-specific copy of the Sirius database folder."""
    return create_test_specific_db_copy(SIRIUS_DB, tmp_path, "test_sirius")


@pytest.fixture(scope="function")
def epanet_demo_db(tmp_path):
    """Create a test-specific copy of the Epanet_Demo database folder."""
    return create_test_specific_db_copy(EPANET_DEMO_DB, tmp_path, "test_epanet_demo")


@pytest.fixture(scope="function")
def swmm_db(tmp_path):
    """Create a test-specific copy of the SWMM database folder."""
    return create_test_specific_db_copy(SWMM_DB, tmp_path, "test_swmm")


@pytest.fixture(scope="function")
def flood_db(tmp_path):
    """Create a test-specific copy of the 2D Blue Beach database folder."""
    return create_test_specific_db_copy(FLOOD_DB, tmp_path, "test_flood")


@pytest.fixture(scope="function")
def repair_tool_db(tmp_path):
    """Create a test-specific copy of the RepairTestCase database folder."""
    return create_test_specific_db_copy(REPAIR_TOOL_DB, tmp_path, "test_repair_tool")


@pytest.fixture(scope="function")
def interpolate_db(tmp_path):
    """Create a test-specific copy of the interpolate database folder."""
    return create_test_specific_db_copy(INTERPOLATE_DB, tmp_path, "test_interpolate")


@pytest.fixture(scope="function")
def connection_repair_db(tmp_path):
    """Create a test-specific copy of the connection repair database folder."""
    return create_test_specific_db_copy(CONNECTION_REPAIR_DB, tmp_path, "test_connection_repair")


@pytest.fixture(scope="function")
def catch_slope_len_db(tmp_path):
    """Create a test-specific copy of the catch slope length database folder."""
    return create_test_specific_db_copy(CATCH_SLOPE_LEN_DB, tmp_path, "test_catch_slope_len")


@pytest.fixture(scope="function")
def import_db(tmp_path):
    """Create a test-specific copy of the import database folder."""
    return create_test_specific_db_copy(IMPORT_DB, tmp_path, "test_import")
