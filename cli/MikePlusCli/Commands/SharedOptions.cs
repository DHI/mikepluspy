using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// Shared option definitions reused across commands.
/// </summary>
internal static class SharedOptions
{
    /// <summary>
    /// The --database (-d) option, required by every command that touches a model.
    /// </summary>
    public static Option<string> Database() => new(
        aliases: new[] { "--database", "-d" },
        description: "Path to the MIKE+ model database (.sqlite or .mupp)")
    { IsRequired = true };
}
