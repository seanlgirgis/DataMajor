# Fix-AntiGravityContextMenu.ps1
$antigravityPath = "C:\Users\shareuser\AppData\Local\Programs\Antigravity\bin\antigravity.cmd"
$iconPath = "C:\Users\shareuser\AppData\Local\Programs\Antigravity\antigravity.exe"

$classes = @(
    "Directory",
    "Directory\Background",
    "Drive",
    "*"
)

foreach ($class in $classes) {
    $path = "HKCU:\Software\Classes\$class\shell\AntiGravity"
    if (-not (Test-Path $path)) { New-Item -Path $path -Force | Out-Null }
    
    # Set default value (label)
    Set-Item -Path $path -Value "Open with AntiGravity"
    Set-ItemProperty -Path $path -Name "Icon" -Value $iconPath
    
    $cmdPath = "$path\command"
    if (-not (Test-Path $cmdPath)) { New-Item -Path $cmdPath -Force | Out-Null }
    
    # Set command
    if ($class -eq "Directory\Background") {
        Set-Item -Path $cmdPath -Value "`"$antigravityPath`" `"%V`""
    } else {
        Set-Item -Path $cmdPath -Value "`"$antigravityPath`" `"%1`""
    }
}

Write-Host "Context menu entries updated for Directory, Background, Drive, and All Files (*)."
