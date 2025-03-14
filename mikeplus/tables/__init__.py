"""
Tables of MIKE+ database.

This package contains the base table classes and the auto-generated table classes.
"""
from .base_table import BaseTable
from .base_table_collection import BaseTableCollection
from .auto_generated import __all__ as auto_generated_all

__all__ = ["BaseTable", "BaseTableCollection"] + auto_generated_all
