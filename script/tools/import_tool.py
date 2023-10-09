import os.path
from DHI.Amelia.Tools.ImportTool.ImportEngine import FunctionHelper
from DHI.Amelia.Tools.ImportTool.ImportEngine import ImportToolBase


class ImportTool:
    def __init__(self,
                 configFile,
                 dataTables=None):
        self._configFile = os.path.abspath(configFile)
        self._dataTables = dataTables

    def run(self):
        import_engine = ImportToolBase(self._dataTables)
        import_engine.Load(self._configFile)
        FunctionHelper.ChangeFilePathInConfigToAbsolute(import_engine.JobConfigSectionsDic, self._configFile)
        import_engine.OnTableDataProcessing += self._on_table_data_processing
        import_engine.Run()

    def _on_table_data_processing(self, source, args):
        print(args.TileInfo)
