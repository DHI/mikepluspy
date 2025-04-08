"""
.NET conversion utilities for Python-to-.NET and .NET-to-Python conversions.
"""
from __future__ import annotations
from _typeshed import NoneType

import clr  # noqa: F401
import datetime
from typing import Any, Dict, Optional

import System
from System import String, Object, Nullable
from System.Collections.Generic import List, IList, IDictionary, Dictionary
from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper


class DotNetConverter:
    """
    Handles conversions between Python and .NET data types.
    """

    @staticmethod
    def to_dotnet_value(value: Any) -> Any:
        """
        Convert a Python value to its appropriate .NET equivalent for database operations.

        Args:
            value: The Python value to convert

        Returns:
            The converted .NET value
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
            return value  # Strings automatically convert
        elif isinstance(value, list):
            return DotNetConverter.as_dotnet_list(value)
        # Add other type conversions as needed
        return value

    @staticmethod
    def from_dotnet_value(value: Any) -> Any:
        """
        Convert a .NET value to its appropriate Python equivalent.

        Args:
            value: The .NET value to convert

        Returns:
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
    ) -> Optional[Dictionary[String, Object]]:
        """
        Convert a Python dictionary to a .NET Dictionary.

        Args:
            py_dict: Python dictionary to convert

        Returns:
            .NET Dictionary with converted values
        """
        if not py_dict:
            return None

        net_dict = Dictionary[String, Object]()

        for key, value in py_dict.items():
            net_dict[key] = DotNetConverter.to_dotnet_value(value)

        return net_dict

    @staticmethod
    def from_dotnet_dictionary(net_dict: IDictionary) -> dict[str, Any] | None:
        """
        Convert a .NET Dictionary to a Python dictionary.

        Args:
            net_dict: .NET Dictionary to convert

        Returns:
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
        """
        Convert a geometry to a .NET IGeometry object.

        Args:
            geometry: WKT geometry string or any object with a .wkt attribute or to_wkt() method

        Returns:
            .NET IGeometry object or None if geometry is None
        """
        if geometry is None:
            return None
            
        if isinstance(geometry, str):
            return GeoAPIHelper.GetIGeometryFromWKT(geometry)
        else:
            # If we have a shapely geometry object, we can just call to_wkt() on it
            # No need to import shapely or check modules
            wkt = geometry.wkt if hasattr(geometry, 'wkt') else geometry.to_wkt()
            return GeoAPIHelper.GetIGeometryFromWKT(wkt)

    @staticmethod
    def as_dotnet_list(py_list: list, dotnet_type=None) -> List:
        """
        Convert a Python list to a .NET List.

        Args:
            py_list: The Python list to convert
            dotnet_type: Optional .NET type for the list elements

        Returns:
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
        """
        Convert from python datetime to .NET System.DateTime.

        Args:
            dt: Python datetime object

        Returns:
            .NET System.DateTime object
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
        """
        Convert from .NET System.DateTime to python datetime.

        Args:
            dt: .NET System.DateTime object
            round_to_milliseconds: Whether to round microseconds to milliseconds

        Returns:
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
        """
        Convert a .NET IList to a Python list.

        Args:
            net_list: .NET IList object

        Returns:
            Python list with converted values
        """
        if net_list is None:
            return []

        # Pythonnet handles IList conversion automatically
        return list(net_list)


# For backward compatibility, keep the module-level functions
# but make them delegate to the DotNetConverter class methods


def as_dotnet_list(py_list: list, dotnet_type=None):
    """
    Convert python list to .NET List.

    Parameters
    ----------
    py_list : list
        The python list to convert.
    dotnet_type : T, optional
        The .NET type of the list.

    Returns
    -------
    List[T]
        .NET List<T> object.
    """
    return DotNetConverter.as_dotnet_list(py_list, dotnet_type)


def to_dotnet_datetime(x):
    """Convert from python datetime to .NET System.DateTime."""
    return DotNetConverter.to_dotnet_datetime(x)


def from_dotnet_datetime(x, round_to_milliseconds=True):
    """Convert from .NET System.DateTime to python datetime."""
    return DotNetConverter.from_dotnet_datetime(x, round_to_milliseconds)


def from_dotnet_dict(dotnet_dict):
    """
    Convert a .NET IDictionary to a Python dictionary.

    Parameters
    ----------
    dotnet_dict : System.Collections.Generic.IDictionary
        The .NET dictionary to convert.

    Returns
    -------
    dict
        Python dictionary with converted values based on their type.
    """
    return DotNetConverter.from_dotnet_dictionary(dotnet_dict)
