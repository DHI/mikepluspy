"""Tests for the MikeEngine class."""

from __future__ import annotations

import pytest
import os
from pathlib import Path
from mikeplus import Database
from mikeplus.engines.mike_engine import MikeEngine


def test_mike_engine_run_1d(sirius_db):
    """Test running a MIKE 1D simulation."""
    db = Database(sirius_db)
    engine = MikeEngine(db)
    
    # Run the simulation
    result_files = engine.run_1d()
    
    # Verify engine returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)
    
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
    
    db.close()


def test_mike_engine_run_epanet(sirius_db):
    """Test running an EPANET simulation."""
    db = Database(sirius_db)
    engine = MikeEngine(db)
    
    # Run the simulation
    result_files = engine.run_epanet()
    
    # Verify engine returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)
    
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
    
    db.close()


def test_mike_engine_run_swmm(sirius_db):
    """Test running a SWMM simulation."""
    db = Database(sirius_db)
    engine = MikeEngine(db)
    
    # Run the simulation
    result_files = engine.run_swmm()
    
    # Verify engine returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)
    
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
    
    db.close()


def test_mike_engine_run_flood(sirius_db):
    """Test running a Flood simulation."""
    db = Database(sirius_db)
    engine = MikeEngine(db)
    
    # Run the simulation
    result_files = engine.run_flood()
    
    # Verify engine returns a list of Path objects
    assert isinstance(result_files, list)
    assert all(isinstance(file, Path) for file in result_files)
    
    # Verify result files exist
    for file in result_files:
        assert file.exists(), f"Result file {file} does not exist"
    
    db.close()