# Add-PowerShellContextMenu.ps1
# Adds "Open in PowerShell" to the right-click context menu for folders.
# Run once as the current user - no admin rights required.

$pwshPath = "C:\Program Files\PowerShell\7\pwsh.exe"

if (-not (Test-Path $pwshPath)) {
    # Fall back to Windows PowerShell 5
    $pwshPath = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
    Write-Warning "PowerShell 7 not found - falling back to Windows PowerShell 5."
}

$iconValue = "`"$pwshPath`",0"

# Directory and Drive: %1 = selected folder path
# Directory\Background: %V = current open folder (right-click on empty space)
$entries = @{
    "Directory"            = "`"$pwshPath`" -NoExit -Command `"Set-Location '%1'`""
    "Drive"                = "`"$pwshPath`" -NoExit -Command `"Set-Location '%1'`""
    "Directory\Background" = "`"$pwshPath`" -NoExit -Command `"Set-Location '%V'`""
}

foreach ($class in $entries.Keys) {
    $keyPath = "HKCU:\Software\Classes\$class\shell\OpenInPowerShell"

    if (-not (Test-Path $keyPath)) { New-Item -Path $keyPath -Force | Out-Null }
    Set-Item         -Path $keyPath -Value "Open in PowerShell"
    Set-ItemProperty -Path $keyPath -Name "Icon" -Value $iconValue

    $cmdPath = "$keyPath\command"
    if (-not (Test-Path $cmdPath)) { New-Item -Path $cmdPath -Force | Out-Null }
    Set-Item -Path $cmdPath -Value $entries[$class]
}

Write-Host "Done! Context menu registered for folders, drives, and folder background." -ForegroundColor Green
Write-Host "Right-click any folder > 'Open in PowerShell'" -ForegroundColor Cyan
