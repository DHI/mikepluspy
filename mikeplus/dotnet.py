"""Utilities for Python-to-.NET and .NET-to-Python conversions.

This module provides a set of utility functions and classes for handling
the conversion of data types between Python and .NET. It is primarily used
for database operations and interacting with the MIKE+ .NET API.
"""

from __future__ import annotations

import clr  # noqa: F401
import datetime
from typing import Any, Dict

import System
from System import String, Object, Nullable
from System.Collections.Generic import List, IList, IDictionary, Dictionary
from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper

from System.Data import DbType
import pandas as pd

def get_implementation(net_object: Any, raw: bool = False) -> Any:
    """Get the implementation of a .NET interface object.

    Parameters
    ----------
    net_object : Any
        The .NET object to get the implementation for
    raw : bool, optional
        When true, returns pure CLR object.
        When false, returns Python.NET marshalled/encoded object.

    Returns
    -------
    Any
        The implementation of the .NET object

    """
    if not hasattr(net_object, "__implementation__"):
        raise ValueError(f"Expected Python.NET interface object, got: {net_object}")

    if not raw:
        return net_object.__implementation__
    else:
        return net_object.__raw_implementation__


class DotNetConverter:
    """Handles conversions between Python and .NET data types.

    This class provides static methods for converting between Python and .NET
    data types, including primitives, collections, and geometric objects.
    """

    @staticmethod
    def to_dotnet_value(value: Any, db_type: DbType | None = None) -> Any:
        """Convert a Python value to its appropriate .NET equivalent.

        String values for Double fields accept either dot or comma as the
        decimal separator. Strings for DateTime fields are parsed and converted
        to ``System.DateTime``. Other strings are returned unchanged.

        Parameters
        ----------
        value : Any
            The Python value to convert

        db_type : DbType, optional
            Destination database type. Used to identify Double and DateTime fields.

        Returns
        -------
        Any
            Converted .NET value, or the original value when no conversion is
            required.

        """
        if value is None:
            return None
        elif isinstance(value, int):
            return Nullable[int](value)
        elif isinstance(value, float):
            return Nullable[float](value)
        elif isinstance(value, bool):
            return Nullable[bool](value)
        elif isinstance(value, datetime.datetime):
            return DotNetConverter.to_dotnet_datetime(value)
        elif isinstance(value, str):
            if db_type == DbType.Double:
                try:
                    return Nullable[float](float(value.replace(",", ".")))
                except ValueError:
                    return value
            if db_type != DbType.DateTime:
                return value
            value = pd.to_datetime(value).to_pydatetime()
            return DotNetConverter.to_dotnet_datetime(value)

        elif isinstance(value, list):
            return DotNetConverter.as_dotnet_list(value)
        # Add other type conversions as needed
        return value

    @staticmethod
    def from_dotnet_value(value: Any) -> Any:
        """Convert a .NET value to its appropriate Python equivalent.

        Parameters
        ----------
        value : Any
            The .NET value to convert

        Returns
        -------
        Any
            The converted Python value

        """
        if value is None:
            return None
        elif isinstance(value, System.DateTime):
            return DotNetConverter.from_dotnet_datetime(value)
        elif isinstance(value, IDictionary):
            return DotNetConverter.from_dotnet_dictionary(value)
        elif isinstance(value, IList[Object]):
            return DotNetConverter.from_dotnet_list(value)
        # Add other type conversions as needed
        return value

    @staticmethod
    def to_dotnet_dictionary(
        py_dict: Dict[str, Any],
        column_types: Dict[str, DbType] | None = None
    ) -> Dictionary[String, Object]:
        """Convert a Python dictionary to a .NET Dictionary.

        An empty/falsy ``py_dict`` yields an empty .NET Dictionary (not ``None``);
        some MIKE+ 2026 U1 insert APIs NullReference on a ``null`` fields argument.

        Parameters
        ----------
        py_dict : Dict[str, Any]
            Python dictionary to convert

        column_types : Dict[str, DbType], optional
            Casefold field names mapped to their destination database types.

        Returns
        -------
        Dictionary[String, Object]
            .NET Dictionary with converted values

        """
        net_dict = Dictionary[String, Object]()
        column_types = column_types or {}

        if not py_dict:
            return net_dict

        for key, value in py_dict.items():
            db_type = column_types.get(key.casefold())
            net_dict[key] = DotNetConverter.to_dotnet_value(value, db_type)

        return net_dict

    @staticmethod
    def from_dotnet_dictionary(net_dict: IDictionary) -> dict[str, Any] | None:
        """Convert a .NET Dictionary to a Python dictionary.

        Parameters
        ----------
        net_dict : IDictionary
            .NET Dictionary to convert

        Returns
        -------
        dict[str, Any] or None
            Python dictionary with converted values

        """
        if net_dict is None:
            return None

        result = {}

        # Iterate through the dictionary keys
        for key in net_dict.Keys:
            value = net_dict[key]
            result[key] = DotNetConverter.from_dotnet_value(value)

        return result

    @staticmethod
    def to_dotnet_geometry(geometry: str | Any) -> Any:
        """Convert a geometry to a .NET IGeometry object.

        Parameters
        ----------
        geometry : str or Any
            WKT geometry string or any object with a .wkt attribute or to_wkt() method

        Returns
        -------
        Any
            .NET IGeometry object or None if geometry is None

        """
        if geometry is None:
            return None

        if isinstance(geometry, str):
            return GeoAPIHelper.GetIGeometryFromWKT(geometry)
        else:
            # If we have a shapely geometry object, we can just call to_wkt() on it
            # No need to import shapely or check modules
            wkt = geometry.wkt if hasattr(geometry, "wkt") else geometry.to_wkt()
            return GeoAPIHelper.GetIGeometryFromWKT(wkt)

    @staticmethod
    def as_dotnet_list(py_list: list, dotnet_type=None) -> List:
        """Convert a Python list to a .NET List.

        Parameters
        ----------
        py_list : list
            The Python list to convert
        dotnet_type : type, optional
            .NET type for the list elements

        Returns
        -------
        List
            .NET List object

        """
        if not py_list:
            return List[String]()  # Default to string type for empty lists

        if dotnet_type is None:
            if isinstance(py_list[0], str):
                dotnet_type = String
            else:
                raise NotImplementedError(
                    f"Unsupported type '{type(py_list[0])}'. Please specify with dotnet_type."
                )

        dotnet_list = List[dotnet_type]()
        for item in py_list:
            dotnet_list.Add(item)
        return dotnet_list

    @staticmethod
    def to_dotnet_datetime(dt: datetime.datetime) -> System.DateTime:
        """Convert from Python datetime to .NET System.DateTime.

        Parameters
        ----------
        dt : datetime.datetime
            Python datetime object

        Returns
        -------
        System.DateTime
            .NET DateTime object

        """
        dotnet_datetime = System.DateTime(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
        )
        # Get .NET ticks microseconds
        ticks = dt.microsecond * 10
        dotnet_datetime = dotnet_datetime.AddTicks(ticks)
        return dotnet_datetime

    @staticmethod
    def from_dotnet_datetime(
        dt: System.DateTime, round_to_milliseconds=True
    ) -> datetime.datetime:
        """Convert from .NET System.DateTime to Python datetime.

        Parameters
        ----------
        dt : System.DateTime
            .NET DateTime object
        round_to_milliseconds : bool, optional
            Whether to round to milliseconds (default: True)

        Returns
        -------
        datetime.datetime
            Python datetime object

        """
        # Get microseconds from .NET ticks
        microseconds = dt.Ticks % 10**7 // 10
        time = datetime.datetime(
            dt.Year, dt.Month, dt.Day, dt.Hour, dt.Minute, dt.Second, microseconds
        )

        # Round to milliseconds if requested
        if round_to_milliseconds:
            microseconds_rounded = round(time.microsecond, -3)
            if microseconds_rounded == 10**6:
                time += datetime.timedelta(seconds=1)
                microseconds_rounded = 0
            time = time.replace(microsecond=microseconds_rounded)

        return time

    @staticmethod
    def from_dotnet_list(net_list: IList) -> list[Any]:
        """Convert a .NET IList to a Python list.

        Args:
            net_list: .NET IList object

        Returns
        -------
            Python list with converted values

        """
        if net_list is None:
            return []

        # Pythonnet handles IList conversion automatically
        return [DotNetConverter.from_dotnet_value(x) for x in net_list]


# For backward compatibility, keep the module-level functions
# but make them delegate to the DotNetConverter class methods


def as_dotnet_list(py_list: list, dotnet_type=None):
    """Convert Python list to .NET List.

    Parameters
    ----------
    py_list : list
        The Python list to convert
    dotnet_type : type, optional
        The .NET type of the list

    Returns
    -------
    List
        .NET List object

    """
    return DotNetConverter.as_dotnet_list(py_list, dotnet_type)


def to_dotnet_datetime(x):
    """Convert from Python datetime to .NET System.DateTime.

    Parameters
    ----------
    x : datetime.datetime
        Python datetime object

    Returns
    -------
    System.DateTime
        .NET DateTime object

    """
    return DotNetConverter.to_dotnet_datetime(x)


def from_dotnet_datetime(x, round_to_milliseconds=True):
    """Convert from .NET System.DateTime to Python datetime.

    Parameters
    ----------
    x : System.DateTime
        .NET DateTime object
    round_to_milliseconds : bool, optional
        Whether to round to milliseconds (default: True)

    Returns
    -------
    datetime.datetime
        Python datetime object

    """
    return DotNetConverter.from_dotnet_datetime(x, round_to_milliseconds)


def from_dotnet_dict(dotnet_dict):
    """Convert a .NET IDictionary to a Python dictionary.

    Parameters
    ----------
    dotnet_dict : System.Collections.Generic.IDictionary
        The .NET dictionary to convert

    Returns
    -------
    dict
        Python dictionary with converted values based on their type

    """
    return DotNetConverter.from_dotnet_dictionary(dotnet_dict)
