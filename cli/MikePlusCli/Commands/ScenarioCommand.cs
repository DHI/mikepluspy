using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "scenario" command group — manage scenarios and alternatives through
/// Amelia's <c>IScenarioManager</c>.
///
/// MIKE+ models support a hierarchy of scenarios, each referencing a set
/// of alternatives (one per alternative group).  This mirrors the Scenario
/// Manager panel in the MIKE+ GUI.
///
///   mikeplus scenario list     -d model.sqlite
///   mikeplus scenario create   -d model.sqlite --name "Climate 2050" --parent "Base"
///   mikeplus scenario delete   -d model.sqlite --name "Climate 2050"
///   mikeplus scenario activate -d model.sqlite --name "Climate 2050"
///
///   mikeplus scenario alternative groups -d model.sqlite
///   mikeplus scenario alternative list   -d model.sqlite --group HD
///   mikeplus scenario alternative create -d model.sqlite --group HD --name "Alt A"
///   mikeplus scenario alternative set    -d model.sqlite --scenario "Climate 2050" --group HD --name "Alt A"
/// </summary>
public static class ScenarioCommand
{
    public static Command Build()
    {
        var cmd = new Command("scenario", "Manage scenarios and alternatives (Amelia ScenarioManager)");
        cmd.AddCommand(BuildList());
        cmd.AddCommand(BuildCreate());
        cmd.AddCommand(BuildDelete());
        cmd.AddCommand(BuildActivate());
        cmd.AddCommand(BuildAlternativeGroup());
        return cmd;
    }

    // ── scenario list ─────────────────────────────────────────────────

    private static Command BuildList()
    {
        var dbOpt = SharedOptions.Database();

        var cmd = new Command("list", "List all scenarios (name, parent, active status)");
        cmd.AddOption(dbOpt);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;
                var scenarios = new List<object>();

                foreach (var sc in mgr.GetScenarios())
                {
                    scenarios.Add(new
                    {
                        id = sc.Id,
                        name = sc.Name,
                        parent = sc.Parent?.Name,
                        is_base = sc.IsBase,
                        is_active = (sc.Id == mgr.ActiveScenario.Id),
                        comment = sc.Comment,
                    });
                }

                CliResult.Ok("scenario list", db, new { count = scenarios.Count, scenarios }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario list", ex.Message, db).Print();
            }
        }, dbOpt);

        return cmd;
    }

    // ── scenario create ───────────────────────────────────────────────

    private static Command BuildCreate()
    {
        var dbOpt = SharedOptions.Database();
        var nameOpt = new Option<string>("--name", "Name for the new scenario") { IsRequired = true };
        var parentOpt = new Option<string?>("--parent", "Parent scenario name (default: base scenario)");

        var cmd = new Command("create", "Create a child scenario");
        cmd.AddOption(dbOpt);
        cmd.AddOption(nameOpt);
        cmd.AddOption(parentOpt);

        cmd.SetHandler((string db, string name, string? parent) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;

                var parentScenario = parent != null
                    ? mgr.FindScenarioByName(parent)
                    : mgr.BaseScenario;

                if (parentScenario == null)
                {
                    CliResult.Fail("scenario create", $"Parent scenario '{parent}' not found.", db).Print();
                    return;
                }

                var newScenario = mgr.CreateChildScenario(parentScenario, name);
                CliResult.Ok("scenario create", db, new
                {
                    id = newScenario.Id,
                    name = newScenario.Name,
                    parent = parentScenario.Name,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario create", ex.Message, db).Print();
            }
        }, dbOpt, nameOpt, parentOpt);

        return cmd;
    }

    // ── scenario delete ───────────────────────────────────────────────

    private static Command BuildDelete()
    {
        var dbOpt = SharedOptions.Database();
        var nameOpt = new Option<string>("--name", "Scenario name to delete") { IsRequired = true };

        var cmd = new Command("delete", "Delete a scenario (base scenario cannot be deleted)");
        cmd.AddOption(dbOpt);
        cmd.AddOption(nameOpt);

        cmd.SetHandler((string db, string name) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;

                var scenario = mgr.FindScenarioByName(name);
                if (scenario == null)
                {
                    CliResult.Fail("scenario delete", $"Scenario '{name}' not found.", db).Print();
                    return;
                }

                if (scenario.IsBase)
                {
                    CliResult.Fail("scenario delete", "Cannot delete the base scenario.", db).Print();
                    return;
                }

                mgr.DeleteScenario(scenario);
                CliResult.Ok("scenario delete", db, new { name, deleted = true }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario delete", ex.Message, db).Print();
            }
        }, dbOpt, nameOpt);

        return cmd;
    }

    // ── scenario activate ─────────────────────────────────────────────

    private static Command BuildActivate()
    {
        var dbOpt = SharedOptions.Database();
        var nameOpt = new Option<string>("--name", "Scenario name to make active") { IsRequired = true };

        var cmd = new Command("activate", "Set a scenario as the active scenario");
        cmd.AddOption(dbOpt);
        cmd.AddOption(nameOpt);

        cmd.SetHandler((string db, string name) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;

                var scenario = mgr.FindScenarioByName(name);
                if (scenario == null)
                {
                    CliResult.Fail("scenario activate", $"Scenario '{name}' not found.", db).Print();
                    return;
                }

                mgr.ActivateScenario(scenario);
                CliResult.Ok("scenario activate", db, new { name, activated = true }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario activate", ex.Message, db).Print();
            }
        }, dbOpt, nameOpt);

        return cmd;
    }

    // ── scenario alternative (sub-group) ──────────────────────────────

    private static Command BuildAlternativeGroup()
    {
        var cmd = new Command("alternative", "Manage alternatives within alternative groups");
        cmd.AddCommand(BuildAltGroups());
        cmd.AddCommand(BuildAltList());
        cmd.AddCommand(BuildAltCreate());
        cmd.AddCommand(BuildAltSet());
        return cmd;
    }

    private static Command BuildAltGroups()
    {
        var dbOpt = SharedOptions.Database();

        var cmd = new Command("groups", "List all alternative groups");
        cmd.AddOption(dbOpt);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;
                var groups = new List<object>();

                foreach (var grp in mgr.AlternativeGroups)
                {
                    var tables = new List<string>();
                    foreach (var t in grp.Tables)
                        tables.Add(t);

                    groups.Add(new
                    {
                        id = grp.Id,
                        name = grp.Name,
                        base_alternative = grp.BaseAlternative?.Name,
                        active_alternative = grp.ActiveAlternative?.Name,
                        tables,
                    });
                }

                CliResult.Ok("scenario alternative groups", db,
                    new { count = groups.Count, groups }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario alternative groups", ex.Message, db).Print();
            }
        }, dbOpt);

        return cmd;
    }

    private static Command BuildAltList()
    {
        var dbOpt = SharedOptions.Database();
        var groupOpt = new Option<string>("--group", "Alternative group name or ID") { IsRequired = true };

        var cmd = new Command("list", "List alternatives within a group");
        cmd.AddOption(dbOpt);
        cmd.AddOption(groupOpt);

        cmd.SetHandler((string db, string group) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;
                var grp = FindGroup(mgr, group);

                if (grp == null)
                {
                    CliResult.Fail("scenario alternative list",
                        $"Alternative group '{group}' not found.", db).Print();
                    return;
                }

                var alts = new List<object>();
                foreach (var alt in grp)
                {
                    alts.Add(new
                    {
                        id = alt.AltId,
                        name = alt.Name,
                        parent = alt.Parent?.Name,
                        is_base = alt.IsBase,
                        is_active = alt.IsActive,
                        comment = alt.Comment,
                    });
                }

                CliResult.Ok("scenario alternative list", db,
                    new { group = grp.Name, count = alts.Count, alternatives = alts }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario alternative list", ex.Message, db).Print();
            }
        }, dbOpt, groupOpt);

        return cmd;
    }

    private static Command BuildAltCreate()
    {
        var dbOpt = SharedOptions.Database();
        var groupOpt = new Option<string>("--group", "Alternative group name or ID") { IsRequired = true };
        var nameOpt = new Option<string>("--name", "Name for the new alternative") { IsRequired = true };
        var parentOpt = new Option<string?>("--parent", "Parent alternative name");

        var cmd = new Command("create", "Create a new alternative within a group");
        cmd.AddOption(dbOpt);
        cmd.AddOption(groupOpt);
        cmd.AddOption(nameOpt);
        cmd.AddOption(parentOpt);

        cmd.SetHandler((string db, string group, string name, string? parent) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;
                var grp = FindGroup(mgr, group);

                if (grp == null)
                {
                    CliResult.Fail("scenario alternative create",
                        $"Alternative group '{group}' not found.", db).Print();
                    return;
                }

                var parentAlt = parent != null ? FindAlternative(grp, parent) : grp.BaseAlternative;
                var newAlt = mgr.CreateAlternative(grp, parentAlt, name);

                CliResult.Ok("scenario alternative create", db, new
                {
                    id = newAlt.AltId,
                    name = newAlt.Name,
                    group = grp.Name,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario alternative create", ex.Message, db).Print();
            }
        }, dbOpt, groupOpt, nameOpt, parentOpt);

        return cmd;
    }

    private static Command BuildAltSet()
    {
        var dbOpt = SharedOptions.Database();
        var scenarioOpt = new Option<string>("--scenario", "Scenario name") { IsRequired = true };
        var groupOpt = new Option<string>("--group", "Alternative group name or ID") { IsRequired = true };
        var nameOpt = new Option<string>("--name", "Alternative name to assign") { IsRequired = true };

        var cmd = new Command("set", "Assign an alternative to a scenario for a group");
        cmd.AddOption(dbOpt);
        cmd.AddOption(scenarioOpt);
        cmd.AddOption(groupOpt);
        cmd.AddOption(nameOpt);

        cmd.SetHandler((string db, string scenario, string group, string name) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var mgr = ctx.ScenarioManager;

                var sc = mgr.FindScenarioByName(scenario);
                if (sc == null)
                {
                    CliResult.Fail("scenario alternative set",
                        $"Scenario '{scenario}' not found.", db).Print();
                    return;
                }

                var grp = FindGroup(mgr, group);
                if (grp == null)
                {
                    CliResult.Fail("scenario alternative set",
                        $"Alternative group '{group}' not found.", db).Print();
                    return;
                }

                var alt = FindAlternative(grp, name);
                if (alt == null)
                {
                    CliResult.Fail("scenario alternative set",
                        $"Alternative '{name}' not found in group '{group}'.", db).Print();
                    return;
                }

                mgr.AddAlternative(sc, alt);
                CliResult.Ok("scenario alternative set", db, new
                {
                    scenario = sc.Name,
                    group = grp.Name,
                    alternative = alt.Name,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("scenario alternative set", ex.Message, db).Print();
            }
        }, dbOpt, scenarioOpt, groupOpt, nameOpt);

        return cmd;
    }

    // ── Helper methods ────────────────────────────────────────────────

    private static IAlternativeGroup? FindGroup(IScenarioManager mgr, string nameOrId)
    {
        foreach (var grp in mgr.AlternativeGroups)
        {
            if (string.Equals(grp.Name, nameOrId, StringComparison.OrdinalIgnoreCase)
                || string.Equals(grp.Id, nameOrId, StringComparison.OrdinalIgnoreCase))
                return grp;
        }
        return null;
    }

    private static IAlternative? FindAlternative(IAlternativeGroup grp, string name)
    {
        foreach (var alt in grp)
        {
            if (string.Equals(alt.Name, name, StringComparison.OrdinalIgnoreCase))
                return alt;
        }
        return null;
    }
}
