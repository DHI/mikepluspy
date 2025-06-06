"""
MIKE+ Python API - AlternativeGroup class.

Represents a group of alternatives in the MIKE+ model.

An alternative group contains alternatives for specific tables or model components.
Each group has a base alternative and potentially an active alternative.
"""

from __future__ import annotations
from typing import Iterator

from .alternative import Alternative


class AlternativeGroup:
    """Represents an alternative group with collection-like access to alternatives.

    Provides a Pythonic interface for accessing and managing alternatives within a group.
    """

    def __init__(self, scenario_manager, net_alternative_group):
        """AlternativeGroup constructor.

        Parameters
        ----------
        scenario_manager : IScenarioManager
            The underlying .NET scenario manager object
        net_alternative_group : IAlternativeGroup
            The .NET IAlternativeGroup object
        """
        self._scenario_manager = scenario_manager
        self._net_alternative_group = net_alternative_group

    @property
    def id(self) -> str:
        """The group's unique identifier.

        Returns
        -------
        str
            The group ID
        """
        return str(self._net_alternative_group.Id)

    @property
    def name(self) -> str:
        """The group's name.

        Returns
        -------
        str
            The group name
        """
        return str(self._net_alternative_group.Name)

    @property
    def tables(self) -> list[str]:
        """The database tables associated with this group.

        Returns
        -------
        list of str
            The table names associated with this group
        """
        tables = []
        for table in self._net_alternative_group.Tables:
            tables.append(str(table))
        return tables

    @property
    def base(self) -> Alternative:
        """The base alternative for this group.

        Returns
        -------
        Alternative
            The base alternative for this group
        """
        base_alt = self._scenario_manager.GetBaseAlternative(self.id)
        return Alternative(self._scenario_manager, base_alt)

    @property
    def active(self) -> Alternative:
        """The alternative assigned to the active scenario for this group.

        Returns
        -------
        Alternative
            The currently active alternative for this group
        """
        current_alt = self._scenario_manager.GetCurrentAlternative(self.id)
        return Alternative(self._scenario_manager, current_alt)

    def __getitem__(self, key: str | int) -> Alternative:
        """Access alternative by ID (int) or name (str).

        Parameters
        ----------
        key : str or int
            The alternative ID (int) or name (str)

        Returns
        -------
        Alternative
            The matching Alternative object

        Raises
        ------
        KeyError
            If no alternative matches the given key
        """
        for alt in self._net_alternative_group.Alternatives:
            if isinstance(key, int) and alt.AltId == key:
                return Alternative(self._scenario_manager, alt)
            elif isinstance(key, str) and alt.Name == key:
                return Alternative(self._scenario_manager, alt)

        raise KeyError(f"No alternative with ID or name '{key}' in group '{self.name}'")

    def __iter__(self) -> Iterator[Alternative]:
        """Iterate through all alternatives in this group.

        Returns
        -------
        iterator
            Iterator over all alternatives in this group
        """
        for alt in self._net_alternative_group.Alternatives:
            yield Alternative(self._scenario_manager, alt)

    def find_by_name(self, name: str) -> list[Alternative]:
        """
        Find alternatives by name (may return multiple if names aren't unique).

        Parameters
        ----------
        name : str
            The name to search for

        Returns
        -------
        list of Alternative
            A list of matching alternatives
        """
        matches = []
        for alt in self._net_alternative_group.Alternatives:
            if alt.Name == name:
                matches.append(Alternative(self._scenario_manager, alt))
        return matches

    def create(
        self, name: str, parent: Alternative | None = None
    ) -> Alternative:
        """
        Create a new alternative, optionally as a child of another.

        Parameters
        ----------
        name : str
            Name for the new alternative
        parent : Alternative, optional
            Optional parent alternative (defaults to base alternative if None)

        Returns
        -------
        Alternative
            The newly created Alternative

        Raises
        ------
        ValueError
            If the alternative could not be created
        """
        try:
            if parent is None:
                parent_alt = self._scenario_manager.GetBaseAlternative(self.id)
            else:
                parent_alt = parent._net_alternative

            new_alt = self._scenario_manager.CreateAlternative(parent_alt, name)
            if new_alt is None:
                raise ValueError(
                    f"Failed to create alternative '{name}' - no alternative returned"
                )

            return Alternative(self._scenario_manager, new_alt)

        except Exception as e:
            existing_names = [
                alt.Name for alt in self._net_alternative_group.Alternatives
            ]
            raise ValueError(
                f"Failed to create alternative '{name}'. Error: {str(e)}. "
                f"Group: {self.name}, Existing alternatives: {existing_names}"
            ) from e
