from __future__ import annotations

import pytest
import os
from mikeplus import Database
from mikeplus.engines.engine1d import Engine1D
from mikeplus.engines.epanet import EPANET
from mikeplus.engines.swmm import SWMM
from mikeplus.engines.flood_engine import FloodEngine


@pytest.mark.slow(reason="Test run slow because of the license check.")
def test_mike1d_engine(sirius_db):
    db = Database(sirius_db)
    engine = Engine1D(db)
    
    result_files = engine.get_result_files()

    for res_file in result_files:
        if os.path.exists(res_file):
            os.remove(res_file)
    
    engine.run()
    
    for res_file in result_files:
        assert os.path.exists(res_file)
        
    db.close()


@pytest.mark.slow(reason="Test run slow because of the license check.")
def test_epanet_engine(epanet_demo_db):
    db = Database(epanet_demo_db)
    engine = EPANET(db)
    result_file = engine.result_file

    if os.path.exists(result_file):
        os.remove(result_file)

    current_dir = os.getcwd()
    engine.run_engine_epanet()
    db.close()
    os.chdir(current_dir)
    assert os.path.exists(result_file)


@pytest.mark.slow(reason="Test run slow because of the license check.")
def test_swmm_engine(swmm_db):
    db = Database(swmm_db)
    engine = SWMM(db)
    result_file = engine.result_file

    if os.path.exists(result_file):
        os.remove(result_file)

    current_dir = os.getcwd()
    engine.run()
    db.close()
    os.chdir(current_dir)
    assert os.path.exists(result_file)


# TODO: Fix this - something not so great going on
@pytest.mark.license_required
@pytest.mark.xfail(reason="Passes locally on re-run, but not on full run or CI")
def test_flood_engine(flood_db):
    db = Database(flood_db)
    engine = FloodEngine(db)
    result_files = engine.result_files

    if result_files is not None:
        for file in result_files:
            if os.path.exists(file):
                os.remove(file)

    engine.run()
    db.close()
    assert result_files is not None
    for file in result_files:
        assert os.path.exists(file)
