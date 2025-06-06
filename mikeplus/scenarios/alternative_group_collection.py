"""
MIKE+ Python API - AlternativeGroupCollection class.

Collection-like access to alternative groups in the MIKE+ model.

Provides a Pythonic interface for accessing alternative groups in the MIKE+ model.
"""
from typing import Iterator, TYPE_CHECKING

if TYPE_CHECKING:
    from .alternative_group import AlternativeGroup

class AlternativeGroupCollection:
    """Collection-like access to alternative groups.

    Provides a Pythonic interface for accessing and managing alternative groups.
    """
    
    def __init__(self, scenario_manager):
        """
        Parameters
        ----------
        scenario_manager : object
            The underlying scenario manager
        """
        self._scenario_manager = scenario_manager
    
    def __getitem__(self, key: str) -> "AlternativeGroup":
        """
        Access group by ID or name.

        Parameters
        ----------
        key : str
            The group ID or name

        Returns
        -------
        AlternativeGroup
            The matching AlternativeGroup object

        Raises
        ------
        KeyError
            If no group matches the given key
        """
        return NotImplemented
    
    def __iter__(self) -> Iterator["AlternativeGroup"]:
        """Iterate through all alternative groups.

        Returns
        -------
        iterator
            Iterator over all alternative groups
        """
        return NotImplemented
    
    def by_table(self, table_name: str) -> "AlternativeGroup":
        """
        Find the alternative group associated with a specific table.

        Parameters
        ----------
        table_name : str
            The table name to look for

        Returns
        -------
        AlternativeGroup
            The alternative group associated with the table

        Raises
        ------
        KeyError
            If no group is associated with the given table
        """
        return NotImplemented
