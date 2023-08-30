import os.path
from DHI.Amelia.DomainServices.Services import AmeliaEngineService
from DHI.Amelia.DomainServices.Services import AmeliaDataService
from DHI.Amelia.GlobalUtility.DataType import MUSimulationOption
from DHI.Amelia.DataModule.Interface.Services import IMwProjectTable
from DHI.Amelia.Infrastructure.Interface.Entity import StatusInfoEventArgs
from System.Threading import CancellationTokenSource
from System.Collections.Generic import List
from System.Threading import Thread
from System import Environment
from DHI.Mike.Install import MikeImport, MikeProducts

class EPANET:
	def __init__(self,
				 dataTables):
		MikeImport.Setup(22, MikeProducts.MikePlus)
		self._dataTables = dataTables
		self._result_file = None
	
	def run_engine_epanet(self, 
			 simMuid=None):
		if simMuid == None:
			simMuid = self._get_active_muid()
			if simMuid == None:
				print("Simulation id can't be none.")
				return
		print("Simulation id is " + simMuid)
		data_service = AmeliaDataService()
		data_service.DataTables = self._dataTables
		engine_service = AmeliaEngineService()
		engine_service.DataTables = self._dataTables
		engine_service.DataService = data_service
		cancel_source = CancellationTokenSource()
		msg = List[str]()
		success = engine_service.RunEngine_AllEpanet(MUSimulationOption.WD_EPANET, cancel_source.Token, msg, None, None, None, simMuid, None, None)
		if self._result_file == None:
			self._result_file = self._get_result_file(simMuid)
		dir = os.path.dirname(os.path.abspath(self._result_file)) 
		file_name = os.path.splitext(os.path.split(self._result_file)[1])[0]
		log_file = os.path.join(dir, file_name + '.log')
		if self._print_log(log_file) is False:
			if (success == False):
				print("Simulation failed.")
			else:
				print("Simulation is finished without logFile generated.")
	
	def result_file(self):
		if self._result_file == None:
			simMuid = self._get_active_muid()
			self._result_file = self._get_result_file(simMuid)
		return self._result_file
	
	def _print_log(self, log_file):
		if os.path.exists(log_file):
			with open(log_file) as f:
				lines = f.readlines()
				for line in lines:
					print(line)
			return True
		else:
			return False
			
	def _get_result_file(self, simMuid):
		project = self._dataTables["mw_Project"]
		prj = IMwProjectTable(project)
		res_file = prj.GetEpanetResultFilePath(MUSimulationOption.WD_EPANET, None, simMuid)
		return os.path.abspath(res_file)
	
	def _get_active_muid(self):
		muid = self._dataTables["mw_Project"].GetMuidsWhere("ActiveProject=1")
		if muid == None and muid.Count == 0:
			return None
		return muid[0]