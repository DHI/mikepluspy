"""Tables of MIKE+ database.

This package contains the base table classes and the auto-generated table classes.
"""

from . import auto_generated
from .auto_generated import *
from .base_geometry_table import BaseGeometryTable
from .base_node_table import BaseNodeTable
from .base_table import BaseTable
from .base_table_collection import BaseTableCollection
from .base_table_columns import BaseColumns

__all__ = [
    "BaseColumns",
    "BaseGeometryTable",
    "BaseNodeTable",
    "BaseTable",
    "BaseTableCollection",
] + auto_generated.__all__
