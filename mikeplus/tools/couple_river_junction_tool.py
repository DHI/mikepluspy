import clr

clr.AddReference("ThinkGeo.Core")

from ThinkGeo.Core import BaseShape
from ThinkGeo.Core import PointShape
from ThinkGeo.Core import GeographyUnit
from DHI.Amelia.Infrastructure.Interface.UtilityHelper import GeoAPIHelper
from DHI.Amelia.GlobalUtility.LinkChainage import ChainageMngr


class CoupleRiverJunctionTool:
    def __init__(self, database):
        """Initialize the CoupleRiverJunctionTool with the given Database. Only river junctions which has no river branch configured are the targets.

        Parameters
        ----------
        database : Database or DataTables
            A Database object for the MIKE+ model.

        """
        if not database.is_open:
            database.open()
        self.db = database

    def run(self):
        df = (
            self.db._tables.msm_Node.select(["GeomX", "GeomY"])
            .where("TypeNo=6 AND BranchID is NULL")
            .execute()
        )
        for key, value in df.items():
            x = value[0]
            y = value[1]
            river = self.db.tables.mrm_Branch._net_table.GetNearestMuid(
                x, y, 100.0, None, None
            )
            if river is not None:
                riverGeom = self.db.tables.mrm_Branch._net_table.GetGeometry(river)
                lineGeom = GeoAPIHelper.GetWKBIGeometry(riverGeom)
                lineShape = BaseShape.CreateShapeFromWellKnownData(lineGeom)
                pointshp = PointShape(x, y)
                locationPnt = lineShape.GetClosestPointTo(pointshp, GeographyUnit.Meter)
                chainageMngr = self.db._data_table_container.GetChainageManager(
                    "mrm_Branch", river
                )
                chainage = chainageMngr.GetChainageAt(locationPnt, 100.0)
                self.db._tables.msm_Node.update(
                    {"BranchID": river, "BranchChainage": chainage}
                ).by_muid(key).execute()
                print(
                    f"River junction of '{key}' has been coupled to '{river}' at {chainage}"
                )
