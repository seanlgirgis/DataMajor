# Set-Win11ClassicContextMenu.ps1
# Forces Windows 11 to always show the classic (full) context menu on right-click,
# so custom entries like Antigravity, Obsidian, and PowerShell appear immediately
# without having to click "Show more options".
#
# This is a per-user change (HKCU) - no admin rights required.
# A sign-out/sign-in or Explorer restart is required to apply.
#
# Usage:
#   .\Set-Win11ClassicContextMenu.ps1          # Enable classic menu
#   .\Set-Win11ClassicContextMenu.ps1 -Revert  # Restore Windows 11 modern menu

param(
    [switch]$Revert
)

$clsidPath = "HKCU:\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"

if ($Revert) {
    $parent = "HKCU:\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}"
    if (Test-Path $parent) {
        Remove-Item -Path $parent -Recurse -Force
        Write-Host "Reverted - Windows 11 modern context menu restored." -ForegroundColor Yellow
    } else {
        Write-Host "Nothing to revert - classic menu override was not set." -ForegroundColor DarkGray
    }
} else {
    if (-not (Test-Path $clsidPath)) {
        New-Item -Path $clsidPath -Force | Out-Null
    }
    # The key must exist with an empty default value - that's what suppresses the modern menu.
    Set-ItemProperty -Path $clsidPath -Name "(default)" -Value "" -Type String
    Write-Host "Classic context menu enabled." -ForegroundColor Green
}

# Restart Explorer to apply immediately (saves a sign-out/in).
Write-Host "Restarting Explorer to apply..." -ForegroundColor Cyan
Stop-Process -Name explorer -Force
Start-Sleep -Seconds 1
Start-Process explorer
Write-Host "Done. Right-click any folder to confirm." -ForegroundColor Green
