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

Notes
-----
This API is designed to provide a lightweight wrapper around the MIKE+ .NET
scenario management API, implementing Pythonic patterns for collection access
and property management.
"""

from .scenario import Scenario
from .alternative import Alternative
from .alternative_group import AlternativeGroup
from .scenario_collection import ScenarioCollection  
from .alternative_group_collection import AlternativeGroupCollection

__all__ = [
    "Scenario",
    "Alternative",
    "AlternativeGroup",
    "ScenarioCollection",
    "AlternativeGroupCollection"
]
