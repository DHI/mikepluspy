"""Tests for the MikeEngine class."""

from __future__ import annotations

from pathlib import Path
from mikeplus import Database
from mikeplus.simulation_runner import SimulationRunner


def test_mike_engine_run_1d(sirius_db):
    """Test running a MIKE 1D simulation."""
    db = Database(sirius_db)
    
    # Run the simulation
    result_files = db.run()
    
    # Verify runner returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)
    
    # Verify number and type of result files
    assert len(result_files) > 0, "No result files found for MIKE 1D simulation"
    assert any(file.suffix == ".res1d" for file in result_files), \
        "Expected at least one .res1d file for MIKE 1D simulation"

    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
        file.unlink(missing_ok=True)
    
    db.close()

def test_mike_engine_run_flood(flood_db):
    """Test running a Flood simulation."""
    db = Database(flood_db)
    
    # Run the simulation
    result_files = db.run()
    
    # Verify runner returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)

    # Verify number and type of result files
    assert len(result_files) > 0, "No result files found for Flood simulation"
    suffixes = [".res1d", ".dfsu"]
    assert all(any(file.suffix == s for file in result_files) for s in suffixes), \
        "Expected at least one .res1d and one .dfsu file for Flood simulation"
        
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
        file.unlink(missing_ok=True)
    
    db.close()

def test_mike_engine_run_swmm(swmm_db):
    """Test running a SWMM simulation."""
    db = Database(swmm_db)
    
    # Run the simulation
    result_files = db.run()
    
    # Verify runner returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)

    # Verify number and type of result files
    # SWMM typically produces .out and .rpt files.
    assert len(result_files) > 0, "Expected at least 1 result file for SWMM (e.g., .out)"
    expected_extensions = {".out"}
    actual_extensions = {file.suffix for file in result_files}
    assert expected_extensions.issubset(actual_extensions), \
        f"Expected SWMM result extensions {expected_extensions}, got {actual_extensions}"
    
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
        file.unlink(missing_ok=True)
    
    db.close()


def test_mike_engine_run_epanet(epanet_demo_db):
    """Test running an EPANET simulation."""
    db = Database(epanet_demo_db)
    
    # Run the simulation
    result_files = db.run()
    
    # Verify runner returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)

    # Verify number and type of result files
    assert len(result_files) > 0, "Expected at least 1 result file for EPANET (e.g., .res)"
    expected_extensions = {".res"}
    actual_extensions = {file.suffix for file in result_files}
    assert expected_extensions.issubset(actual_extensions), \
        f"Expected EPANET result extensions {expected_extensions}, got {actual_extensions}"
        
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
        file.unlink(missing_ok=True)
    
    db.close()
    
