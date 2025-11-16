#!/usr/bin/env python3
"""
Create distribution package for client simulation
"""
import shutil
import os
from pathlib import Path

def create_client_package():
    """Create a clean package like a client would download"""
    
    # Create distribution folder
    dist_path = Path("../aws-cli-assistant-client-test")
    if dist_path.exists():
        shutil.rmtree(dist_path)
    
    dist_path.mkdir()
    
    # Copy essential files only (what client gets)
    files_to_copy = [
        "requirements.txt",
        "setup.py", 
        "README.md",
        "aws_cli_assistant/",
        "test_basic.py"
    ]
    
    for item in files_to_copy:
        src = Path(item)
        if src.exists():
            if src.is_dir():
                shutil.copytree(src, dist_path / item)
            else:
                shutil.copy2(src, dist_path / item)
    
    # Create client setup script
    setup_script = dist_path / "client_setup.bat"
    setup_script.write_text("""@echo off
echo Setting up AWS CLI Assistant - Client Test
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
call venv\\Scripts\\activate.bat

echo Step 2: Installing dependencies...
pip install -r requirements.txt

echo Step 3: Testing basic functionality...
python test_basic.py

echo.
echo Setup complete! Run: python aws_cli_assistant\\mcp_server.py
pause
""")
    
    print(f"✅ Client package created at: {dist_path.absolute()}")
    return dist_path

if __name__ == "__main__":
    create_client_package()