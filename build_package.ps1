# AWS CLI Assistant - Build Distribution Package
# PowerShell script for Windows

$VERSION = "1.0.0"
$PACKAGE_NAME = "aws-cli-assistant-lite-v$VERSION"

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  AWS CLI Assistant - Package Builder" -ForegroundColor Cyan
Write-Host "  Version: $VERSION" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Clean previous builds
Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
}
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
}
if (Test-Path "*.egg-info") {
    Remove-Item -Recurse -Force "*.egg-info"
}
Write-Host "  [OK] Clean complete" -ForegroundColor Green

# Create distribution directory
Write-Host ""
Write-Host "Creating distribution directory..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "dist\$PACKAGE_NAME" | Out-Null

# Copy project files
Write-Host ""
Write-Host "Copying project files..." -ForegroundColor Yellow

$items = @(
    "aws_cli_assistant",
    "scripts",
    "tests",
    "config",
    "docs",
    "requirements.txt",
    "README.md",
    "LICENSE",
    "setup.py",
    "install.bat",
    "install.sh",
    "CHANGELOG.md"
)

foreach ($item in $items) {
    if (Test-Path $item) {
        if (Test-Path $item -PathType Container) {
            Copy-Item -Path $item -Destination "dist\$PACKAGE_NAME\$item" -Recurse -Force
            Write-Host "  [OK] $item/" -ForegroundColor Green
        } else {
            Copy-Item -Path $item -Destination "dist\$PACKAGE_NAME\" -Force
            Write-Host "  [OK] $item" -ForegroundColor Green
        }
    } else {
        Write-Host "  [SKIP] $item (not found)" -ForegroundColor Gray
    }
}

# Copy SAM template to root
Write-Host ""
Write-Host "Copying SAM template to root..." -ForegroundColor Yellow
if (Test-Path "dist\$PACKAGE_NAME\config\config.template.yaml") {
    Copy-Item -Path "dist\$PACKAGE_NAME\config\config.template.yaml" -Destination "dist\$PACKAGE_NAME\template.yaml" -Force
    Write-Host "  [OK] template.yaml" -ForegroundColor Green
} else {
    Write-Host "  [SKIP] config.template.yaml not found" -ForegroundColor Gray
}

# Clean unnecessary files
Write-Host ""
Write-Host "Cleaning unnecessary files..." -ForegroundColor Yellow

# Remove Python cache
Get-ChildItem -Path "dist\$PACKAGE_NAME" -Include "__pycache__","*.pyc","*.pyo" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
Write-Host "  [OK] Removed Python cache" -ForegroundColor Green

# Remove OS files
Get-ChildItem -Path "dist\$PACKAGE_NAME" -Filter ".DS_Store" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force
Write-Host "  [OK] Removed OS files" -ForegroundColor Green

# Remove virtual environments
$venvs = @("venv", "venv-phase3", "venv-mcp", ".venv")
foreach ($venv in $venvs) {
    $venvPath = "dist\$PACKAGE_NAME\$venv"
    if (Test-Path $venvPath) {
        Remove-Item $venvPath -Recurse -Force
        Write-Host "  [OK] Removed $venv/" -ForegroundColor Green
    }
}

# Remove .env files
if (Test-Path "dist\$PACKAGE_NAME\.env") {
    Remove-Item "dist\$PACKAGE_NAME\.env" -Force
    Write-Host "  [OK] Removed .env" -ForegroundColor Green
}

# Remove IDE folders
$ideFolders = @(".vscode", ".idea", ".vs")
foreach ($ide in $ideFolders) {
    $idePath = "dist\$PACKAGE_NAME\$ide"
    if (Test-Path $idePath) {
        Remove-Item $idePath -Recurse -Force
        Write-Host "  [OK] Removed $ide/" -ForegroundColor Green
    }
}

# Create ZIP archive
Write-Host ""
Write-Host "Creating ZIP archive..." -ForegroundColor Yellow
$zipFile = "dist\$PACKAGE_NAME.zip"
Compress-Archive -Path "dist\$PACKAGE_NAME\*" -DestinationPath $zipFile -Force
Write-Host "  [OK] ZIP created" -ForegroundColor Green

# Create checksum
Write-Host ""
Write-Host "Generating SHA256 checksum..." -ForegroundColor Yellow
$hash = Get-FileHash -Path $zipFile -Algorithm SHA256
$checksum = "$($hash.Hash)  $PACKAGE_NAME.zip"
$checksum | Out-File -FilePath "$zipFile.sha256" -Encoding ASCII
Write-Host "  [OK] Checksum: $($hash.Hash.Substring(0,16))..." -ForegroundColor Green

# Get file sizes
$zipSize = (Get-Item $zipFile).Length / 1MB
$folderSize = (Get-ChildItem "dist\$PACKAGE_NAME" -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB

# Count files
$fileCount = (Get-ChildItem "dist\$PACKAGE_NAME" -Recurse -File | Measure-Object).Count

# Success summary
Write-Host ""
Write-Host "========================================================" -ForegroundColor Green
Write-Host "  Build Complete!" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "ðŸ“¦ Package Details:" -ForegroundColor Cyan
Write-Host "   Name:      $PACKAGE_NAME" -ForegroundColor White
Write-Host "   Version:   $VERSION" -ForegroundColor White
Write-Host "   Files:     $fileCount files" -ForegroundColor White
Write-Host "   Folder:    $([math]::Round($folderSize, 2)) MB" -ForegroundColor White
Write-Host "   ZIP:       $([math]::Round($zipSize, 2)) MB" -ForegroundColor White
Write-Host ""
Write-Host "ðŸ“‹ Output Files:" -ForegroundColor Cyan
Write-Host "   ZIP:       dist\$PACKAGE_NAME.zip" -ForegroundColor White
Write-Host "   Checksum:  dist\$PACKAGE_NAME.zip.sha256" -ForegroundColor White
Write-Host "   Folder:    dist\$PACKAGE_NAME\" -ForegroundColor White
Write-Host ""
Write-Host "âœ… Ready for distribution!" -ForegroundColor Green
Write-Host ""
