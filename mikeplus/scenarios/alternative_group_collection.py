"""
MIKE+ Python API - AlternativeGroupCollection class.

Collection-like access to alternative groups in the MIKE+ model.

Provides a Pythonic interface for accessing alternative groups in the MIKE+ model.
"""

from typing import Iterator, List
from .alternative_group import AlternativeGroup


class AlternativeGroupCollection:
    """Collection-like access to alternative groups.

    Provides access to alternative groups in the MIKE+ model with dictionary-like
    syntax and helper methods for finding groups by related criteria.

    Methods
    -------
    group_names() : list[str]
        Get a list of all group names
    by_table(table_name) : AlternativeGroup
        Find the group associated with a specific table

    Examples
    --------
    >>> # Access by name/ID
    >>> loads_group = db.scenarios.alternative_groups["Loads and boundaries data"]
    >>>
    >>> # Get all group names
    >>> group_names = db.scenarios.alternative_groups.group_names()
    >>> "Loads and boundaries data" in group_names
    >>>
    >>> # Find group by associated table
    >>> msm_group = db.scenarios.alternative_groups.by_table("msm_Link")
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
        """Get alternative group by ID or name.

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
        """Iterate through all alternative groups."""
        for group in self._scenario_manager.AlternativeGroups:
            yield AlternativeGroup(self._scenario_manager, group)

    def __repr__(self) -> str:
        """Return a string representation of the AlternativeGroupCollection."""
        return "<AlternativeGroupCollection>"

    def group_names(self) -> List[str]:
        """Get a list of available group names."""
        return [group.Name for group in self._scenario_manager.AlternativeGroups]

    def by_table(self, table_name: str) -> AlternativeGroup:
        """Find the alternative group associated with a specific table.

        Parameters
        ----------
        table_name : str
            The name of the table to find the group for (e.g. "msm_Link")

        Returns
        -------
        AlternativeGroup
            The alternative group associated with the given table

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
