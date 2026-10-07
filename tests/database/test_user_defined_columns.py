"""Tests for managing user-defined columns through ``table.columns``."""

from __future__ import annotations

import pytest

from mikeplus.database import Database

EXISTING_AD_COLUMNS = [
    "AttachPol2PipeSediNo",
    "PolSediRatioPipe",
    "DissolvedPctPipe",
    "FineSediPctPipe",
    "CoarseSediPctPipe",
]


@pytest.fixture
def db(catch_slope_len_db):
    db = Database(catch_slope_len_db)
    yield db
    db.close()


@pytest.fixture(scope="module")
def read_only_db(module_catch_slope_len_db):
    db = Database(module_catch_slope_len_db)
    yield db
    db.close()


def _records(db, table_name, field_name):
    df = db.tables.m_UserDefinedColumn.select(["TableName", "FieldName"]).to_dataframe()
    return df[(df.TableName == table_name) & (df.FieldName == field_name)].index.tolist()


def test_user_defined_lists_columns_already_in_database(read_only_db):
    components = read_only_db.tables.msm_ADComponent
    assert components.columns.user_defined == EXISTING_AD_COLUMNS
    assert components.columns.detached == []
    assert read_only_db.tables.msm_Link.columns.user_defined == []


def test_add_user_defined_creates_column_visible_immediately(db):
    pipes = db.tables.msm_Link
    assert "my_col" not in pipes.columns

    muid = pipes.columns.add_user_defined("my_col", "string", header="My col")

    assert muid.startswith("udf_")
    assert pipes.columns.user_defined == ["my_col"]
    assert "MY_COL" in pipes.columns
    assert pipes.columns["MY_COL"] == "my_col"
    assert "my_col" in list(pipes.columns)
    assert pipes.columns.detached == []


def test_add_user_defined_twice_keeps_one_record(db):
    pipes = db.tables.msm_Link

    first = pipes.columns.add_user_defined("my_col", "string")
    second = pipes.columns.add_user_defined("MY_COL", "string")
    third = pipes.columns.add_user_defined("my_col")

    assert first == second == third
    assert _records(db, "msm_Link", "my_col") == [first]
    assert pipes.columns.user_defined == ["my_col"]


def test_add_user_defined_with_different_type_raises(db):
    pipes = db.tables.msm_Link
    pipes.columns.add_user_defined("my_col", "string")

    with pytest.raises(ValueError, match="string"):
        pipes.columns.add_user_defined("my_col", "integer")


def test_add_user_defined_on_standard_column_raises(read_only_db):
    with pytest.raises(ValueError, match="standard"):
        read_only_db.tables.msm_Link.columns.add_user_defined("Diameter")


def test_add_user_defined_new_column_without_type_raises(db):
    pipes = db.tables.msm_Link

    with pytest.raises(ValueError, match="data_type"):
        pipes.columns.add_user_defined("my_col")

    assert "my_col" not in pipes.columns


def test_remove_user_defined_detaches_column(db):
    components = db.tables.msm_ADComponent
    assert components.columns.detached == []

    muid = components.columns.remove_user_defined("finesedipctpipe")

    assert muid == "udf_4"
    assert "FineSediPctPipe" not in components.columns
    assert components.columns.user_defined == [
        c for c in EXISTING_AD_COLUMNS if c != "FineSediPctPipe"
    ]
    assert components.columns.detached == ["FineSediPctPipe"]
    assert _records(db, "msm_ADComponent", "FineSediPctPipe") == []


def test_remove_user_defined_unknown_column_raises(read_only_db):
    pipes = read_only_db.tables.msm_Link

    with pytest.raises(KeyError):
        pipes.columns.remove_user_defined("my_col")

    with pytest.raises(KeyError):
        pipes.columns.remove_user_defined("Diameter")


def test_add_user_defined_restores_detached_column_with_data(db):
    pipes = db.tables.msm_Link
    muid = pipes.get_muids()[0]
    pipes.columns.add_user_defined("my_col", "integer")
    pipes.update({"my_col": 42}).by_muid(muid).execute()
    pipes.columns.remove_user_defined("my_col")

    record = pipes.columns.add_user_defined("my_col")

    assert pipes.columns.user_defined == ["my_col"]
    assert pipes.columns.detached == []
    assert _records(db, "msm_Link", "my_col") == [record]
    assert str(pipes.columns.db_types()["my_col"]) == "Int32"
    df = pipes.select(["my_col"]).by_muid(muid).to_dataframe()
    assert df["my_col"].iloc[0] == 42


def test_restore_with_matching_type_succeeds(db):
    components = db.tables.msm_ADComponent
    components.columns.remove_user_defined("FineSediPctPipe")

    components.columns.add_user_defined("FineSediPctPipe", "double")

    assert "FineSediPctPipe" in components.columns.user_defined


def test_restore_keeps_canonical_casing(db):
    components = db.tables.msm_ADComponent
    components.columns.remove_user_defined("FineSediPctPipe")

    muid = components.columns.add_user_defined("FINESEDIPCTPIPE")

    assert "FineSediPctPipe" in components.columns.user_defined
    assert _records(db, "msm_ADComponent", "FineSediPctPipe") == [muid]


def test_restore_with_different_type_raises_and_changes_nothing(db):
    components = db.tables.msm_ADComponent
    components.columns.remove_user_defined("FineSediPctPipe")

    with pytest.raises(ValueError, match="double"):
        components.columns.add_user_defined("FineSediPctPipe", "string")

    assert "FineSediPctPipe" not in components.columns
    assert components.columns.detached == ["FineSediPctPipe"]


def test_insert_and_update_set_new_column(db):
    pipes = db.tables.msm_Link
    pipes.columns.add_user_defined("my_col", "integer")

    muid = pipes.insert({"my_col": 1})
    pipes.update({"MY_COL": 2}).by_muid(pipes.get_muids()[0]).execute()

    df = pipes.select(["my_col"]).to_dataframe()
    assert df.loc[muid, "my_col"] == 1
    assert df.loc[pipes.get_muids()[0], "my_col"] == 2


def test_insert_and_update_set_restored_column(db):
    components = db.tables.msm_ADComponent
    components.columns.remove_user_defined("FineSediPctPipe")
    components.columns.add_user_defined("FineSediPctPipe")

    muid = components.insert({"FineSediPctPipe": 1.5})
    components.update({"FineSediPctPipe": 2.5}).by_muid(muid).execute()

    df = components.select(["FineSediPctPipe"]).by_muid(muid).to_dataframe()
    assert df["FineSediPctPipe"].iloc[0] == 2.5


def test_insert_sets_column_already_in_database(db):
    components = db.tables.msm_ADComponent

    muid = components.insert({"CoarseSediPctPipe": 3.5})

    df = components.select(["CoarseSediPctPipe"]).by_muid(muid).to_dataframe()
    assert df["CoarseSediPctPipe"].iloc[0] == 3.5


def test_add_user_defined_column_is_safe_to_repeat(db):
    pipes = db.tables.msm_Link

    first = pipes.add_user_defined_column("my_col", "integer", column_header="Mine")
    second = pipes.add_user_defined_column("my_col", "integer")

    assert first == second
    assert _records(db, "msm_Link", "my_col") == [first]
    with pytest.raises(ValueError):
        pipes.add_user_defined_column("my_col", "string")
