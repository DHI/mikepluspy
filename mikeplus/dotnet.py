import clr  # noqa: F401

from System import String
from System.Collections.Generic import List


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
