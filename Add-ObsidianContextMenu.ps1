# Add-ObsidianContextMenu.ps1
# Adds "Open as Obsidian Vault" to the right-click context menu for folders.
# Run once as the current user - no admin rights required.

$obsidianPath = "$env:LOCALAPPDATA\Programs\obsidian\Obsidian.exe"

if (-not (Test-Path $obsidianPath)) {
    Write-Warning "Obsidian.exe not found at: $obsidianPath"
    Write-Warning "Edit the `$obsidianPath variable in this script to match your install path."
    exit 1
}

# URL-encode the path via PowerShell so Obsidian's URI handler receives a valid URI.
# %1 is replaced by Explorer with the selected folder path at runtime.
$command = "powershell.exe -WindowStyle Hidden -Command `"Start-Process ('obsidian://open?path=' + [uri]::EscapeDataString('%1'))`""
$iconValue = "`"$obsidianPath`",0"

# Only register on Directory and Drive - not on files or folder background.
$classes = @(
    "Directory",
    "Drive"
)

foreach ($class in $classes) {
    $keyPath = "HKCU:\Software\Classes\$class\shell\OpenAsObsidianVault"

    if (-not (Test-Path $keyPath)) { New-Item -Path $keyPath -Force | Out-Null }
    Set-Item     -Path $keyPath -Value "Open as Obsidian Vault"
    Set-ItemProperty -Path $keyPath -Name "Icon" -Value $iconValue

    $cmdPath = "$keyPath\command"
    if (-not (Test-Path $cmdPath)) { New-Item -Path $cmdPath -Force | Out-Null }
    Set-Item -Path $cmdPath -Value $command
}

Write-Host "Done! Context menu registered for folders and drives." -ForegroundColor Green
Write-Host "Right-click any folder > 'Open as Obsidian Vault'" -ForegroundColor Cyan
