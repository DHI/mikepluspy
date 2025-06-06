"""MIKE+ Python API - Scenario Management Package.

This package provides a Pythonic interface to the MIKE+ scenario management system.
It offers familiar Python patterns for working with scenarios and alternatives,
following conventions consistent with the rest of the mikepluspy library.

Classes
-------
Scenario
    Represents a scenario in MIKE+ with its properties and relationships
Alternative
    Represents an alternative configuration for model components
AlternativeGroup
    Represents a group of alternatives for a specific model component
ScenarioCollection
    Collection-like access to scenarios with lookup methods
AlternativeGroupCollection
    Collection-like access to alternative groups with lookup methods

Examples
--------
>>> from mikeplus import open
>>> db = open("path/to/example.sqlite")
>>>
>>> # List all alternative groups
>>> for group in db.scenarios.alternative_groups:
...     print(f"{group.name}: {group.id}")
>>>
>>> # Find a specific alternative group
>>> network_group = db.scenarios.alternative_groups["CS Network data"]
>>>
>>> # Get active alternative in the group
>>> active_network = network_group.active
>>> print(f"Active network: {active_network.name}")
>>>
>>> # List all scenarios
>>> for scenario in db.scenarios:
...     print(f"{scenario.name}: {scenario.id}")
>>>
>>> # Activate a specific scenario
>>> scenario = db.scenarios.by_name("Future Development")
>>> scenario.activate()

Notes
-----
The scenario classes provide lightweight wrappers around the underlying .NET API.
They are designed to provide a Pythonic interface while maintaining direct access
to the full functionality of the MIKE+ scenario management system.
"""

from .scenario import Scenario
from .scenario_collection import ScenarioCollection
from .alternative import Alternative
from .alternative_group import AlternativeGroup
from .alternative_group_collection import AlternativeGroupCollection

__all__ = [
    "Scenario",
    "ScenarioCollection",
    "Alternative",
    "AlternativeGroup",
    "AlternativeGroupCollection",
]
