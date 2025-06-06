"""
MIKE+ Python API - AlternativeGroupCollection class.

Collection-like access to alternative groups in the MIKE+ model.

Provides a Pythonic interface for accessing alternative groups in the MIKE+ model.
"""

from typing import Iterator, List
from .alternative_group import AlternativeGroup


class AlternativeGroupCollection:
    """Collection-like access to alternative groups.

    Provides a Pythonic interface for accessing and managing alternative groups.
    """

    def __init__(self, scenario_manager):
        """AlternativeGroupCollection constructor.

        Parameters
        ----------
        scenario_manager : IScenarioManager
            The underlying .NET scenario manager object
        """
        self._scenario_manager = scenario_manager

    def __getitem__(self, key: str) -> AlternativeGroup:
        """
        Get alternative group by ID or name.

        Parameters
        ----------
        key : str
            The ID or name of the group to find

        Returns
        -------
        AlternativeGroup
            The found alternative group

        Raises
        ------
        KeyError
            If no alternative group with the specified ID or name is found
        """
        if not isinstance(key, str):
            raise TypeError(
                f"Alternative group key must be a string, got {type(key).__name__}"
            )

        for group in self._scenario_manager.AlternativeGroups:
            if (
                group.Id == key
                or group.Name == key
                or group.Name.lower() == key.lower()
            ):
                return AlternativeGroup(self._scenario_manager, group)

        available_groups = [
            group.Name for group in self._scenario_manager.AlternativeGroups
        ]
        raise KeyError(
            f"No alternative group with ID or name '{key}' found. Available groups: {available_groups}"
        )

    def __iter__(self) -> Iterator[AlternativeGroup]:
        """Iterate through all alternative groups.

        Returns
        -------
        iterator
            Iterator over all alternative groups
        """
        for group in self._scenario_manager.AlternativeGroups:
            yield AlternativeGroup(self._scenario_manager, group)

    def group_names(self) -> List[str]:
        """Get a list of available group names.

        Returns
        -------
        list of str
            Names of all available alternative groups
        """
        return [group.Name for group in self._scenario_manager.AlternativeGroups]

    def by_table(self, table_name: str) -> AlternativeGroup:
        """
        Find the alternative group associated with a specific table.

        Parameters
        ----------
        table_name : str
            The table name to look for

        Returns
        -------
        AlternativeGroup
            The alternative group associated with the table

        Raises
        ------
        KeyError
            If no group is associated with the given table
        """
        for group in self._scenario_manager.AlternativeGroups:
            for table in group.Tables:
                if str(table).lower() == table_name.lower():
                    return AlternativeGroup(self._scenario_manager, group)

        raise KeyError(f"No alternative group associated with table '{table_name}'")
