"""
MIKE+ Python API - AlternativeGroup class.

Represents a group of alternatives in the MIKE+ model.

An alternative group contains alternatives for specific tables or model components.
Each group has a base alternative and potentially an active alternative.
"""

from __future__ import annotations
from typing import Iterator

from .alternative import Alternative
from mikeplus.scenarios import alternative


class AlternativeGroup:
    """Represents an alternative group with collection-like access to alternatives.

    An alternative group contains alternatives for specific tables or model components.
    Each group has a base alternative and potentially an active alternative.

    Attributes
    ----------
    id : str
        Unique identifier for the group
    name : str
        Name of the group
    tables : list[str]
        Database tables associated with this group
    base : Alternative
        Base alternative for this group
    active : Alternative
        Currently active alternative for this group

    Examples
    --------
    >>> network_group = db.scenarios.alternative_groups["CS Network data"]
    >>> print(f"Tables: {network_group.tables}")
    >>> print(f"Active: {network_group.active.name}")
    >>> print(f"Base: {network_group.base.name}")
    >>>
    >>> # Create a new alternative
    >>> new_alt = network_group.create("My Network", parent=network_group.base)
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
        """Group's unique identifier."""
        return str(self._net_alternative_group.Id)

    @property
    def name(self) -> str:
        """Group's name."""
        return str(self._net_alternative_group.Name)

    @property
    def tables(self) -> list[str]:
        """Database tables associated with this group."""
        tables = []
        for table in self._net_alternative_group.Tables:
            tables.append(str(table))
        return tables

    @property
    def base(self) -> Alternative:
        """Base alternative for this group."""
        base_alt = self._net_alternative_group.BaseAlternative
        return Alternative(self._scenario_manager, base_alt)

    @property
    def active(self) -> Alternative:
        """Alternative assigned to the active scenario for this group."""
        current_alt = self._net_alternative_group.ActiveAlternative
        return Alternative(self._scenario_manager, current_alt)

    def __repr__(self) -> str:
        """Return a string representation of the AlternativeGroup."""
        return f"<AlternativeGroup {self.name}>"

    def __iter__(self) -> Iterator[Alternative]:
        """Iterate through all alternatives in this group."""
        yield self.base
        for child in self.base.children:
            yield child

    def _find_by_name(self, name: str, parent: IAlternative, found: list[IAlternative]) -> None:
        if name == parent.Name:
            found.append(parent)
        if parent.Children.Count == 0:
            return
        for child in parent.Children:
            self._find_by_name(name, child, found)

    def find_by_name(self, name: str) -> list[Alternative]:
        """Find alternatives by name."""
        found = []
        base = self._net_alternative_group.BaseAlternative
        self._find_by_name(name, base, found)
        return [Alternative(self._scenario_manager, alt) for alt in found]

    def by_name(self, name: str) -> Alternative | None:
        """Find an alternative by name."""
        found = self.find_by_name(name)
        return found[0] if found else None     

    def create(self, name: str, parent: Alternative | None = None) -> Alternative:
        """Create a new alternative, optionally as a child of another.

        Parameters
        ----------
        name : str
            Name for the new alternative
        parent : Alternative, optional
            Parent alternative (defaults to base alternative if None)

        Raises
        ------
        ValueError
            If the alternative could not be created
        """
        try:
            if parent is None:
                parent_alt = self._net_alternative_group.BaseAlternative
            else:
                parent_alt = parent._net_alternative

            new_alt = self._scenario_manager.CreateAlternative(parent_alt, name)
            if new_alt is None:
                raise ValueError(
                    f"Failed to create alternative '{name}' - no alternative returned"
                )

            return Alternative(self._scenario_manager, new_alt)

        except Exception as e:
            existing_names = [alt.Name for alt in self._scenario_manager.Alternatives]
            raise ValueError(
                f"Failed to create alternative '{name}'. Error: {str(e)}. "
                f"Group: {self.name}, Existing alternatives: {existing_names}"
            ) from e
