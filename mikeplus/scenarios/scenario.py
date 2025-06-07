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

    @property
    def id(self) -> str:
        """The scenario's unique identifier.

        Returns
        -------
        str
            The scenario ID
        """
        return str(self._net_scenario.Id)

    @property
    def name(self) -> str:
        """The scenario's name.

        Returns
        -------
        str
            The scenario name
        """
        return str(self._net_scenario.Name)

    @name.setter
    def name(self, value: str) -> None:
        """Set the scenario name.

        Parameters
        ----------
        value : str
            The new name for the scenario

        Raises
        ------
        ValueError
            If the scenario name could not be changed
        """
        if not self._scenario_manager.RenameScenario(self._net_scenario, value):
            raise ValueError(f"Failed to rename scenario to '{value}'.")

    @property
    def parent(self) -> "Scenario" | None:
        """The parent scenario.

        Returns
        -------
        Scenario or None
            The parent scenario or None if this is the base scenario
        """
        parent_scenario = self._net_scenario.Parent
        if parent_scenario is None:
            return None
        return Scenario(self._scenario_manager, parent_scenario)

    @property
    def children(self) -> list["Scenario"]:
        """The child scenarios.

        Returns
        -------
        list of Scenario
            The child scenarios of this scenario
        """
        children = []
        for child in self._net_scenario.Children:
            children.append(Scenario(self._scenario_manager, child))
        return children

    @property
    def alternatives(self) -> list["Alternative"]:
        """The alternatives assigned to this scenario.

        Returns
        -------
        list of Alternative
            The alternatives assigned to this scenario
        """
        from .alternative import Alternative

        alternatives = []
        for alt in self._net_scenario.CurAlternatives:
            alternatives.append(Alternative(self._scenario_manager, alt))
        return alternatives

    @property
    def is_active(self) -> bool:
        """Whether this scenario is the currently active scenario.

        Returns
        -------
        bool
            True if this is the active scenario, False otherwise
        """
        active_scenario = self._scenario_manager.ActiveScenario
        if active_scenario is None:
            return False
        return active_scenario.Id == self._net_scenario.Id

    @property
    def is_base(self) -> bool:
        """Whether this is the base scenario.

        Returns
        -------
        bool
            True if this is the base scenario, False otherwise
        """
        return self._net_scenario.IsBase

    @property
    def comment(self) -> str:
        """The scenario's comment.

        Returns
        -------
        str
            The scenario comment
        """
        return str(self._net_scenario.Comment) if self._net_scenario.Comment else ""

    @comment.setter
    def comment(self, value: str) -> None:
        """Set the scenario comment.

        Parameters
        ----------
        value : str
            The new comment for the scenario
        """
        self._scenario_manager.SetComment(self._net_scenario, value)

    def activate(self) -> None:
        """Activate this scenario.

        Makes this scenario the currently active scenario in the model.
        This will affect which alternatives are used when accessing model data.

        Raises
        ------
        ValueError
            If the scenario could not be activated
        """
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
            If the alternative could not be set for this scenario
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

    def contains_alternative(self, alternative: "Alternative") -> bool:
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
