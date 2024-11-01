param (
    [string]$year
)

if (-not $year) {
    Write-Host "No year supplied as an argument (e.g. .\install.ps1 2024)."
    exit 1
}

$process = Start-Process -FilePath ".\setup.exe" -ArgumentList "/s /v`"/qn`"" -PassThru
$process.WaitForExit()

if (Test-Path "${env:ProgramFiles(x86)}\DHI\MIKE+") {
    $MIKE_INSTALL_PATH = "${env:ProgramFiles(x86)}\DHI\MIKE+"
} else {
    $MIKE_INSTALL_PATH = "$env:ProgramFiles\DHI\MIKE+"
}

$MIKE_BIN_PATH = "$MIKE_INSTALL_PATH\$year\bin\x64"
$SHELL_CONFIG_NAME = "DHI.MIKEPlus.Shell.exe.config"
$SHELL_CONFIG_FILE = "$MIKE_BIN_PATH\$SHELL_CONFIG_NAME"

if (-not (Test-Path $SHELL_CONFIG_FILE)) {
    Write-Host "File $SHELL_CONFIG_FILE does not exist."
    exit 1
}

Write-Host "Updating $SHELL_CONFIG_FILE..."
$backupFile = "$SHELL_CONFIG_FILE.bak"
$tempFile = "$SHELL_CONFIG_FILE.tmp"

Copy-Item -Path $SHELL_CONFIG_FILE -Destination $backupFile -Force
if (-not (Test-Path $backupFile)) {
    Write-Host "Failed to copy $SHELL_CONFIG_FILE to $backupFile."
    exit 1
}

Copy-Item -Path $SHELL_CONFIG_FILE -Destination $tempFile -Force
if (-not (Test-Path $tempFile)) {
    Write-Host "Failed to copy $SHELL_CONFIG_FILE to $tempFile."
    exit 1
}

$regexPattern = '<setting name="LicenseTimeout" serializeAs="String">\s*<value>(\d+)</value>\s*</setting>'
$existingValue = '240000'
$newValue = '1'

$fileContent = Get-Content -Path $tempFile -Raw

if ($fileContent -match $regexPattern) {
    $updatedContent = $fileContent -replace $existingValue, $newValue
    Set-Content -Path $tempFile -Value $updatedContent -Force
    Write-Host "Updated the value in $tempFile."
} else {
    Write-Host "Pattern not found in $tempFile."
}

Copy-Item -Path $tempFile -Destination $SHELL_CONFIG_FILE -Force
Remove-Item -Path $tempFile -Force
