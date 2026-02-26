using System.Collections.Generic;
using System.Reflection;
using DHI.Amelia.DataModule.Services.DataSource;
using DHI.Amelia.DataModule.Services.DataTables;
using DHI.Amelia.DataModule.Services.ImportExportPfsFile;
using DHI.Amelia.DataModule.Interface;
using DHI.Amelia.GlobalUtility.DataType;
using DHI.Amelia.Tools.TopologyRepairTool;
using DHI.Amelia.Tools.InterpolationEngine;
using DHI.Amelia.Tools.ConnectionRepairEngine;
using DHI.Amelia.Tools.CatchmentProcessing;
using DHI.Amelia.Tools.ImportTool.ImportEngine;
using DHI.Mike.Install;

namespace MikePlusJsonCli;

/// <summary>
/// Wraps the DHI Amelia .NET assemblies and manages the full lifecycle of a
/// MIKE+ model database for use by command handlers.
///
/// This class is identical in purpose to <c>AmeliaContext</c> in PR #113
/// (cli/MikePlusCli/AmeliaContext.cs); the difference is that it is held open
/// for the lifetime of the streaming session rather than being created and
/// disposed per invocation.  All of the Amelia API calls (IMuTable operations,
/// tool invocations, simulation dispatch) are therefore made within a single
/// open session, giving the same performance profile as the MIKE+ GUI.
/// </summary>
public sealed class AmeliaContext : IDisposable
{
    private readonly BaseDataSource _dataSource;
    private readonly DataTableContainer _dataTables;
    private bool _isOpen;

    /// <summary>Absolute path to the .sqlite database file.</summary>
    public string DbPath { get; }

    /// <summary>The Amelia data-table container used by tools and simulation.</summary>
    public DataTableContainer DataTables => _dataTables;

    /// <summary>The Amelia scenario manager.</summary>
    public IScenarioManager ScenarioManager =>
        _dataSource.ScenarioManager
        ?? throw new InvalidOperationException("Scenario manager unavailable. Is the database open?");

    // ── Properties mirroring Database in the Python package ───────────

    public string ProjectionString   => _dataSource.ProjectionString;
    public int    Srid               => _dataSource.Srid;
    public string ActiveModel        => _dataSource.ActiveModel.ToString();
    public string ActiveSimulation   => _dataSource.ActiveSimulation;
    public string Version            => $"{_dataSource.DbMajorVersion}.{_dataSource.DbMinorVersion}";

    // ── Static bootstrap ──────────────────────────────────────────────

    /// <summary>
    /// One-time process setup: registers the MIKE+ assembly resolver and
    /// initialises the DHI MIKE product environment.
    /// </summary>
    public static void Bootstrap()
    {
        // The MIKE_PLUS_INSTALL environment variable overrides the default.
        // The default path embeds the installed product year; set the env var
        // when targeting a different version or a non-standard install location.
        var installRoot = Environment.GetEnvironmentVariable("MIKE_PLUS_INSTALL")
            ?? @"C:\Program Files (x86)\DHI\MIKE+\2026";
        var binDir = Path.Combine(installRoot, "bin");

        AppDomain.CurrentDomain.AssemblyResolve += (_, args) =>
        {
            var name = new AssemblyName(args.Name).Name + ".dll";
            var path = Path.Combine(binDir, name);
            return File.Exists(path) ? Assembly.LoadFrom(path) : null;
        };

        MikeImport.Setup(2026, MikeProducts.MikePlus);
    }

    // ── Construction ──────────────────────────────────────────────────

    private AmeliaContext(string dbPath, BaseDataSource dataSource, DataTableContainer dataTables)
    {
        DbPath      = dbPath;
        _dataSource = dataSource;
        _dataTables = dataTables;
        _isOpen     = false;
    }

    /// <summary>Creates a new MIKE+ model database and returns an open context.</summary>
    public static AmeliaContext Create(string dbPath, string projectionString = "", int srid = -1)
    {
        var fullPath = Path.GetFullPath(dbPath);
        var ds       = BaseDataSource.Create(fullPath);
        ds.CreateDatabase();
        ds.OpenDatabase();
        ds.CreateModelTables(srid, projectionString);
        ds.CloseDatabase();

        var dtc = new DataTableContainer(true) { DataSource = ds };
        var ctx = new AmeliaContext(fullPath, ds, dtc);
        ctx.OpenInternal();
        return ctx;
    }

    /// <summary>Opens an existing MIKE+ model database and returns an open context.</summary>
    public static AmeliaContext Open(string dbPath)
    {
        var fullPath = Path.GetFullPath(dbPath);
        if (!File.Exists(fullPath))
            throw new FileNotFoundException($"Database not found: {fullPath}");

        var ds  = BaseDataSource.Create(fullPath);
        var dtc = new DataTableContainer(true) { DataSource = ds };
        var ctx = new AmeliaContext(fullPath, ds, dtc);
        ctx.OpenInternal();
        return ctx;
    }

    private void OpenInternal()
    {
        _dataSource.OpenDatabase();
        _dataTables.SetActiveModel(_dataSource.ActiveModel);
        _dataTables.SetEumAppUnitSystem(_dataSource.UnitSystemOption);
        _dataTables.OnResetContainer(null, null);
        _dataTables.UndoRedoManager    = new AmlUndoRedoManager();
        _dataTables.ImportExportPfsFile = new ImportExportPfsFile();
        _isOpen = true;
    }

    /// <summary>Closes the database, flushing the undo buffer.</summary>
    public void Close()
    {
        if (!_isOpen) return;
        _dataTables.UndoRedoManager?.ClearUndoRedoBuffer();
        _dataSource.CloseDatabase();
        _isOpen = false;
    }

    public void Dispose() => Close();

    // ── Model metadata ────────────────────────────────────────────────

    /// <summary>Returns all table names known to the DataTableContainer.</summary>
    public IEnumerable<string> GetTableNames()
    {
        foreach (var t in _dataTables.GetAllTables())
            yield return t.TableName;
    }

    // ── Edit operations (via IMuTable) ────────────────────────────────

    /// <summary>
    /// Queries rows from <paramref name="tableName"/> via IMuTable.GetMuidAndFieldsWhereOrder.
    /// Returns a sequence of dictionaries (field name → value).
    /// </summary>
    public IEnumerable<Dictionary<string, object?>> Select(
        string tableName, string columns, string where, string orderBy)
    {
        var muTable = GetMuTable(tableName);
        var result  = muTable.GetMuidAndFieldsWhereOrder(columns, where, orderBy);
        foreach (var row in result)
        {
            var dict = new Dictionary<string, object?>();
            for (int i = 0; i < row.Count; i++)
                dict[row.GetKey(i)] = row.GetValue(i);
            yield return dict;
        }
    }

    /// <summary>Inserts a single row via IMuTable.InsertByCommand.</summary>
    public void Insert(string tableName, Dictionary<string, object?> fields)
    {
        var muTable = GetMuTable(tableName);
        muTable.InsertByCommand(fields);
    }

    /// <summary>Updates rows matching <paramref name="where"/> via IMuTable.SetValuesByCommand.</summary>
    public void Update(string tableName, Dictionary<string, object?> fields, string where)
    {
        var muTable = GetMuTable(tableName);
        muTable.SetValuesByCommand(fields, where);
    }

    /// <summary>Deletes rows matching <paramref name="where"/> via IMuTable.MultiDeleteByCommand.</summary>
    public void Delete(string tableName, string where)
    {
        var muTable = GetMuTable(tableName);
        // Resolve the MUID list from the WHERE clause, then delete in one call.
        var muids = muTable.GetMuidAndFieldsWhereOrder("MUID", where, "")
                           .Select(r => r.GetValue(0)?.ToString() ?? "")
                           .ToList();
        muTable.MultiDeleteByCommand(muids);
    }

    private IMuTable GetMuTable(string tableName)
    {
        var table = _dataTables.GetTable(tableName)
            ?? throw new InvalidOperationException($"Table '{tableName}' not found.");
        return (IMuTable)table;
    }

    // ── Import operations ─────────────────────────────────────────────

    /// <summary>Runs a data import from an XML configuration file.</summary>
    public void ImportData(string configPath)
    {
        var tool = ImportToolBase.CreateFromConfig(configPath, _dataTables);
        tool.Execute();
    }

    // ── Tool operations ───────────────────────────────────────────────

    /// <summary>Runs topology repair.</summary>
    public void RunTopoRepair(double snapDistance, bool deleteUnlinked)
    {
        // Model-type-aware: CS uses CSTopologyRepairTool, WD uses WDTopologyRepairTool.
        var param = new TopologyRepairParam
        {
            SnapDistance   = snapDistance,
            DeleteUnlinked = deleteUnlinked,
        };

        ITopologyRepairTool tool = ActiveModel.StartsWith("WD")
            ? new WDTopologyRepairTool(_dataTables)
            : new CSTopologyRepairTool(_dataTables);

        tool.Run(param);
    }

    /// <summary>Runs connection repair.</summary>
    public void RunConnectionRepair()
    {
        var engine = new ConnectionRepairEngine(_dataTables);
        engine.Run();
    }

    /// <summary>Runs the interpolation engine.</summary>
    public void RunInterpolation(
        string method, string targetTable, string targetAttr,
        string sourceLayer, string sourceAttr, string demFile)
    {
        var param = new InterpolationToolParameters
        {
            Method      = Enum.Parse<InterpolationMethod>(method, ignoreCase: true),
            TargetTable = targetTable,
            TargetAttr  = targetAttr,
            SourceLayer = sourceLayer,
            SourceAttr  = sourceAttr,
            DemFile     = demFile,
        };
        var engine = new InterpolationEngine(_dataTables);
        engine.Run(param);
    }

    /// <summary>Runs catchment slope/length processing.</summary>
    public void RunCatchmentProcess()
    {
        var tool = new CatchmentSlope(_dataTables);
        tool.Run();
    }
}
