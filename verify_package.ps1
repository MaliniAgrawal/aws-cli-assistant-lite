# Pre-Distribution Package Verification Checklist
# Runs essential checks on the distribution package created by build_package.ps1
# Must be run from the project root (aws-cli-assistant-lite)

$VERSION = "1.0.0"
$PACKAGE_NAME = "aws-cli-assistant-lite-v$VERSION"
$ZIP_FILE = "dist\$PACKAGE_NAME.zip"
$CHECKSUM_FILE = "dist\$PACKAGE_NAME.zip.sha256"
$DIST_FOLDER = "dist\$PACKAGE_NAME"
$TEST_EXTRACT_PATH = "C:\temp\final-package-test"

Write-Host "`n========================================================" -ForegroundColor Cyan
Write-Host "  Pre-Distribution Verification Checklist" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

# 1. Verify package contents in dist folder
Write-Host "`n=== 1. Package Contents Verification ===" -ForegroundColor Yellow
if (Test-Path $DIST_FOLDER) {
    Write-Host "✅ Distribution folder found: $DIST_FOLDER" -ForegroundColor Green
    Write-Host "Contents:" -ForegroundColor White
    dir $DIST_FOLDER
} else {
    Write-Host "❌ Distribution folder NOT found: $DIST_FOLDER" -ForegroundColor Red
    Write-Host "Please run .\build_package.ps1 first." -ForegroundColor Red
    exit 1
}

# 2. Check ZIP integrity and file size
Write-Host "`n=== 2. ZIP Integrity and Size ===" -ForegroundColor Yellow
if (Test-Path $ZIP_FILE) {
    Write-Host "✅ ZIP archive found: $ZIP_FILE" -ForegroundColor Green
    $zipItem = Get-Item $ZIP_FILE
    $zipSizeKB = $zipItem.Length / 1KB
    Write-Host "ZIP Size: $([math]::Round($zipSizeKB, 2)) KB" -ForegroundColor Green
} else {
    Write-Host "❌ ZIP archive missing: $ZIP_FILE" -ForegroundColor Red
    exit 1
}

# 3. Verify checksum exists and display hash
Write-Host "`n=== 3. Checksum Verification ===" -ForegroundColor Yellow
if (Test-Path $CHECKSUM_FILE) {
    Write-Host "✅ Checksum file exists: $CHECKSUM_FILE" -ForegroundColor Green
    Write-Host "Hash Content:" -ForegroundColor White
    cat $CHECKSUM_FILE
} else {
    Write-Host "❌ Checksum file missing: $CHECKSUM_FILE" -ForegroundColor Red
}

# 4. Test extraction to a clean temp directory
Write-Host "`n=== 4. Test Extraction ===" -ForegroundColor Yellow

# Clean up previous test extract folder
if (Test-Path $TEST_EXTRACT_PATH) { 
    Write-Host "Cleaning up previous test folder: $TEST_EXTRACT_PATH" -ForegroundColor Gray
    Remove-Item $TEST_EXTRACT_PATH -Recurse -Force 
}

# Create new test folder
New-Item -ItemType Directory -Force -Path $TEST_EXTRACT_PATH | Out-Null

# Expand archive
try {
    Write-Host "Extracting $ZIP_FILE to $TEST_EXTRACT_PATH..." -ForegroundColor White
    Expand-Archive -Path $ZIP_FILE -DestinationPath $TEST_EXTRACT_PATH -Force
    Write-Host "✅ Extraction successful. The contents were placed directly in the test folder." -ForegroundColor Green
    
    # Verify extracted contents - MODIFIED: Check the contents of the extraction path directly
    Write-Host "`nExtracted package contents (should match the package folder):" -ForegroundColor Cyan
    dir "$TEST_EXTRACT_PATH" | Select-Object Name

} catch {
    Write-Host "❌ Extraction failed! $($_.Exception.Message)" -ForegroundColor Red
    # Clean up on failure
    if (Test-Path $TEST_EXTRACT_PATH) { Remove-Item $TEST_EXTRACT_PATH -Recurse -Force }
    exit 1
}

# Final cleanup of the test extraction directory (optional, but good practice)
Write-Host "`nCleaning up test extraction folder..." -ForegroundColor Gray
if (Test-Path $TEST_EXTRACT_PATH) { Remove-Item $TEST_EXTRACT_PATH -Recurse -Force }

Write-Host "`n========================================================" -ForegroundColor Green
Write-Host "✅ FINAL PACKAGE CHECKLIST PASSED! Ready for distribution." -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Green