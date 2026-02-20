"""Util to do spatial analysis for MIKE+ geometry data."""

from ThinkGeo.Core import BaseShape  # noqa: E402
from ThinkGeo.Core import PointShape  # noqa: E402
from ThinkGeo.Core import GeographyUnit  # noqa: E402
from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper  # noqa: E402


class SpatialAnalysisUtil:
    """Spatial analysis functions."""

    @staticmethod
    def get_nearest_river_chainage_at(database, x: float, y: float, tolorance: float):
        """Get the nearest river chainage location by a give (x,y) location.

        Parameters
        ----------
        database : Database or DataTables
        x : float
            x coordinate of target search location
        y : float
            y coordinate of target search location
        tolorance : float
            search radiu distance

        Returns
        -------
        [str, float]
            first value is the river name, second value is the chainage value

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

    @staticmethod
    def get_nearest_river_at(database, x: float, y: float, tolorance: float):
        """Get the nearest river name by a give (x,y) location.

        Parameters
        ----------
        database : Database or DataTables
        x : float
            x coordinate of target search location
        y : float
            y coordinate of target search location
        tolorance : float
            search radiu distance

        Returns
        -------
        str:
            river name

        """
        river_id = database.tables.mrm_Branch._net_table.GetNearestMuid(
            x, y, tolorance, None, None
        )
        river_name = database.tables.mrm_Branch._net_table.GetName(river_id)
        return river_name
