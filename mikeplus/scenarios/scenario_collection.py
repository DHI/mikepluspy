"""
MIKE+ Python API - ScenarioCollection class.

Collection-like access to scenarios in the MIKE+ model.
"""

from __future__ import annotations

from typing import Iterator, TYPE_CHECKING

if TYPE_CHECKING:
    from .scenario import Scenario


class ScenarioCollection:
    """Collection-like access to scenarios in the database.

    Provides a Pythonic interface for accessing scenarios in the MIKE+ model.
    """

    def __init__(self, scenario_manager):
        """ScenarioCollection constructor.

        Parameters
        ----------
        scenario_manager : IScenarioManager
            The underlying .NET scenario manager object
        """
        self._scenario_manager = scenario_manager

    @property
    def active(self) -> Scenario:
        """Get the currently active scenario.

        Returns
        -------
        Scenario
            The currently active scenario
        """
        return Scenario(self._scenario_manager, self._scenario_manager.ActiveScenario)

    @property
    def base(self) -> Scenario:
        """Get the base scenario.

        Returns
        -------
        Scenario
            The base scenario
        """
        return Scenario(self._scenario_manager, self._scenario_manager.BaseScenario)

    def __getitem__(self, id: str) -> Scenario:
        """Access scenario by its ID.

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
        scenario = self._scenario_manager.FindScenario(id)
        if scenario is None:
            raise KeyError(f"No scenario with ID '{id}' found")

        return Scenario(self._scenario_manager, scenario)

    def __iter__(self) -> Iterator[Scenario]:
        """Iterate through all scenarios.

        Returns
        -------
        iterator
            Iterator over all scenarios
        """
        for scenario_id in self._scenario_manager.GetScenarios():
            scenario = self._scenario_manager.FindScenario(scenario_id)
            yield Scenario(self._scenario_manager, scenario)

    def find_by_name(self, name: str) -> list[Scenario]:
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
        scenario = self._scenario_manager.FindScenarioByName(name)
        if scenario is None:
            return []

        return [Scenario(self._scenario_manager, scenario)]

    def by_name(self, name: str) -> Scenario | None:
        """
        Find a scenario by name (returns the first match if multiple exist).

        Parameters
        ----------
        name : str
            The name to search for

        Returns
        -------
        Scenario or None
            The first matching scenario or None if not found
        """
        scenario = self.find_by_name(name)
        return scenario[0] if scenario else None

    def find_by_id(self, id: str) -> Scenario | None:
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
        from .scenario import Scenario

        scenario = self._scenario_manager.FindScenario(id)
        if scenario is None:
            return None

        return Scenario(self._scenario_manager, scenario)

    def create(self, name: str, parent: Scenario) -> Scenario:
        """
        Create a new child scenario.

        Parameters
        ----------
        name : str
            Name for the new scenario
        parent : Scenario
            The parent scenario

        Returns
        -------
        Scenario
            The newly created Scenario

        Raises
        ------
        ValueError
            If the scenario could not be created
        """
        from .scenario import Scenario

        try:
            # Generate a unique ID automatically by using None as first param
            new_scenario = self._scenario_manager.CreateChildScenario(
                parent._net_scenario, None, name, True
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
