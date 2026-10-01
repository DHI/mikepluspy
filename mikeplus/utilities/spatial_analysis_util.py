"""Util to do spatial analysis for MIKE+ geometry data."""

from __future__ import annotations

from typing import TYPE_CHECKING

from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper
from ThinkGeo.Core import (
    BaseShape,
    GeographyUnit,
    PointShape,
)

if TYPE_CHECKING:
    from ..database import Database


def get_nearest_river_chainage_at(
    database: Database, x: float, y: float, tolorance: float
) -> list[str | float] | None:
    """Get the river and chainage nearest to a point.

    Parameters
    ----------
    database : Database
        An open database.
    x : float
        X coordinate of the point.
    y : float
        Y coordinate of the point.
    tolorance : float
        Search radius around the point.

    Returns
    -------
    list[str | float] | None
        `[river_name, chainage]` for the nearest point on the nearest river,
        or None if no river lies within the search radius.

    """
    river_id = database.tables.mrm_Branch._net_table.GetNearestMuid(
        x, y, tolorance, None, None
    )
    if river_id is not None:
        riverGeom = database.tables.mrm_Branch._net_table.GetGeometry(river_id)
        lineGeom = GeoAPIHelper.GetWKBIGeometry(riverGeom)
        lineShape = BaseShape.CreateShapeFromWellKnownData(lineGeom)
        pointshp = PointShape(x, y)
        locationPnt = lineShape.GetClosestPointTo(pointshp, GeographyUnit.Meter)
        river_name = database.tables.mrm_Branch._net_table.GetName(river_id)
        chainageMngr = database._data_table_container.GetChainageManager(
            "mrm_Branch", river_name
        )
        chainage = chainageMngr.GetChainageAt(locationPnt, tolorance)
        return [river_name, chainage]
    else:
        return None


def get_nearest_river_at(
    database: Database, x: float, y: float, tolorance: float
) -> str | None:
    """Get the name of the river nearest to a point.

    Parameters
    ----------
    database : Database
        An open database.
    x : float
        X coordinate of the point.
    y : float
        Y coordinate of the point.
    tolorance : float
        Search radius around the point.

    Returns
    -------
    str | None
        The river name, or None if no river lies within the search radius.

    """
    river_id = database.tables.mrm_Branch._net_table.GetNearestMuid(
        x, y, tolorance, None, None
    )
    river_name = database.tables.mrm_Branch._net_table.GetName(river_id)
    return river_name
