@echo off
echo Activating AWS CLI Assistant environment...
cd /d "%~dp0"

if exist "venv-phase3\Scripts\activate.bat" (
    call venv-phase3\Scripts\activate.bat
    echo Environment activated: venv-phase3
) else (
    echo Creating virtual environment...
    python -m venv venv-phase3
    call venv-phase3\Scripts\activate.bat
    pip install -r requirements.txt
    echo Environment created and activated: venv-phase3
)

echo.
echo Ready to work! Use 'deactivate' to exit.
cmd /k