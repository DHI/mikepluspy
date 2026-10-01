"""Tables of MIKE+ database.

This package contains the base table classes and the auto-generated table classes.
"""

from . import auto_generated
from .base_geometry_table import BaseGeometryTable
from .base_table import BaseTable
from .base_table_collection import BaseTableCollection

__all__ = [
    "BaseGeometryTable",
    "BaseTable",
    "BaseTableCollection",
] + auto_generated.__all__
