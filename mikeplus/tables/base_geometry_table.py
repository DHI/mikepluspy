"""Base table class for MIKE+ database tables with a geometry."""
from __future__ import annotations

from .base_table import BaseTable
from .base_table_columns import BaseColumns # noqa: F401

class BaseGeometryTable(BaseTable):
    """Base class representing a database table with geometry."""

