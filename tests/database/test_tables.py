"""
Tests for the table classes.
"""

from __future__ import annotations

import pytest

from mikeplus.database import Database
from mikeplus.tables import BaseTable
from mikeplus.queries import SelectQuery
from mikeplus.queries import UpdateQuery
from mikeplus.queries import DeleteQuery
from mikeplus.queries import InsertQuery
from mikeplus.tables.base_table_columns import BaseColumns


class TestBaseTable:
    """Tests for the BaseTable class."""

    @pytest.fixture(scope="class")
    def IMuTable(self, class_sirius_db):
        """Fixture providing an IMuTable instance."""
        db = Database(class_sirius_db)
        yield db._data_table_container.GetTable("msm_Link")
        db.close()

    @pytest.fixture
    def base_table(self, IMuTable):
        """Fixture providing a BaseTable instance."""
        yield BaseTable(IMuTable)

    def test_name(self, base_table):
        """Test name property."""
        assert base_table.name == "msm_Link"

    def test_display_name(self, base_table):
        """Test display_name property."""
        assert base_table.display_name == "Pipes and canals"

    def test_description(self, base_table):
        """Test description property."""
        assert base_table.description == "Table of links"

    def test_columns(self, base_table):
        """Test columns property."""
        assert isinstance(base_table.columns, BaseColumns)
        assert "MUID" in base_table.columns
        assert len(tuple(base_table.columns)) == 50

    def test_get_muids(self, base_table):
        """Test get_muids method."""
        assert base_table.get_muids() == [
            "Link_29",
            "Link_30",
            "Link_34",
            "Link_35",
            "Link_36",
            "Link_37",
            "Link_33",
            "Link_2",
        ]

    def test_get_muids_with_order_by(self, base_table):
        """Test get_muids with order_by parameter returns ordered list."""
        muids = base_table.get_muids(order_by="MUID")
        expected = sorted(
            [
                "Link_29",
                "Link_30",
                "Link_34",
                "Link_35",
                "Link_36",
                "Link_37",
                "Link_33",
                "Link_2",
            ]
        )
        assert muids == expected

    def test_get_muids_with_descending(self, base_table):
        """Test get_muids with descending parameter returns descending ordered list."""
        muids = base_table.get_muids(order_by="MUID", descending=True)
        expected = sorted(
            [
                "Link_29",
                "Link_30",
                "Link_34",
                "Link_35",
                "Link_36",
                "Link_37",
                "Link_33",
                "Link_2",
            ],
            reverse=True,
        )
        assert muids == expected

    def test_select_returns_select_query(self, base_table):
        """Test select method returns a SelectQuery instance."""
        query = base_table.select()
        assert isinstance(query, SelectQuery)
        assert query._table == base_table

    def test_select_with_columns(self, base_table):
        """Test select method with columns creates properly configured query."""
        query = base_table.select(["MUID", "Diameter"])
        assert isinstance(query, SelectQuery)
        assert query._table == base_table
        assert query._columns == ["MUID", "Diameter"]

    def test_insert_query(self, base_table):
        """Test insert method with values returns an InsertQuery instance."""
        values = {"MUID": "Testing123"}
        query = base_table.insert(values, execute=False)
        assert isinstance(query, InsertQuery)
        assert query._table == base_table
        assert query._values == values

        # Default execute=True
        result = base_table.insert(values)
        assert result == values["MUID"]
        assert result in base_table.get_muids()

    def test_update_returns_update_query(self, base_table):
        """Test update method returns an UpdateQuery instance."""
        update_values = {"Diameter": 100.0}
        query = base_table.update(update_values)

        # Verify it's an UpdateQuery
        assert isinstance(query, UpdateQuery)

        # Verify it's configured with the table
        assert query._table == base_table
        assert query._values == update_values

    def test_delete_returns_delete_query(self, base_table):
        """Test delete method returns a DeleteQuery instance."""
        query = base_table.delete()

        # Verify it's a DeleteQuery
        assert isinstance(query, DeleteQuery)

        # Verify it's configured with the table
        assert query._table == base_table

    def test_add_user_defined_column(self, base_table: BaseTable):
        base_table.add_user_defined_column("test_column", "integer")

        # Should be None at first
        df = base_table.select(["test_column"]).to_dataframe()
        "test_column" in df.columns
        assert df["test_column"].isnull().all()

        # Set the value
        n_updated = (
            base_table.update(({"test_column": 42})).by_muid("Link_29").execute()
        )
        assert len(n_updated) == 1
        df = base_table.select(["test_column"]).by_muid("Link_29").to_dataframe()
        assert df["test_column"].iloc[0] == 42

        # Insert a new link
        new_muid = base_table.insert({"test_column": 99})
        df = base_table.select(["test_column"]).by_muid(new_muid).to_dataframe()
        assert df["test_column"].iloc[0] == 99

        # data_access.set_value("msm_Link", "Link_29", "test_column", 42)
        # values = data_access.get_field_values("msm_Link", "Link_29", "test_column")
        # assert values[0] == 42
