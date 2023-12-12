import os.path
from System.Collections.Generic import List
from DHI.Amelia.Tools.CatchmentProcessing import CatchmentSlope
from DHI.Generic.MikeZero import eumUnit


class CathSlopeLengthProcess:
    """This tool performs automatic estimation of slope and length for each catchment.
    """
    def __init__(self,
                 dataTables):
        self._dataTables = dataTables

    def run(self,
            catch_ids,
            line_layer,
            dem_layer,
            direction,
            min_slope=0.002,
            demUnitKey=1000,
            overwrite_exist=True):
        """Calculate the slope and length for each catchment and print progress information. 

        Parameters
        ----------
        catch_ids : string
            a array of cathment muids
        line_layer : string
            a slope shape file path
        dem_layer : string
            dem file path, can be dfs2 file path
        direction : int
            Downstream = 0, Upstream = 1
        min_slope : float, optional
            unit is one per one, by default 0.002
        demUnitKey : int, optional
            int type data, please check MIKE unit key, by default 1000
        overwrite_exist : bool, optional
            overwrite exist value or not, by default True
        """
        line_layer = os.path.abspath(line_layer)
        dem_layer = os.path.abspath(dem_layer)
        unit = eumUnit(demUnitKey)
        tool = CatchmentSlope(self._dataTables)
        warnings = List[str]()
        catch_list = List[str]()
        for selCatch in catch_ids:
            catch_list.Add(selCatch)
        tool.CalculateSlopeLength(catch_list, overwrite_exist, min_slope, direction, line_layer, dem_layer, 1, unit, warnings)
        tool.RuningProgress += self._on_tool_runing_progress

    def _on_tool_runing_progress(self, source, args):
        print(args.Msg)
