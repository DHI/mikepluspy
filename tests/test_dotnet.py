"""Regression tests for Python-to-.NET value conversion."""

import datetime

import pytest
from mikeplus.dotnet import DotNetConverter
import System
from System.Data import DbType


@pytest.mark.parametrize("value", ["760309", "33,34"])
def test_arbitrary_strings_are_not_inferred_as_datetimes(value):
    """Keep numeric-looking identifiers and comma-separated text as strings."""
    converted = DotNetConverter.to_dotnet_value(value)

    assert isinstance(converted, str)
    assert converted == value


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("1.2", 1.2),
        ("1,2", 1.2),
        ("-1.2", -1.2),
        ("-1,2", -1.2),
        ("800", 800.0),
        ("+3", 3.0),
        (".5", 0.5),
        (",5", 0.5),
        (" 2,5 ", 2.5),
        ("1.5e3", 1500.0),
        ("1,234", 1.234),
    ],
)
def test_double_strings_accept_dot_or_comma_decimal_separator(value, expected):
    """Convert either decimal separator for schema-declared Double fields."""
    converted = DotNetConverter.to_dotnet_value(value, DbType.Double)

    assert not isinstance(converted, str)
    assert converted.GetType().FullName == "System.Double"
    assert converted.Value == pytest.approx(expected)


@pytest.mark.parametrize(
    "value",
    ["not a number", "1,2,3", "1.234,5", "1,234.5", "1 234", "1_000", "nan", "inf"],
)
def test_invalid_double_strings_raise(value):
    """Reject strings whose meaning would depend on the reader's locale."""
    with pytest.raises(ValueError, match="Cannot parse"):
        DotNetConverter.to_dotnet_value(value, DbType.Double)


@pytest.mark.parametrize("value", ["", "  "])
def test_empty_double_strings_become_none(value):
    """Treat an empty Double string as a null value."""
    assert DotNetConverter.to_dotnet_value(value, DbType.Double) is None


def test_dictionary_conversion_error_names_the_field():
    """Say which field held the value that couldn't be converted."""
    with pytest.raises(ValueError, match="^Diameter: Cannot parse '1.234,5'"):
        DotNetConverter.to_dotnet_dictionary(
            {"Diameter": "1.234,5"}, {"diameter": DbType.Double}
        )


def test_dictionary_conversion_respects_schema_column_types():
    """Convert only strings belonging to schema-declared DateTime fields."""
    values = {
        "assetname": "760309",
        "dem_location": "33,34",
        "ComputationBegin": "2025-01-01 14:30:00",
    }
    column_types = {
        "assetname": DbType.String,
        "dem_location": DbType.String,
        "computationbegin": DbType.DateTime,
    }

    converted = DotNetConverter.to_dotnet_dictionary(values, column_types)

    assert converted["assetname"] == "760309"
    assert converted["dem_location"] == "33,34"
    assert isinstance(converted["ComputationBegin"], System.DateTime)
    assert DotNetConverter.from_dotnet_datetime(
        converted["ComputationBegin"]
    ) == datetime.datetime(2025, 1, 1, 14, 30)


@pytest.mark.parametrize("value", ["", "  "])
def test_empty_datetime_strings_become_none(value):
    """Treat an empty DateTime string as a null value."""
    assert DotNetConverter.to_dotnet_value(value, DbType.DateTime) is None


@pytest.mark.parametrize("value", [None, {}])
def test_empty_string_dictionary_is_empty_not_null(value):
    converted = DotNetConverter.to_dotnet_string_dictionary(value)
    assert converted is not None
    assert converted.Count == 0


def test_string_dictionary_keeps_keys_and_values():
    values = {"MUID": "ID", "TypeNo": "T"}
    converted = DotNetConverter.to_dotnet_string_dictionary(values)
    assert isinstance(converted, System.Collections.Generic.Dictionary[str, str])
    assert DotNetConverter.from_dotnet_dictionary(converted) == values
