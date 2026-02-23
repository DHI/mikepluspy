using System.Text.Json;
using System.Text.Json.Serialization;

namespace MikePlusCli;

/// <summary>
/// Structured output envelope used by every command.
/// Ensures machine-readable, AI-friendly JSON on stdout.
/// Diagnostic messages go to stderr so stdout stays parseable.
/// </summary>
public sealed class CliResult
{
    [JsonPropertyName("status")]
    public string Status { get; init; } = "ok";

    [JsonPropertyName("command")]
    public string Command { get; init; } = "";

    [JsonPropertyName("database")]
    public string? Database { get; init; }

    [JsonPropertyName("data")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    public object? Data { get; init; }

    [JsonPropertyName("error")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    public string? Error { get; init; }

    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        WriteIndented = true,
        DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
    };

    /// <summary>Write the result as JSON to stdout.</summary>
    public void Print()
    {
        Console.WriteLine(JsonSerializer.Serialize(this, JsonOptions));
    }

    public static CliResult Ok(string command, string? database = null, object? data = null) =>
        new() { Status = "ok", Command = command, Database = database, Data = data };

    public static CliResult Fail(string command, string message, string? database = null) =>
        new() { Status = "error", Command = command, Database = database, Error = message };
}
