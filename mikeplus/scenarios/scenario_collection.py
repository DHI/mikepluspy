"""
MIKE+ Python API - ScenarioCollection class.

Collection-like access to scenarios in the MIKE+ model.
"""

from __future__ import annotations

from typing import Iterator

from .scenario import Scenario


class ScenarioCollection:
    """Collection-like access to scenarios in the database.

    Attributes
    ----------
    active : Scenario
        Currently active scenario
    base : Scenario
        Base scenario

    Methods
    -------
    find_by_name(name) : list[Scenario]
        Find scenarios by name (may return multiple)
    by_name(name) : Scenario or None
        Find first scenario that matches the given name
    find_by_id(id) : Scenario or None
        Find scenario by its exact ID
    create(name, id=None, parent=None) : Scenario
        Create a new child scenario
    delete(scenario) : None
        Delete a scenario from the database

    Examples
    --------
    >>> # Access by ID
    >>> scenario = db.scenarios["scenario_id"]
    >>>
    >>> # Get active scenario
    >>> active = db.scenarios.active
    >>>
    >>> # Create new scenario
    >>> new_scenario = db.scenarios.create("Future Development")
    """

    def __init__(self, scenario_manager):
        """ScenarioCollection constructor.

        Parameters
        ----------
        scenario_manager : IScenarioManager
            The underlying .NET scenario manager object
        """
        self._scenario_manager = scenario_manager

    def __repr__(self):
        """Get string representation of the ScenarioCollection object."""
        return f"ScenarioCollection <{len(list(self))}>"

    @property
    def active(self) -> Scenario:
        """Currently active scenario."""
        return Scenario(self._scenario_manager, self._scenario_manager.ActiveScenario)

    @property
    def base(self) -> Scenario:
        """Base scenario."""
        return Scenario(self._scenario_manager, self._scenario_manager.BaseScenario)

    def __getitem__(self, id: str) -> Scenario:
        """Access scenario by its ID.

        Raises
        ------
        KeyError
            If no scenario matches the given ID
        """
        scenario = self._scenario_manager.FindScenario(id)
        if scenario is None:
            raise KeyError(f"No scenario with ID '{id}' found")

        return Scenario(self._scenario_manager, scenario)

    def __iter__(self) -> Iterator[Scenario]:
        """Iterate through all scenarios."""
        for scenario_id in self._scenario_manager.GetScenarios():
            scenario = self._scenario_manager.FindScenarioByName(scenario_id)
            yield Scenario(self._scenario_manager, scenario)

    def find_by_name(self, name: str) -> list[Scenario]:
        """Find scenarios by name (may return multiple if names aren't unique).

        Parameters
        ----------
        name : str
            The name of the scenario to find

        Returns
        -------
        list[Scenario]
            List of scenarios that match the given name
        """
        scenario = self._scenario_manager.FindScenarioByName(name)
        if scenario is None:
            return []

        return [Scenario(self._scenario_manager, scenario)]

    def by_name(self, name: str) -> Scenario | None:
        """Find a scenario by name (returns the first match if multiple exist).

        Parameters
        ----------
        name : str
            The name of the scenario to find

        Returns
        -------
        Scenario or None
            The first scenario that matches the given name, or None if no match is found
        """
        scenario = self.find_by_name(name)
        return scenario[0] if scenario else None

    def find_by_id(self, id: str) -> Scenario | None:
        """Find a scenario by its exact ID (returns single item or None).

        Parameters
        ----------
        id : str
            The ID of the scenario to find

        Returns
        -------
        Scenario or None
            The scenario with the given ID, or None if no scenario with that ID exists
        """
        from .scenario import Scenario

        scenario = self._scenario_manager.FindScenario(id)
        if scenario is None:
            return None

        return Scenario(self._scenario_manager, scenario)

    def create(self, name: str, parent: Scenario | None = None) -> Scenario:
        """Create a new scenario, optionally as a child of another.

        Parameters
        ----------
        name : str
            Name for the new scenario
        parent : Scenario, optional
            Parent scenario (defaults to base scenario if None)

        Raises
        ------
        ValueError
            If the scenario could not be created
        """
        from .scenario import Scenario

        try:
            if parent is None:
                parent = self.base
            new_scenario = self._scenario_manager.CreateChildScenario(
                parent._net_scenario, None, name
            )
            if new_scenario is None:
                raise ValueError(
                    f"Failed to create scenario '{name}' - no scenario returned"
                )

            return Scenario(self._scenario_manager, new_scenario)
        except Exception as e:
            raise ValueError(
                f"Failed to create scenario '{name}'. Error: {str(e)}"
            ) from e

    def delete(self, scenario: Scenario | str) -> None:
        """Delete a scenario by object or id.

        Parameters
        ----------
        scenario : Scenario or str
            The scenario to delete (can be a Scenario object or its ID)

        Raises
        ------
        ValueError
            If the scenario could not be deleted
        KeyError
            If the scenario does not exist
        """
        # Get the ID depending on input type
        if isinstance(scenario, str):
            scenario_id = scenario
        else:
            scenario_id = scenario.id

        # Check if it's the base scenario
        base_scenario = self._scenario_manager.BaseScenario
        if scenario_id == base_scenario.Id:
            raise ValueError("Cannot delete the base scenario")

        # Find the scenario to ensure it exists
        if self._scenario_manager.FindScenario(scenario_id) is None:
            raise KeyError(f"No scenario with ID '{scenario_id}' found")

        # Delete the scenario
        self._scenario_manager.DeleteScenario(scenario_id)
