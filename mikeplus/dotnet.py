import clr  # noqa: F401

import System
from System import String
from System.Collections.Generic import List, IDictionary
import datetime


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


def to_dotnet_datetime(x):
    """Convert from python datetime to .NET System.DateTime."""
    dotnet_datetime = System.DateTime(
        x.year, x.month, x.day, x.hour, x.minute, x.second
    )
    # Get .NET ticks microseconds
    ticks = x.microsecond * 10
    dotnet_datetime = dotnet_datetime.AddTicks(ticks)
    return dotnet_datetime


def from_dotnet_datetime(x, round_to_milliseconds=True):
    """Convert from .NET System.DateTime to python datetime."""
    # Get microseconds from .NET ticks
    microseconds = x.Ticks % 10**7 // 10
    time = datetime.datetime(
        x.Year, x.Month, x.Day, x.Hour, x.Minute, x.Second, microseconds
    )

    # Round to milliseconds if requested
    if round_to_milliseconds:
        microseconds_rounded = round(time.microsecond, -3)
        if microseconds_rounded == 10**6:
            time += datetime.timedelta(seconds=1)
            microseconds_rounded = 0
        time = time.replace(microsecond=microseconds_rounded)

    return time


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
    if dotnet_dict is None:
        return None
        
    result = {}
    
    # Iterate through the dictionary keys
    for key in dotnet_dict.Keys:
        value = dotnet_dict[key]
        
        # Convert the value based on its type
        if hasattr(value, 'GetType') and value.GetType().IsGenericType and \
           value.GetType().GetGenericTypeDefinition().FullName.startswith('System.Collections.Generic.List'):
            # Convert .NET IList to Python list
            py_value = [item for item in value]
        elif isinstance(value, IDictionary):
            # Recursively convert nested dictionaries
            py_value = from_dotnet_dict(value)
        elif isinstance(value, System.DateTime):
            # Convert DateTime using existing function
            py_value = from_dotnet_datetime(value)
        else:
            # Use the value as is for simple types
            py_value = value
        
        # Add to the result dictionary
        result[key] = py_value
        
    return result
