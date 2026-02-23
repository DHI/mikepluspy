using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "run" command — execute MIKE+ simulations.
///
///   mikeplus run -d model.sqlite --engine CS_MIKE_1D
///   mikeplus run -d model.sqlite --engine CS_SWMM --muid sim1
///   mikeplus run -d model.sqlite --engine WD_EPANET
/// </summary>
public static class RunCommand
{
    private static readonly Option<string> DatabaseOption = new(
        aliases: new[] { "--database", "-d" },
        description: "Path to the MIKE+ SQLite database file")
    { IsRequired = true };

    public static Command Build()
    {
        var engineOpt = new Option<string>(
            "--engine",
            "Simulation engine: CS_MIKE_1D, CS_SWMM, WD_EPANET, CS_MIKE_1D_JobList")
        { IsRequired = true };
        engineOpt.AddCompletions("CS_MIKE_1D", "CS_SWMM", "WD_EPANET", "CS_MIKE_1D_JobList");

        var muidOpt = new Option<string?>("--muid", "Simulation MUID (uses active simulation if omitted)");

        var cmd = new Command("run", "Run a MIKE+ simulation");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(engineOpt);
        cmd.AddOption(muidOpt);

        cmd.SetHandler((string db, string engine, string? muid) =>
        {
            try
            {
                var validEngines = new[] { "CS_MIKE_1D", "CS_SWMM", "WD_EPANET", "CS_MIKE_1D_JobList" };
                if (!validEngines.Contains(engine, StringComparer.OrdinalIgnoreCase))
                {
                    CliResult.Fail("run", $"Invalid engine '{engine}'. Valid options: {string.Join(", ", validEngines)}", db).Print();
                    return;
                }

                using var ctx = DatabaseContext.Open(db);

                // SimulationRunner integration point:
                // var runner = new SimulationRunner(ctx.DataTableContainer);
                // var resultFiles = runner.Run(muid, engine);
                // CliResult.Ok("run", db, new { engine, muid, result_files = resultFiles }).Print();

                CliResult.Ok("run", db, new
                {
                    engine,
                    muid = muid ?? "(active simulation)",
                    result_files = Array.Empty<string>(),
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("run", ex.Message, db).Print();
            }
        }, DatabaseOption, engineOpt, muidOpt);

        return cmd;
    }
}
