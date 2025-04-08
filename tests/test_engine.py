from __future__ import annotations

import pytest
import os
from mikeplus import DataTableAccess
from mikeplus.engines.engine1d import Engine1D
from mikeplus.engines.epanet import EPANET
from mikeplus.engines.swmm import SWMM
from mikeplus.engines.flood_engine import FloodEngine


@pytest.mark.slow(reason="Test run slow because of the license check.")
def test_mike1d_engine(sirius_db):
    # Extract the directory from sirius_db to construct the result path
    db_dir = os.path.dirname(sirius_db)
    res_1d_file = os.path.join(db_dir, "Sirius_1_DEMOBaseDefault_Network_HD.res1d")

    if os.path.exists(res_1d_file):
        os.remove(res_1d_file)

    data_access = DataTableAccess(sirius_db)
    data_access.open_database()
    engine = Engine1D(data_access.datatables)
    engine.run()
    data_access.close_database()
    assert os.path.exists(res_1d_file)


@pytest.mark.slow(reason="Test run slow because of the license check.")
def test_epanet_engine(epanet_demo_db):
    data_access = DataTableAccess(epanet_demo_db)
    data_access.open_database()
    engine = EPANET(data_access.datatables)
    result_file = engine.result_file

    if os.path.exists(result_file):
        os.remove(result_file)

    current_dir = os.getcwd()
    engine.run_engine_epanet()
    data_access.close_database()
    os.chdir(current_dir)
    assert os.path.exists(result_file)


@pytest.mark.slow(reason="Test run slow because of the license check.")
def test_swmm_engine(swmm_db):
    data_access = DataTableAccess(swmm_db)
    data_access.open_database()
    engine = SWMM(data_access.datatables)
    result_file = engine.result_file

    if os.path.exists(result_file):
        os.remove(result_file)

    current_dir = os.getcwd()
    engine.run()
    data_access.close_database()
    os.chdir(current_dir)
    assert os.path.exists(result_file)


@pytest.mark.license_required
def test_flood_engine(flood_db):
    data_access = DataTableAccess(flood_db)
    data_access.open_database()
    engine = FloodEngine(data_access.datatables)
    result_files = engine.result_files

    if result_files is not None:
        for file in result_files:
            if os.path.exists(file):
                os.remove(file)

    engine.run()
    data_access.close_database()
    assert result_files is not None
    for file in result_files:
        assert os.path.exists(file)
