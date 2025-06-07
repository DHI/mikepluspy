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
        return f"Alternative <{self.name}>"

    @property
    def id(self) -> int:
        """The alternative's unique identifier.

        Returns
        -------
        int
            The alternative ID
        """
        return int(self._net_alternative.AltId)

    @property
    def name(self) -> str:
        """The alternative's name.

        Returns
        -------
        str
            The alternative name
        """
        return str(self._net_alternative.Name)

    @name.setter
    def name(self, value: str) -> None:
        """Set the alternative name.

        Parameters
        ----------
        value : str
            The new name for the alternative

        Raises
        ------
        ValueError
            If the alternative name could not be changed
        """
        if not self._scenario_manager.RenameAlternative(self._net_alternative, value):
            raise ValueError(f"Failed to rename alternative to '{value}'.")

    @property
    def group(self) -> AlternativeGroup:
        """The alternative group this alternative belongs to.

        Returns
        -------
        AlternativeGroup
            The alternative group
        """
        from .alternative_group import AlternativeGroup

        return AlternativeGroup(self._scenario_manager, self._net_alternative.Group)

    @property
    def parent(self) -> Alternative | None:
        """The parent alternative.

        Returns
        -------
        Alternative or None
            The parent alternative or None if this is the base alternative
        """
        parent = self._net_alternative.Parent
        if parent is None:
            return None
        return Alternative(self._scenario_manager, parent)

    @property
    def children(self) -> list["Alternative"]:
        """The child alternatives.

        Returns
        -------
        list of Alternative
            The child alternatives of this alternative
        """
        children = []
        for child in self._net_alternative.Children:
            children.append(Alternative(self._scenario_manager, child))
        return children

    @property
    def is_active(self) -> bool:
        """Whether this alternative is part of the active scenario.

        Returns
        -------
        bool
            True if this alternative is part of the active scenario, False otherwise
        """
        return self._net_alternative.IsActive

    @property
    def is_base(self) -> bool:
        """Whether this alternative is the base alternative for its group.

        Returns
        -------
        bool
            True if this is the base alternative, False otherwise
        """
        return self._net_alternative.IsBase

    @property
    def comment(self) -> str:
        """The alternative's comment.

        Returns
        -------
        str
            The alternative comment
        """
        return (
            str(self._net_alternative.Comment) if self._net_alternative.Comment else ""
        )

    @comment.setter
    def comment(self, value: str) -> None:
        """Set the alternative comment.

        Parameters
        ----------
        value : str
            The new comment for the alternative
        """
        self._scenario_manager.SetComment(self._net_alternative, value)

    @property
    def scenarios(self) -> list["Scenario"]:
        """The scenarios that use this alternative.

        Returns
        -------
        list of Scenario
            The scenarios that use this alternative
        """
        from .scenario import Scenario

        scenarios = []
        for scenario_id in self._scenario_manager.GetScenarios():
            scenario = self._scenario_manager.FindScenario(scenario_id)
            for alt in scenario.CurAlternatives:
                if alt.AltId == self._net_alternative.AltId:
                    scenarios.append(Scenario(self._scenario_manager, scenario))
                    break

        return scenarios
