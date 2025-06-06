"""
MIKE+ Python API - AlternativeGroup class.

Represents a group of alternatives in the MIKE+ model.

An alternative group contains alternatives for specific tables or model components.
Each group has a base alternative and potentially an active alternative.
"""
from typing import List, Iterator, Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .alternative import Alternative

class AlternativeGroup:
    """Represents an alternative group with collection-like access to alternatives.

    Provides a Pythonic interface for accessing and managing alternatives within a group.
    """
    
    def __init__(self, scenario_manager, net_alternative_group):
        """
        Parameters
        ----------
        scenario_manager : object
            The underlying scenario manager
        net_alternative_group : object
            The .NET IAlternativeGroup object
        """
        self._scenario_manager = scenario_manager
        self._net_alternative_group = net_alternative_group
    
    @property
    def id(self) -> str:
        """The group's unique identifier.

        Returns
        -------
        str
            The group ID
        """
        return NotImplemented
    
    @property
    def name(self) -> str:
        """The group's name.

        Returns
        -------
        str
            The group name
        """
        return NotImplemented
    
    @property
    def tables(self) -> List[str]:
        """The database tables associated with this group.

        Returns
        -------
        list of str
            The table names associated with this group
        """
        return NotImplemented
    
    @property
    def base(self) -> "Alternative":
        """The base alternative for this group.

        Returns
        -------
        Alternative
            The base alternative for this group
        """
        return NotImplemented
    
    @property
    def active(self) -> "Alternative":
        """The alternative assigned to the active scenario for this group.

        Returns
        -------
        Alternative
            The currently active alternative for this group
        """
        return NotImplemented
    
    def __getitem__(self, key: Union[str, int]) -> "Alternative":
        """
        Access alternative by ID (int) or name (str).

        Parameters
        ----------
        key : str or int
            The alternative ID (int) or name (str)

        Returns
        -------
        Alternative
            The matching Alternative object

        Raises
        ------
        KeyError
            If no alternative matches the given key
        """
        return NotImplemented
    
    def __iter__(self) -> Iterator["Alternative"]:
        """Iterate through all alternatives in this group.

        Returns
        -------
        iterator
            Iterator over all alternatives in this group
        """
        return NotImplemented
    
    def find_by_name(self, name: str) -> List["Alternative"]:
        """
        Find alternatives by name (may return multiple if names aren't unique).

        Parameters
        ----------
        name : str
            The name to search for

        Returns
        -------
        list of Alternative
            A list of matching alternatives
        """
        return NotImplemented
    
    def create(self, name: str, parent: Optional["Alternative"] = None) -> "Alternative":
        """
        Create a new alternative, optionally as a child of another.

        Parameters
        ----------
        name : str
            Name for the new alternative
        parent : Alternative, optional
            Optional parent alternative (defaults to base alternative if None)

        Returns
        -------
        Alternative
            The newly created Alternative
        """
        return NotImplemented
