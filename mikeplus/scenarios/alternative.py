"""
MIKE+ Python API - Alternative class.

Represents an alternative in the MIKE+ model.
"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .alternative_group import AlternativeGroup
    from .scenario import Scenario

class Alternative:
    """Represents an alternative in the MIKE+ model.

    An alternative represents a specific configuration of a model component.
    Alternatives form a hierarchical tree structure with parent-child relationships.
    """
    
    def __init__(self, scenario_manager, net_alternative):
        """
        Parameters
        ----------
        scenario_manager : object
            The underlying scenario manager
        net_alternative : object
            The .NET IAlternative object
        """
        self._scenario_manager = scenario_manager
        self._net_alternative = net_alternative
    
    @property
    def id(self) -> int:
        """The alternative's unique identifier.

        Returns
        -------
        int
            The alternative ID
        """
        return NotImplemented
    
    @property
    def name(self) -> str:
        """The alternative's name.

        Returns
        -------
        str
            The alternative name
        """
        return NotImplemented
    
    @name.setter
    def name(self, value: str) -> None:
        """Set the alternative name.
        
        Parameters
        ----------
        value : str
            The new name for the alternative
        """
        pass
    
    @property
    def group(self) -> "AlternativeGroup":
        """The alternative group this alternative belongs to.

        Returns
        -------
        AlternativeGroup
            The alternative group
        """
        return NotImplemented
    
    @property
    def parent(self) -> Optional["Alternative"]:
        """The parent alternative.

        Returns
        -------
        Alternative or None
            The parent alternative or None if this is the base alternative
        """
        return NotImplemented
    
    @property
    def children(self) -> List["Alternative"]:
        """The child alternatives.

        Returns
        -------
        list of Alternative
            The child alternatives of this alternative
        """
        return NotImplemented
    
    @property
    def is_active(self) -> bool:
        """Whether this alternative is part of the active scenario.

        Returns
        -------
        bool
            True if this alternative is part of the active scenario, False otherwise
        """
        return NotImplemented
    
    @property
    def scenarios(self) -> List["Scenario"]:
        """The scenarios that use this alternative.

        Returns
        -------
        list of Scenario
            The scenarios that use this alternative
        """
        return NotImplemented
