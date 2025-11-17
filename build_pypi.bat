@echo off
echo Building PyPI package...

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist\*.tar.gz del /q dist\*.tar.gz
if exist dist\*.whl del /q dist\*.whl
if exist *.egg-info rmdir /s /q *.egg-info

REM Install build tools
pip install build twine

REM Build package
python -m build

echo.
echo PyPI package built successfully!
echo Files created in dist/:
dir dist\*.whl
dir dist\*.tar.gz

echo.
echo Next steps:
echo 1. Test upload: twine upload --repository testpypi dist/*
echo 2. Real upload: twine upload dist/*
pause