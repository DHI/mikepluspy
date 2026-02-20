"""Package containing spatial analysis for MIKE+ geometries."""

import clr

clr.AddReference("DHI.Amelia.Infrastructure.Interface")
clr.AddReference("ThinkGeo.Core")

from .spatial_analysis_util import SpatialAnalysisUtil  # noqa: E402

__all__ = [
    "SpatialAnalysisUtil",
]
