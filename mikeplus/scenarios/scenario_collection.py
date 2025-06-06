"""
MIKE+ Python API - ScenarioCollection class.

Collection-like access to scenarios in the MIKE+ model.
"""
from typing import List, Iterator, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .scenario import Scenario

class ScenarioCollection:
    """Collection-like access to scenarios in the database.

    Provides a Pythonic interface for accessing scenarios in the MIKE+ model.
    """
    
    def __init__(self, scenario_manager):
        """
        Parameters
        ----------
        scenario_manager : object
            The underlying .NET scenario manager object
        """
        self._scenario_manager = scenario_manager
    
    @property
    def active(self) -> "Scenario":
        """Get the currently active scenario.

        Returns
        -------
        Scenario
            The currently active scenario
        """
        return NotImplemented
        
    @property
    def base(self) -> "Scenario":
        """Get the base scenario.

        Returns
        -------
        Scenario
            The base scenario
        """
        return NotImplemented
    
    def __getitem__(self, id: str) -> "Scenario":
        """
        Access scenario by its ID.

        Parameters
        ----------
        id : str
            The scenario ID

        Returns
        -------
        Scenario
            The matching Scenario object

        Raises
        ------
        KeyError
            If no scenario matches the given ID
        """
        return NotImplemented
    
    def __iter__(self) -> Iterator["Scenario"]:
        """Iterate through all scenarios.

        Returns
        -------
        iterator
            Iterator over all scenarios
        """
        return NotImplemented
    
    def find_by_name(self, name: str) -> List["Scenario"]:
        """
        Find scenarios by name (may return multiple if names aren't unique).

        Parameters
        ----------
        name : str
            The name to search for

        Returns
        -------
        list of Scenario
            A list of matching scenarios
        """
        return NotImplemented
    
    def find_by_id(self, id: str) -> Optional["Scenario"]:
        """
        Find a scenario by its exact ID (returns single item or None).

        Parameters
        ----------
        id : str
            The ID to search for

        Returns
        -------
        Scenario or None
            The matching scenario or None if not found
        """
        return NotImplemented
    
    def create(self, parent: "Scenario", name: str) -> "Scenario":
        """
        Create a new child scenario.

        Parameters
        ----------
        parent : Scenario
            The parent scenario
        name : str
            Name for the new scenario

        Returns
        -------
        Scenario
            The newly created Scenario
        """
        return NotImplemented
        
    def delete(self, scenario: Union["Scenario", str]) -> None:
        """
        Delete a scenario from the database.

        Parameters
        ----------
        scenario : Scenario or str
            The scenario object or scenario ID to delete

        Raises
        ------
        ValueError
            If attempting to delete the base scenario
        KeyError
            If the scenario ID is not found
        """
        return NotImplemented
