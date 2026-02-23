using System.CommandLine;
using DHI.Amelia.DomainServices.Interface.SharedEntity;
using DHI.Amelia.GlobalUtility.DataType;
using DHI.Amelia.Tools.EngineTool;

namespace MikePlusCli.Commands;

/// <summary>
/// The "simulate" command — run MIKE+ simulations through Amelia's EngineTool.
///
/// Supports every engine type available in the MIKE+ GUI:
///   • CS_MIKE_1D       — Collection System with MIKE 1D
///   • CS_SWMM           — Collection System with SWMM
///   • WD_EPANET          — Water Distribution with EPANET
///   • CS_MIKE_1D_JobList — Long-Term Statistics job-list mode
///
///   mikeplus simulate -d model.sqlite --engine CS_MIKE_1D
///   mikeplus simulate -d model.sqlite --engine WD_EPANET --muid MySim
///   mikeplus simulate -d model.sqlite --engine CS_SWMM
/// </summary>
public static class SimulateCommand
{
    public static Command Build()
    {
        var dbOpt = SharedOptions.Database();

        var engineOpt = new Option<string>(
            "--engine",
            "Simulation engine to use")
        { IsRequired = true };
        engineOpt.AddCompletions("CS_MIKE_1D", "CS_SWMM", "WD_EPANET", "CS_MIKE_1D_JobList");

        var muidOpt = new Option<string?>(
            "--muid",
            "Simulation MUID (uses the model's active simulation if omitted)");

        var cmd = new Command("simulate", "Run a MIKE+ simulation (EngineTool)");
        cmd.AddOption(dbOpt);
        cmd.AddOption(engineOpt);
        cmd.AddOption(muidOpt);

        cmd.SetHandler((string db, string engine, string? muid) =>
        {
            try
            {
                if (!Enum.TryParse<MUSimulationOption>(engine, ignoreCase: true, out var simOption))
                {
                    var valid = string.Join(", ", Enum.GetNames<MUSimulationOption>());
                    CliResult.Fail("simulate",
                        $"Invalid engine '{engine}'. Valid options: {valid}", db).Print();
                    return;
                }

                using var ctx = AmeliaContext.Open(db);

                var engineTool = new EngineTool { DataTables = ctx.DataTables };
                var launcher = new DhiEngineSimpleLauncher();
                var messages = new List<string>();

                bool success;
                List<string> resultFiles;

                switch (simOption)
                {
                    case MUSimulationOption.CS_MIKE_1D:
                        (success, launcher, messages) =
                            RunCS(engineTool, launcher, messages, muid);
                        break;

                    case MUSimulationOption.CS_SWMM:
                        (success, messages) =
                            RunSWMM(engineTool, launcher, messages, muid);
                        break;

                    case MUSimulationOption.WD_EPANET:
                        (success, messages) =
                            RunEpanet(engineTool, simOption, launcher, messages, muid);
                        break;

                    case MUSimulationOption.CS_MIKE_1D_JobList:
                        (success, launcher, messages) =
                            RunLtsJobList(engineTool, launcher, messages, muid);
                        break;

                    default:
                        CliResult.Fail("simulate", $"Unsupported engine: {engine}", db).Print();
                        return;
                }

                // Start the engine and wait for completion
                if (launcher != null)
                {
                    launcher.Start();
                    while (launcher.IsEngineRunning)
                        Thread.Sleep(500);
                }

                // Retrieve result file paths from the project table
                resultFiles = GetResultFiles(ctx, simOption, muid);

                CliResult.Ok("simulate", db, new
                {
                    engine,
                    muid = muid ?? ctx.ActiveSimulation,
                    success,
                    result_files = resultFiles,
                    messages,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("simulate", ex.Message, db).Print();
            }
        }, dbOpt, engineOpt, muidOpt);

        return cmd;
    }

    // ── Engine dispatch helpers ────────────────────────────────────────

    private static (bool, DhiEngineSimpleLauncher, List<string>) RunCS(
        EngineTool tool, DhiEngineSimpleLauncher launcher, List<string> messages, string? muid)
    {
        var (ok, l, m) = tool.RunEngine_CS(launcher, messages, muid ?? "");
        return (ok, l, new List<string>(m));
    }

    private static (bool, List<string>) RunSWMM(
        EngineTool tool, DhiEngineSimpleLauncher launcher, List<string> messages, string? muid)
    {
        var cts = new CancellationTokenSource();
        var (ok, m) = tool.RunEngine_AllSWMM(cts.Token, messages, launcher, muid ?? "");
        return (ok, new List<string>(m));
    }

    private static (bool, List<string>) RunEpanet(
        EngineTool tool, MUSimulationOption simOpt,
        DhiEngineSimpleLauncher launcher, List<string> messages, string? muid)
    {
        var cts = new CancellationTokenSource();
        var (ok, m) = tool.RunEngine_AllEpanet(simOpt, cts.Token, messages, launcher, muid ?? "");
        return (ok, new List<string>(m));
    }

    private static (bool, DhiEngineSimpleLauncher, List<string>) RunLtsJobList(
        EngineTool tool, DhiEngineSimpleLauncher launcher, List<string> messages, string? muid)
    {
        var (ok, l, m) = tool.RunEngine_LTS_JobList(launcher, messages, muid ?? "");
        return (ok, l, new List<string>(m));
    }

    private static List<string> GetResultFiles(AmeliaContext ctx, MUSimulationOption simOpt, string? muid)
    {
        try
        {
            // Determine which project table holds results
            var projectTable = simOpt switch
            {
                MUSimulationOption.CS_MIKE_1D => "msm_Project",
                MUSimulationOption.CS_MIKE_1D_JobList => "msm_Project",
                MUSimulationOption.CS_SWMM => "mss_Project",
                MUSimulationOption.WD_EPANET => "mw_Project",
                _ => "msm_Project",
            };

            var table = ctx.GetTable(projectTable);
            var files = table.GetResultFilePath(muid ?? "");
            return files?.Values.Cast<string>().ToList() ?? new List<string>();
        }
        catch
        {
            return new List<string>();
        }
    }
}
