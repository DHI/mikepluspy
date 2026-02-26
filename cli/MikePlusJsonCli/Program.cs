using System.Text.Json;
using System.Text.Json.Nodes;
using MikePlusJsonCli.Handlers;

namespace MikePlusJsonCli;

/// <summary>
/// Entry point for the MIKE+ JSON streaming CLI.
///
/// The process reads Newline-Delimited JSON (NDJSON) from stdin — one command
/// object per line — dispatches each command to the registered handler, and
/// writes a corresponding NDJSON result to stdout.  A single process handles
/// an entire workflow, so the Amelia assemblies and the database are loaded
/// only once regardless of how many commands are issued.
///
/// Usage
/// ─────
///   echo '{"command":"model.info","database":"model.sqlite"}' | mikeplus-json
///   cat workflow.ndjson | mikeplus-json
///   generate_nodes.py   | mikeplus-json
/// </summary>
public static class Program
{
    public static async Task<int> Main(string[] args)
    {
        // One-time: locate the MIKE+ installation and register the assembly resolver.
        AmeliaContext.Bootstrap();

        // Build the dispatcher with all known command handlers.
        var dispatcher = new CommandDispatcher()
            .Register(new ModelOpenHandler())
            .Register(new ModelCloseHandler())
            .Register(new ModelCreateHandler())
            .Register(new ModelInfoHandler())
            .Register(new ModelTablesHandler())
            .Register(new EditSelectHandler())
            .Register(new EditInsertHandler())
            .Register(new EditUpdateHandler())
            .Register(new EditDeleteHandler())
            .Register(new ScenarioListHandler())
            .Register(new ScenarioCreateHandler())
            .Register(new ScenarioDeleteHandler())
            .Register(new ScenarioActivateHandler())
            .Register(new ScenarioAlternativeListHandler())
            .Register(new ScenarioAlternativeSetHandler())
            .Register(new ImportEpanetHandler())
            .Register(new ImportSwmmHandler())
            .Register(new ImportDataHandler())
            .Register(new ToolTopoRepairHandler())
            .Register(new ToolConnectionRepairHandler())
            .Register(new ToolInterpolateHandler())
            .Register(new ToolCatchmentProcessHandler())
            .Register(new SimulateRunHandler());

        // One shared session holds all open AmeliaContexts for this process lifetime.
        using var session = new Session();

        string? line;
        while ((line = await Console.In.ReadLineAsync()) is not null)
        {
            line = line.Trim();
            if (line.Length == 0) continue; // skip blank lines

            JsonObject response;
            string? commandId = null;
            string? commandName = null;
            bool abortOnError = false;

            try
            {
                var cmd = JsonNode.Parse(line) as JsonObject
                    ?? throw new InvalidOperationException("Command must be a JSON object.");

                commandId   = cmd["id"]?.GetValue<string>();
                commandName = cmd["command"]?.GetValue<string>()
                    ?? throw new InvalidOperationException("Missing required field 'command'.");
                abortOnError = cmd["on_error"]?.GetValue<string>() == "abort";

                response = await dispatcher.DispatchAsync(cmd, session);
                response["id"]      = commandId;
                response["status"]  = "ok";
                response["command"] = commandName;
            }
            catch (Exception ex)
            {
                response = new JsonObject
                {
                    ["id"]      = commandId,
                    ["status"]  = "error",
                    ["command"] = commandName,
                    ["error"]   = ex.Message,
                };

                // Write the error immediately before deciding whether to abort.
                Console.WriteLine(response.ToJsonString());
                await Console.Out.FlushAsync();

                if (abortOnError) return 1;
                continue;
            }

            Console.WriteLine(response.ToJsonString());
            await Console.Out.FlushAsync();
        }

        return 0;
    }
}
