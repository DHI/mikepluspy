import os
from mikeplus import DataTableAccess
from mikeplus.engines.engine1d import Egnine1D
from mikeplus.engines.epanet import EPANET
from mikeplus.engines.swmm import SWMM


def test_mike1d_engine():
    res_1d_file = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius_RR_and_HDBaseDefault_Network_HD.res1d")
    if os.path.exists(res_1d_file):
        os.remove(res_1d_file)
    dbFile = os.path.join("tests", "testdata", "Db", "Sirius", "Sirius.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    engine = Egnine1D(data_access.datatables)
    engine.run()
    data_access.close_database()
    assert os.path.exists(res_1d_file)


def test_epanet_engine():
    dbFile = os.path.join("tests", "testdata", "Db", "Average DayDemand GPM", "AverageDayDemand_GPM.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    engine = EPANET(data_access.datatables)
    result_file = engine.result_file
    if os.path.exists(result_file):
        os.remove(result_file)
    engine.run_engine_epanet()
    data_access.close_database()
    assert os.path.exists(result_file)


def test_swmm_engine():
    dbFile = os.path.join("tests", "testdata", "Db", "SWMM_Sirius", "Sirius_SWMM.sqlite")
    data_access = DataTableAccess(dbFile)
    data_access.open_database()
    engine = SWMM(data_access.datatables)
    result_file = engine.result_file
    if os.path.exists(result_file):
        os.remove(result_file)
    engine.run()
    data_access.close_database()
    assert os.path.exists(result_file)
