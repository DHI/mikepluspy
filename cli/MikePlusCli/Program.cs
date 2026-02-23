using System.CommandLine;
using MikePlusCli.Commands;

namespace MikePlusCli;

/// <summary>
/// MIKE+ CLI — a workflow-oriented command-line interface backed by the
/// Amelia .NET engine.  Mirrors the capabilities of the MIKE+ GUI so that
/// every modeling task (creating a model, editing network data, running
/// simulations, post-processing) can be scripted or invoked by AI agents.
///
/// All commands emit structured JSON to stdout for machine consumption.
///
/// Usage examples
/// ──────────────
///   mikeplus model  create  -d model.sqlite --projection "PROJCS[…]" --srid 32632
///   mikeplus model  info    -d model.sqlite
///   mikeplus model  tables  -d model.sqlite
///
///   mikeplus edit select msm_Node -d model.sqlite --columns Diameter,InvertLevel
///   mikeplus edit insert msm_Node -d model.sqlite --set MUID=N1 --set Diameter=1.5
///   mikeplus edit update msm_Node -d model.sqlite --set Diameter=2.0 --where "MUID='N1'"
///   mikeplus edit delete msm_Node -d model.sqlite --where "MUID='N1'"
///
///   mikeplus scenario list     -d model.sqlite
///   mikeplus scenario create   -d model.sqlite --name "Climate 2050"
///   mikeplus scenario activate -d model.sqlite --name "Climate 2050"
///
///   mikeplus import epanet -d model.sqlite --file network.inp
///   mikeplus import swmm   -d model.sqlite --file drainage.inp
///   mikeplus import data   -d model.sqlite --config import_config.xml
///
///   mikeplus tool topo-repair      -d model.sqlite --snap-distance 0.1
///   mikeplus tool connection-repair -d model.sqlite
///   mikeplus tool interpolate nearest -d model.sqlite --target-table msm_Node …
///
///   mikeplus simulate -d model.sqlite --engine CS_MIKE_1D
/// </summary>
public static class Program
{
    public static async Task<int> Main(string[] args)
    {
        AmeliaContext.Bootstrap();

        var root = new RootCommand(
            "MIKE+ CLI — workflow-oriented command-line tool backed by the Amelia engine")
        {
            ModelCommand.Build(),
            EditCommand.Build(),
            ScenarioCommand.Build(),
            ImportCommand.Build(),
            ToolCommand.Build(),
            SimulateCommand.Build(),
        };

        return await root.InvokeAsync(args);
    }
}

