import os.path
import subprocess
from DHI.Mike.Install import MikeImport, MikeProducts


class Egnine1D:
    def __init__(self,
                 dataTables):
        MikeImport.Setup(22, MikeProducts.MikePlus)
        self._dataTables = dataTables
        self._result_file = None

    def run(self,
            simMuid=None):
        if simMuid is None:
            muid = self._dataTables["msm_Project"].GetMuidsWhere("ActiveProject=1")
            if muid is None and muid.Count == 0:
                print("Simulation id can't be none.")
                return
            simMuid = muid[0]

        product_info = MikeImport.ActiveProduct()
        mike1d_exec = os.path.join(product_info.InstallRoot, r'bin\x64', 'DHI.Mike1D.Application.exe')
        dbOrMuppFile = self._dataTables.DataSource.BaseFullPath
        dir = os.path.dirname(os.path.abspath(dbOrMuppFile))
        file = os.path.basename(dbOrMuppFile)
        file_name = file.split('.')[0]
        log_file = os.path.join(dir, file_name + '_' + simMuid + '.log')
        self._result_file = os.path.join(dir, file_name + '_' + simMuid + '.res1d')
        print("Simulation is started. Simulation id is '" + simMuid + "'")
        subprocess.run([mike1d_exec, str(dbOrMuppFile), "-simulationid=" + simMuid, "-logfilename=" + log_file])
        if self._print_log(log_file) is False:
            print("Simulation is finished without logFile generated.")

    def result_file(self):
        return self._result_file

    def _print_log(self, logFile):
        if os.path.exists(logFile):
            with open(logFile) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
            return True
        else:
            return False
