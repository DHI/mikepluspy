"""
MIKE+ Python API - Scenario class.

Represents a scenario in the MIKE+ model.
"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .alternative import Alternative

class Scenario:
    """Represents a scenario in the MIKE+ model.

    A scenario is a collection of alternatives from different alternative groups.
    Scenarios form a hierarchical tree structure with parent-child relationships.
    """
    
    def __init__(self, scenario_manager, net_scenario):
        """
        Parameters
        ----------
        scenario_manager : object
            The underlying scenario manager
        net_scenario : object
            The .NET IScenario object
        """
        self._scenario_manager = scenario_manager
        self._net_scenario = net_scenario
    
    @property
    def id(self) -> str:
        """The scenario's unique identifier.

        Returns
        -------
        str
            The scenario ID
        """
        return NotImplemented
    
    @property
    def name(self) -> str:
        """The scenario's name.

        Returns
        -------
        str
            The scenario name
        """
        return NotImplemented
    
    @name.setter
    def name(self, value: str) -> None:
        """Set the scenario name.
        
        Parameters
        ----------
        value : str
            The new name for the scenario
        """
        pass
    
    @property
    def parent(self) -> Optional["Scenario"]:
        """The parent scenario.

        Returns
        -------
        Scenario or None
            The parent scenario or None if this is the base scenario
        """
        return NotImplemented
    
    @property
    def children(self) -> List["Scenario"]:
        """The child scenarios.

        Returns
        -------
        list of Scenario
            The child scenarios of this scenario
        """
        return NotImplemented
    
    @property
    def alternatives(self) -> List["Alternative"]:
        """The alternatives assigned to this scenario.

        Returns
        -------
        list of Alternative
            The alternatives assigned to this scenario
        """
        return NotImplemented
    
    @property
    def is_active(self) -> bool:
        """Whether this scenario is the currently active scenario.

        Returns
        -------
        bool
            True if this is the active scenario, False otherwise
        """
        return NotImplemented
    
    def activate(self) -> None:
        """Activate this scenario.
        
        Makes this scenario the currently active scenario in the model.
        This will affect which alternatives are used when accessing model data.
        """
        pass
    
    def set_alternative(self, alternative: "Alternative") -> None:
        """
        Add/replace an alternative in this scenario.
        
        Parameters
        ----------
        alternative : Alternative
            The alternative to add to this scenario. If the scenario already
            has an alternative for the same group, it will be replaced.
        """
        pass
