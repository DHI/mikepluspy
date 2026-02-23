using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "import" command group — import external data into a MIKE+ model.
///
/// Wraps Amelia's bridge and import-engine classes to bring data from
/// EPANET .inp files, SWMM .inp files, and XML-configured import operations
/// (the same import wizard available in the MIKE+ GUI).
///
///   mikeplus import epanet -d model.sqlite --file network.inp
///   mikeplus import swmm   -d model.sqlite --file drainage.inp
///   mikeplus import data   -d model.sqlite --config import_config.xml
/// </summary>
public static class ImportCommand
{
    public static Command Build()
    {
        var cmd = new Command("import", "Import external data into the model (EPANET, SWMM, XML config)");
        cmd.AddCommand(BuildEpanet());
        cmd.AddCommand(BuildSwmm());
        cmd.AddCommand(BuildData());
        return cmd;
    }

    // ── import epanet ─────────────────────────────────────────────────

    private static Command BuildEpanet()
    {
        var dbOpt = SharedOptions.Database();
        var fileOpt = new Option<string>("--file", "Path to EPANET .inp file") { IsRequired = true };

        var cmd = new Command("epanet", "Import an EPANET network from an .inp file (via INPBridge)");
        cmd.AddOption(dbOpt);
        cmd.AddOption(fileOpt);

        cmd.SetHandler((string db, string file) =>
        {
            try
            {
                if (!File.Exists(file))
                {
                    CliResult.Fail("import epanet", $"File not found: {file}", db).Print();
                    return;
                }

                using var ctx = AmeliaContext.Open(db);

                // Use Amelia's INPBridge — same path the GUI follows
                var bridge = new DHI.Amelia.EPANETBridge.INPBridge(ctx.DataTables, null);
                var cts = new CancellationTokenSource();
                var result = bridge.Import(Path.GetFullPath(file), cts.Token);

                var messages = new List<string>();
                foreach (var msg in bridge.ErrorMsgs)
                    messages.Add(msg);

                CliResult.Ok("import epanet", db, new
                {
                    file = Path.GetFullPath(file),
                    success = result,
                    messages,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("import epanet", ex.Message, db).Print();
            }
        }, dbOpt, fileOpt);

        return cmd;
    }

    // ── import swmm ───────────────────────────────────────────────────

    private static Command BuildSwmm()
    {
        var dbOpt = SharedOptions.Database();
        var fileOpt = new Option<string>("--file", "Path to SWMM .inp file") { IsRequired = true };

        var cmd = new Command("swmm", "Import a SWMM model from an .inp file (via SWMMStorageBridge)");
        cmd.AddOption(dbOpt);
        cmd.AddOption(fileOpt);

        cmd.SetHandler((string db, string file) =>
        {
            try
            {
                if (!File.Exists(file))
                {
                    CliResult.Fail("import swmm", $"File not found: {file}", db).Print();
                    return;
                }

                using var ctx = AmeliaContext.Open(db);

                var bridge = new DHI.Amelia.SWMMBridge.SWMMStorageBridge(ctx.DataTables, null);
                var cts = new CancellationTokenSource();
                var result = bridge.Import(Path.GetFullPath(file), cts.Token);

                var messages = new List<string>();
                foreach (var msg in bridge.ErrorMsgs)
                    messages.Add(msg);

                CliResult.Ok("import swmm", db, new
                {
                    file = Path.GetFullPath(file),
                    success = result,
                    messages,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("import swmm", ex.Message, db).Print();
            }
        }, dbOpt, fileOpt);

        return cmd;
    }

    // ── import data ───────────────────────────────────────────────────

    private static Command BuildData()
    {
        var dbOpt = SharedOptions.Database();
        var configOpt = new Option<string>("--config", "Path to XML import configuration file") { IsRequired = true };

        var cmd = new Command("data", "Run the MIKE+ import wizard from an XML configuration (via ImportToolBase)");
        cmd.AddOption(dbOpt);
        cmd.AddOption(configOpt);

        cmd.SetHandler((string db, string config) =>
        {
            try
            {
                if (!File.Exists(config))
                {
                    CliResult.Fail("import data", $"Config file not found: {config}", db).Print();
                    return;
                }

                using var ctx = AmeliaContext.Open(db);

                // ImportToolBase + FunctionHelper — same as MIKE+ GUI import wizard
                var engine = new DHI.Amelia.Tools.ImportTool.ImportEngine.ImportToolBase(ctx.DataTables);
                engine.Load(config);

                // Ensure relative paths in the config are resolved
                var configDir = Path.GetDirectoryName(Path.GetFullPath(config)) ?? ".";
                DHI.Amelia.Tools.ImportTool.ImportEngine.FunctionHelper
                    .ChangeFilePathInConfigToAbsolute(engine, configDir);

                engine.Run();

                CliResult.Ok("import data", db, new
                {
                    config_file = Path.GetFullPath(config),
                    completed = true,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("import data", ex.Message, db).Print();
            }
        }, dbOpt, configOpt);

        return cmd;
    }
}
