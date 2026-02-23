using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "alternative" command group — manage alternatives and alternative groups.
///
///   mikeplus alternative groups    -d model.sqlite
///   mikeplus alternative list      -d model.sqlite --group-id HD
///   mikeplus alternative create    -d model.sqlite --name "Alt A" --group-id HD
///   mikeplus alternative set       -d model.sqlite --scenario-id S1 --alternative-id 5 --group-id HD
/// </summary>
public static class AlternativeCommand
{
    private static readonly Option<string> DatabaseOption = new(
        aliases: new[] { "--database", "-d" },
        description: "Path to the MIKE+ SQLite database file")
    { IsRequired = true };

    public static Command Build()
    {
        var cmd = new Command("alternative", "Manage alternatives and alternative groups");
        cmd.AddCommand(BuildGroups());
        cmd.AddCommand(BuildList());
        cmd.AddCommand(BuildCreate());
        cmd.AddCommand(BuildSet());
        return cmd;
    }

    // ── alternative groups ────────────────────────────────────────────

    private static Command BuildGroups()
    {
        var cmd = new Command("groups", "List all alternative groups");
        cmd.AddOption(DatabaseOption);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                var rows = ctx.ListAlternativeGroups();
                CliResult.Ok("alternative groups", db, new { count = rows.Count, groups = rows }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("alternative groups", ex.Message, db).Print();
            }
        }, DatabaseOption);

        return cmd;
    }

    // ── alternative list ──────────────────────────────────────────────

    private static Command BuildList()
    {
        var groupOpt = new Option<string?>("--group-id", "Filter by alternative group ID");

        var cmd = new Command("list", "List alternatives (optionally filtered by group)");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(groupOpt);

        cmd.SetHandler((string db, string? groupId) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                var rows = ctx.ListAlternatives(groupId);
                CliResult.Ok("alternative list", db, new { count = rows.Count, alternatives = rows }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("alternative list", ex.Message, db).Print();
            }
        }, DatabaseOption, groupOpt);

        return cmd;
    }

    // ── alternative create ────────────────────────────────────────────

    private static Command BuildCreate()
    {
        var nameOpt = new Option<string>("--name", "Name for the new alternative") { IsRequired = true };
        var groupOpt = new Option<string>("--group-id", "Alternative group to add to") { IsRequired = true };
        var parentOpt = new Option<int?>("--parent-id", "Parent alternative ID");
        var commentOpt = new Option<string?>("--comment", "Optional description");

        var cmd = new Command("create", "Create a new alternative within a group");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(nameOpt);
        cmd.AddOption(groupOpt);
        cmd.AddOption(parentOpt);
        cmd.AddOption(commentOpt);

        cmd.SetHandler((string db, string name, string groupId, int? parentId, string? comment) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                var id = ctx.CreateAlternative(name, groupId, parentId, comment);
                CliResult.Ok("alternative create", db, new { alternative_id = id, name, group_id = groupId }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("alternative create", ex.Message, db).Print();
            }
        }, DatabaseOption, nameOpt, groupOpt, parentOpt, commentOpt);

        return cmd;
    }

    // ── alternative set ───────────────────────────────────────────────

    private static Command BuildSet()
    {
        var scenarioOpt = new Option<string>("--scenario-id", "Scenario to assign the alternative to") { IsRequired = true };
        var altOpt = new Option<int>("--alternative-id", "Alternative ID to assign") { IsRequired = true };
        var groupOpt = new Option<string>("--group-id", "Alternative group ID") { IsRequired = true };

        var cmd = new Command("set", "Assign an alternative to a scenario for a given group");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(scenarioOpt);
        cmd.AddOption(altOpt);
        cmd.AddOption(groupOpt);

        cmd.SetHandler((string db, string scenarioId, int altId, string groupId) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                ctx.SetScenarioAlternative(scenarioId, altId, groupId);
                CliResult.Ok("alternative set", db, new
                {
                    scenario_id = scenarioId,
                    alternative_id = altId,
                    group_id = groupId,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("alternative set", ex.Message, db).Print();
            }
        }, DatabaseOption, scenarioOpt, altOpt, groupOpt);

        return cmd;
    }
}
