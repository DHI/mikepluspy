"""General utilities for mikepluspy."""


def to_sql(value) -> str:
    """Convert a Python value to its SQL string representation.

    Parameters
    ----------
    value
        The value to convert.

    Returns
    -------
    str
        The SQL string representation of the value.

    Examples
    --------
    >>> to_sql(10)
    '10'
    >>> to_sql(10.5)
    '10.5'
    >>> to_sql("test_muid")
    "'test_muid'"
    >>> to_sql(None)
    'NULL'
    """
    if value is None:
        return "NULL"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return f"'{str(value)}'"
