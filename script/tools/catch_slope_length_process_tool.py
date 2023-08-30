import os.path
from System.Collections.Generic import List
from DHI.Amelia.Tools.CatchmentProcessing import CatchmentSlope
from DHI.Generic.MikeZero import eumUnit

class CathSlopeLengthProcess:
	def __init__(self,
				 dataTables):
		self._dataTables = dataTables
		
	'''
	lineLayer: a slope shape file path
	demLayer: dem file path, can be dfs2 file path
	direction: Downstream = 0, Upstream = 1
	minSlope: unit is one per one
	demUnitKey: int type data, please check MIKE unit key
	'''
	def run(self,
			 catch_ids,
			 line_layer,
			 dem_layer,
			 direction,
			 min_slope=0.002,
			 demUnitKey=1000,
			 overwrite_exist=True):
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