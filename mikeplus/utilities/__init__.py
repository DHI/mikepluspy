"""Package containing spatial analysis for MIKE+ geometries."""

import clr

clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("ThinkGeo.Core")


from .spatial_analysis_util import (
    get_nearest_river_at,
    get_nearest_river_chainage_at,
)

__all__ = [
    "get_nearest_river_at",
    "get_nearest_river_chainage_at",
]
