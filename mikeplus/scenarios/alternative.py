"""
MIKE+ Python API - Alternative class.

Represents an alternative in the MIKE+ model.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .alternative_group import AlternativeGroup
    from .scenario import Scenario


class Alternative:
    """Represents an alternative in the MIKE+ model.

    An alternative represents a specific configuration of a model component.
    Alternatives form a hierarchical tree structure with parent-child relationships.

    Attributes
    ----------
    id : int
        Unique identifier for the alternative
    name : str
        Name of the alternative
    group : AlternativeGroup
        The group this alternative belongs to
    parent : Alternative or None
        Parent alternative (None if base alternative)
    children : list[Alternative]
        Child alternatives derived from this one
    is_active : bool
        Whether this alternative is part of the active scenario
    is_base : bool
        Whether this is the base alternative for its group
    comment : str
        User comment attached to this alternative
    scenarios : list[Scenario]
        Scenarios that use this alternative

    Examples
    --------
    >>> alt = db.scenarios.alternative_groups["CS Network data"].active
    >>> print(f"Active network: {alt.name}")
    >>> print(f"Parent: {alt.parent.name if alt.parent else 'None'}")
    >>> print(f"Child count: {len(alt.children)}")
    """

    def __init__(self, scenario_manager, net_alternative):
        """Alternative constructor.

        Parameters
        ----------
        scenario_manager : IScenarioManager
            The underlying .NET scenario manager object
        net_alternative : IAlternative
            The .NET IAlternative object
        """
        self._scenario_manager = scenario_manager
        self._net_alternative = net_alternative

    def __repr__(self):
        """Return a string representation of the alternative."""
        return f"Alternative <{self.name}>"

    def __eq__(self, other: object) -> bool:
        """Check if two alternatives are equal."""
        if not isinstance(other, Alternative):
            return False
        return self.id == other.id

    @property
    def id(self) -> int:
        """Alternative's unique identifier."""
        return int(self._net_alternative.AltId)

    @property
    def name(self) -> str:
        """Alternative's name.

        Returns
        -------
        str
            The name of the alternative

        Raises
        ------
        ValueError
            If the alternative name could not be changed
        """
        return str(self._net_alternative.Name)

    @name.setter
    def name(self, value: str) -> None:
        if not self._scenario_manager.RenameAlternative(self._net_alternative, value):
            raise ValueError(f"Failed to rename alternative to '{value}'.")

    @property
    def group(self) -> AlternativeGroup:
        """Alternative group this alternative belongs to."""
        from .alternative_group import AlternativeGroup

        return AlternativeGroup(self._scenario_manager, self._net_alternative.Group)

    @property
    def parent(self) -> Alternative | None:
        """Parent alternative (None if this is the base alternative)."""
        parent = self._net_alternative.Parent
        if parent is None:
            return None
        return Alternative(self._scenario_manager, parent)

    @property
    def children(self) -> list[Alternative]:
        """Child alternatives derived from this alternative."""
        children = []
        for child in self._net_alternative.Children:
            children.append(Alternative(self._scenario_manager, child))
        return children

    @property
    def is_active(self) -> bool:
        """Whether this alternative is part of the active scenario."""
        return self._net_alternative.IsActive

    @property
    def is_base(self) -> bool:
        """Whether this alternative is the base alternative for its group."""
        return self._net_alternative.IsBase

    @property
    def comment(self) -> str:
        """Alternative's comment."""
        return (
            str(self._net_alternative.Comment) if self._net_alternative.Comment else ""
        )

    @comment.setter
    def comment(self, value: str) -> None:
        """Set the alternative comment."""
        self._scenario_manager.SetComment(self._net_alternative, value)

    @property
    def scenarios(self) -> list[Scenario]:
        """Scenarios that use this alternative."""
        from .scenario import Scenario

        scenarios = []
        for scenario_id in self._scenario_manager.GetScenarios():
            scenario = self._scenario_manager.FindScenario(scenario_id)
            for alt in scenario.CurAlternatives:
                if alt.AltId == self._net_alternative.AltId:
                    scenarios.append(Scenario(self._scenario_manager, scenario))
                    break

        return scenarios
