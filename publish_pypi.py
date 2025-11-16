#!/usr/bin/env python3
"""
Publish to PyPI
"""
import subprocess
import sys

def publish_to_pypi():
    """Publish package to PyPI"""
    
    commands = [
        # Clean previous builds
        "rm -rf dist/ build/ *.egg-info/",
        
        # Build package
        "python -m build",
        
        # Upload to PyPI (requires API token)
        "python -m twine upload dist/*"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            print(f"Failed: {cmd}")
            sys.exit(1)
    
    print("✅ Published to PyPI successfully!")

if __name__ == "__main__":
    publish_to_pypi()