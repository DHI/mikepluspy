using System.CommandLine;
using MikePlusCli.Commands;

namespace MikePlusCli;

/// <summary>
/// MIKE+ CLI — a command-line interface for MIKE+ database operations.
///
/// Usage examples:
///   mikeplus database info --database model.sqlite
///   mikeplus table  select msm_Node --database model.sqlite --columns Diameter,InvertLevel
///   mikeplus table  insert msm_Node --database model.sqlite --set Diameter=1.5 --set MUID=N1
///   mikeplus scenario list --database model.sqlite
///   mikeplus run --database model.sqlite --engine CS_MIKE_1D
///
/// All commands produce structured JSON output suitable for scripting and AI agents.
/// </summary>
public static class Program
{
    public static async Task<int> Main(string[] args)
    {
        var root = new RootCommand("MIKE+ CLI — database operations for MIKE+ models")
        {
            DatabaseCommand.Build(),
            TableCommand.Build(),
            ScenarioCommand.Build(),
            AlternativeCommand.Build(),
            ToolCommand.Build(),
            RunCommand.Build(),
        };

        return await root.InvokeAsync(args);
    }
}
