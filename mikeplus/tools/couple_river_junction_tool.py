"""Tools for coupling river junctions to river chainage locations."""

from mikeplus.utilities.spatial_analysis_util import SpatialAnalysisUtil


class CoupleRiverJunctionTool:
    """Tool for coupling river junction nodes to nearest river chainage locations.

    Only those river junction which is missing river chainage location will be mapulated by this tool.

    Parameters
    ----------
    database: Database object or DataTableContainer

    Examples
    --------
    >>>from mikeplus import Database
    >>>from mikeplus.tools.couple_river_junction_tool import CoupleRiverJunctionTool
    >>>db = Database("path/to/model.sqlite")
    >>>river_junction_couple_tool = CoupleRiverJunctionTool(db)
    >>>river_junction_couple_tool.run()
    >>>db.close()

    """

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
        """Run the river junction couple tool."""
        df = (
            self.db._tables.msm_Node.select(["GeomX", "GeomY"])
            .where("TypeNo=6 AND BranchID is NULL")
            .execute()
        )
        self.db._data_table_container.BeginTransaction()
        commit = True
        try:
            for key, value in df.items():
                x = value[0]
                y = value[1]
                river_chainage = SpatialAnalysisUtil.get_nearest_river_chainage_at(
                    self.db, x, y, 100.0
                )
                if river_chainage is not None:
                    river = river_chainage[0]
                    chainage = river_chainage[1]
                    self.db._tables.msm_Node.update(
                        {"BranchID": river, "BranchChainage": chainage}
                    ).by_muid(key).execute()
                    print(
                        f"River junction of '{key}' has been coupled to '{river}' at {chainage}"
                    )

        except RuntimeError as e:
            print(f"An error occurred: {e}")
            commit = False

        self.db._data_table_container.EndTransaction(commit)
