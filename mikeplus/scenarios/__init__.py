"""MIKE+ Python API - Scenario Management Package.

Scenario and alternative management functionality for MIKE+ models.
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
