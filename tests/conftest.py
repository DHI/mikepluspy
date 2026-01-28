import faulthandler
import pythonnet
import pytest
import shutil
import tempfile
import uuid
from pathlib import Path

faulthandler.enable()

"""
Test Database Fixture System
===========================

This module provides both session-scoped, module-scoped, class-scoped and function-scoped database fixtures:

1. Session-level fixtures (`session_*_db`):
   - Created once per test session (all tests run)
   - Suitable for tests that only read from the database or don't require isolation
   - Changes to these databases will persist across tests in the same session
   - Use these for better performance when test isolation isn't needed

2. Module-level fixtures (`module_*_db`):
   - Created once per test module
   - Suitable for tests that only read from the database or don't require isolation
   - Changes to these databases will persist across tests in the same module
   - Use these for better performance when test isolation isn't needed

3. Class-level fixtures (`class_*_db`):
   - Created once per test class
   - Suitable for tests that only read from the database or don't require isolation
   - Changes to these databases will persist across tests in the same class
   - Use these for better performance when test isolation isn't needed

4. Function-level fixtures (e.g., `sirius_db`, `epanet_demo_db`):
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

# Use module fixture for read-only operations (faster)
def test_read_only_example(module_sirius_db):
    # This test only reads from the database, so isolation isn't needed
    ...

# Use class fixture for read-only operations (faster)
def test_read_only_example(class_sirius_db):
    # This test only reads from the database, so isolation isn't needed
    ...

# Use function fixture when modifying the database (isolated)
def test_write_example(sirius_db):
    # This test modifies the database, so it needs isolation
    ...
```

The utility functions in this module make it easy to extend with other scopes if needed.
"""

TEST_DATA_DIR = Path(__file__).resolve().parent / "testdata"
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


def copy_database_folder(source_db_path, target_dir) -> Path:
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


def create_test_specific_db_copy(source_db_path, tmp_path, prefix) -> Path:
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
def session_sirius_db(session_temp_dir) -> Path:
    """Copy the Sirius database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "Sirius"
    return copy_database_folder(SIRIUS_DB, target_dir)


@pytest.fixture(scope="session")
def session_epanet_demo_db(session_temp_dir) -> Path:
    """Copy the Epanet_Demo database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "Epanet_Demo"
    return copy_database_folder(EPANET_DEMO_DB, target_dir)


@pytest.fixture(scope="session")
def session_swmm_db(session_temp_dir) -> Path:
    """Copy the SWMM database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "SWMM"
    return copy_database_folder(SWMM_DB, target_dir)


@pytest.fixture(scope="session")
def session_flood_db(session_temp_dir) -> Path:
    """Copy the 2D Blue Beach database folder once per test session."""
    target_dir = session_temp_dir / "session" / "Db" / "2D Blue Beach"
    return copy_database_folder(FLOOD_DB, target_dir)


@pytest.fixture(scope="session")
def session_repair_tool_db(session_temp_dir) -> Path:
    """Copy the RepairTestCase database folder once per test session."""
    target_dir = session_temp_dir / "session" / "repairToolData"
    return copy_database_folder(REPAIR_TOOL_DB, target_dir)


@pytest.fixture(scope="session")
def session_interpolate_db(session_temp_dir) -> Path:
    """Copy the interpolate database folder once per test session."""
    target_dir = session_temp_dir / "session" / "interpolate"
    return copy_database_folder(INTERPOLATE_DB, target_dir)


@pytest.fixture(scope="session")
def session_connection_repair_db(session_temp_dir) -> Path:
    """Copy the connection repair database folder once per test session."""
    target_dir = session_temp_dir / "session" / "connectionRepair"
    return copy_database_folder(CONNECTION_REPAIR_DB, target_dir)


@pytest.fixture(scope="session")
def session_catch_slope_len_db(session_temp_dir) -> Path:
    """Copy the catch slope length database folder once per test session."""
    target_dir = session_temp_dir / "session" / "catchSlopeLen"
    return copy_database_folder(CATCH_SLOPE_LEN_DB, target_dir)


@pytest.fixture(scope="session")
def session_import_db(session_temp_dir) -> Path:
    """Copy the import database folder once per test session."""
    target_dir = session_temp_dir / "session" / "import"
    return copy_database_folder(IMPORT_DB, target_dir)


@pytest.fixture(scope="module")
def module_temp_dir():
    """Create a temporary directory for test files that persists for the entire test module."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)


@pytest.fixture(scope="module")
def module_sirius_db(module_temp_dir) -> Path:
    """Copy the Sirius database folder once per test module."""
    target_dir = module_temp_dir / "module" / "Db" / "Sirius"
    return copy_database_folder(SIRIUS_DB, target_dir)


@pytest.fixture(scope="module")
def module_epanet_demo_db(module_temp_dir) -> Path:
    """Copy the Epanet_Demo database folder once per test module."""
    target_dir = module_temp_dir / "module" / "Db" / "Epanet_Demo"
    return copy_database_folder(EPANET_DEMO_DB, target_dir)


@pytest.fixture(scope="module")
def module_swmm_db(module_temp_dir) -> Path:
    """Copy the SWMM database folder once per test module."""
    target_dir = module_temp_dir / "module" / "Db" / "SWMM"
    return copy_database_folder(SWMM_DB, target_dir)


@pytest.fixture(scope="module")
def module_flood_db(module_temp_dir) -> Path:
    """Copy the 2D Blue Beach database folder once per test module."""
    target_dir = module_temp_dir / "module" / "Db" / "2D Blue Beach"
    return copy_database_folder(FLOOD_DB, target_dir)


@pytest.fixture(scope="module")
def module_repair_tool_db(module_temp_dir) -> Path:
    """Copy the RepairTestCase database folder once per test module."""
    target_dir = module_temp_dir / "module" / "repairToolData"
    return copy_database_folder(REPAIR_TOOL_DB, target_dir)


@pytest.fixture(scope="module")
def module_interpolate_db(module_temp_dir) -> Path:
    """Copy the interpolate database folder once per test module."""
    target_dir = module_temp_dir / "module" / "interpolate"
    return copy_database_folder(INTERPOLATE_DB, target_dir)


@pytest.fixture(scope="module")
def module_connection_repair_db(module_temp_dir) -> Path:
    """Copy the connection repair database folder once per test module."""
    target_dir = module_temp_dir / "module" / "connectionRepair"
    return copy_database_folder(CONNECTION_REPAIR_DB, target_dir)


@pytest.fixture(scope="module")
def module_catch_slope_len_db(module_temp_dir) -> Path:
    """Copy the catch slope length database folder once per test module."""
    target_dir = module_temp_dir / "module" / "catchSlopeLen"
    return copy_database_folder(CATCH_SLOPE_LEN_DB, target_dir)


@pytest.fixture(scope="module")
def module_import_db(module_temp_dir) -> Path:
    """Copy the import database folder once per test module."""
    target_dir = module_temp_dir / "module" / "import"
    return copy_database_folder(IMPORT_DB, target_dir)


@pytest.fixture(scope="class")
def class_temp_dir():
    """Create a temporary directory for test files that persists for the entire test class."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)


@pytest.fixture(scope="class")
def class_sirius_db(class_temp_dir) -> Path:
    """Copy the Sirius database folder once per test class."""
    target_dir = class_temp_dir / "class" / "Db" / "Sirius"
    return copy_database_folder(SIRIUS_DB, target_dir)


@pytest.fixture(scope="class")
def class_epanet_demo_db(class_temp_dir) -> Path:
    """Copy the Epanet_Demo database folder once per test class."""
    target_dir = class_temp_dir / "class" / "Db" / "Epanet_Demo"
    return copy_database_folder(EPANET_DEMO_DB, target_dir)


@pytest.fixture(scope="class")
def class_swmm_db(class_temp_dir) -> Path:
    """Copy the SWMM database folder once per test class."""
    target_dir = class_temp_dir / "class" / "Db" / "SWMM"
    return copy_database_folder(SWMM_DB, target_dir)


@pytest.fixture(scope="class")
def class_flood_db(class_temp_dir) -> Path:
    """Copy the 2D Blue Beach database folder once per test class."""
    target_dir = class_temp_dir / "class" / "Db" / "2D Blue Beach"
    return copy_database_folder(FLOOD_DB, target_dir)


@pytest.fixture(scope="class")
def class_repair_tool_db(class_temp_dir) -> Path:
    """Copy the RepairTestCase database folder once per test class."""
    target_dir = class_temp_dir / "class" / "repairToolData"
    return copy_database_folder(REPAIR_TOOL_DB, target_dir)


@pytest.fixture(scope="class")
def class_interpolate_db(class_temp_dir) -> Path:
    """Copy the interpolate database folder once per test class."""
    target_dir = class_temp_dir / "class" / "interpolate"
    return copy_database_folder(INTERPOLATE_DB, target_dir)


@pytest.fixture(scope="class")
def class_connection_repair_db(class_temp_dir) -> Path:
    """Copy the connection repair database folder once per test class."""
    target_dir = class_temp_dir / "class" / "connectionRepair"
    return copy_database_folder(CONNECTION_REPAIR_DB, target_dir)


@pytest.fixture(scope="class")
def class_catch_slope_len_db(class_temp_dir) -> Path:
    """Copy the catch slope length database folder once per test class."""
    target_dir = class_temp_dir / "class" / "catchSlopeLen"
    return copy_database_folder(CATCH_SLOPE_LEN_DB, target_dir)


@pytest.fixture(scope="class")
def class_import_db(class_temp_dir) -> Path:
    """Copy the import database folder once per test class."""
    target_dir = class_temp_dir / "class" / "import"
    return copy_database_folder(IMPORT_DB, target_dir)


@pytest.fixture(scope="function")
def sirius_db(tmp_path) -> Path:
    """Create a test-specific copy of the Sirius database folder."""
    return create_test_specific_db_copy(SIRIUS_DB, tmp_path, "test_sirius")


@pytest.fixture(scope="function")
def epanet_demo_db(tmp_path) -> Path:
    """Create a test-specific copy of the Epanet_Demo database folder."""
    return create_test_specific_db_copy(EPANET_DEMO_DB, tmp_path, "test_epanet_demo")


@pytest.fixture(scope="function")
def swmm_db(tmp_path) -> Path:
    """Create a test-specific copy of the SWMM database folder."""
    return create_test_specific_db_copy(SWMM_DB, tmp_path, "test_swmm")


@pytest.fixture(scope="function")
def flood_db(tmp_path) -> Path:
    """Create a test-specific copy of the 2D Blue Beach database folder."""
    return create_test_specific_db_copy(FLOOD_DB, tmp_path, "test_flood")


@pytest.fixture(scope="function")
def repair_tool_db(tmp_path) -> Path:
    """Create a test-specific copy of the RepairTestCase database folder."""
    return create_test_specific_db_copy(REPAIR_TOOL_DB, tmp_path, "test_repair_tool")


@pytest.fixture(scope="function")
def interpolate_db(tmp_path) -> Path:
    """Create a test-specific copy of the interpolate database folder."""
    return create_test_specific_db_copy(INTERPOLATE_DB, tmp_path, "test_interpolate")


@pytest.fixture(scope="function")
def connection_repair_db(tmp_path) -> Path:
    """Create a test-specific copy of the connection repair database folder."""
    return create_test_specific_db_copy(
        CONNECTION_REPAIR_DB, tmp_path, "test_connection_repair"
    )


@pytest.fixture(scope="function")
def catch_slope_len_db(tmp_path) -> Path:
    """Create a test-specific copy of the catch slope length database folder."""
    return create_test_specific_db_copy(
        CATCH_SLOPE_LEN_DB, tmp_path, "test_catch_slope_len"
    )


@pytest.fixture(scope="function")
def import_db(tmp_path) -> Path:
    """Create a test-specific copy of the import database folder."""
    return create_test_specific_db_copy(IMPORT_DB, tmp_path, "test_import")
