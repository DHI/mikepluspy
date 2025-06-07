"""
MIKE+ Python API - Scenario class.

Represents a scenario in the MIKE+ model.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .alternative import Alternative


class Scenario:
    """Represents a scenario in the MIKE+ model.

    A scenario is a collection of alternatives from different alternative groups.
    Scenarios form a hierarchical tree structure with parent-child relationships.
    
    Attributes
    ----------
    id : str
        Unique identifier for the scenario
    name : str
        Name of the scenario
    parent : Scenario or None
        Parent scenario (None if base scenario)
    children : list[Scenario]
        Child scenarios derived from this one
    alternatives : list[Alternative]
        Alternatives assigned to this scenario
    is_active : bool
        Whether this is the currently active scenario
    is_base : bool
        Whether this is the base scenario
    comment : str
        User comment attached to this scenario
        
    Methods
    -------
    activate()
        Make this the active scenario
    set_alternative(alternative)
        Add or replace an alternative in this scenario
    contains_alternative(alternative) : bool
        Check if this scenario uses a specific alternative
        
    Examples
    --------
    >>> # Activate a scenario
    >>> scenario = db.scenarios.by_name("Future Development")
    >>> scenario.activate()
    >>> 
    >>> # See which alternatives are used
    >>> for alt in scenario.alternatives:
    ...     print(f"{alt.group.name}: {alt.name}")
    """

    def __init__(self, scenario_manager, net_scenario):
        """Scenario constructor.

        Parameters
        ----------
        scenario_manager : IScenarioManager
            The underlying scenario manager
        net_scenario : IScenario
            The .NET IScenario object
        """
        self._scenario_manager = scenario_manager
        self._net_scenario = net_scenario

    def __repr__(self):
        """Get string representation of the Scenario object."""
        return f"Scenario <{self.name}>"

    def __eq__(self, other: object) -> bool:
        """Check if two scenarios are equal."""
        if not isinstance(other, Scenario):
            return False
        return self.id == other.id

    @property
    def id(self) -> str:
        """Scenario's unique identifier."""
        return str(self._net_scenario.Id)

    @property
    def name(self) -> str:
        """Scenario's name."""
        return str(self._net_scenario.Name)

    @name.setter
    def name(self, value: str) -> None:
        """Set the scenario name.
        
        Raises
        ------
        ValueError
            If the scenario name could not be changed
        """
        if not self._scenario_manager.RenameScenario(self._net_scenario, value):
            raise ValueError(f"Failed to rename scenario to '{value}'.")

    @property
    def parent(self) -> Scenario | None:
        """Parent scenario (None if this is the base scenario)."""
        parent_scenario = self._net_scenario.Parent
        if parent_scenario is None:
            return None
        return Scenario(self._scenario_manager, parent_scenario)

    @property
    def children(self) -> list[Scenario]:
        """Child scenarios derived from this scenario."""
        children = []
        for child in self._net_scenario.Children:
            children.append(Scenario(self._scenario_manager, child))
        return children

    @property
    def alternatives(self) -> list[Alternative]:
        """Alternatives assigned to this scenario."""
        from .alternative import Alternative

        alternatives = []
        for alt in self._net_scenario.CurAlternatives:
            alternatives.append(Alternative(self._scenario_manager, alt))
        return alternatives

    @property
    def is_active(self) -> bool:
        """Whether this scenario is the currently active scenario."""
        active_scenario = self._scenario_manager.ActiveScenario
        if active_scenario is None:
            return False
        return active_scenario.Id == self._net_scenario.Id

    @property
    def is_base(self) -> bool:
        """Whether this is the base scenario."""
        return self._net_scenario.IsBase

    @property
    def comment(self) -> str:
        """Scenario's comment."""
        return str(self._net_scenario.Comment) if self._net_scenario.Comment else ""

    @comment.setter
    def comment(self, value: str) -> None:
        """Set the scenario comment."""
        self._scenario_manager.SetComment(self._net_scenario, value)

    def activate(self) -> None:
        """Make this the currently active scenario in the model."""
        try:
            self._scenario_manager.ActivateScenario(self.id)
        except Exception as e:
            raise ValueError(f"Failed to activate scenario: {e}")

    def set_alternative(self, alternative: Alternative) -> None:
        """
        Add/replace an alternative in this scenario.

        Parameters
        ----------
        alternative : Alternative
            The alternative to add to this scenario. If the scenario already
            has an alternative for the same group, it will be replaced.

        Raises
        ------
        ValueError
            If the alternative could not be assigned to the scenario
        """
        try:
            self._scenario_manager.AddAlternative(self.id, alternative.id)
        except Exception as e:
            try:
                self._scenario_manager.AddAlternative(
                    self._net_scenario, alternative._net_alternative
                )
            except Exception as inner_e:
                raise ValueError(f"Failed to set alternative: {inner_e}") from e

    def contains_alternative(self, alternative: Alternative) -> bool:
        """Check if this scenario uses a specific alternative.

        Parameters
        ----------
        alternative : Alternative
            The alternative to check for

        Returns
        -------
        bool
            True if this scenario uses the alternative, False otherwise
        """
        return self._net_scenario.ContainsAlternative(alternative._net_alternative)
