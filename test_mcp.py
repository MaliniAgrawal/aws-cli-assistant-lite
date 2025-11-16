#!/usr/bin/env python3
"""Test MCP server functionality."""

import sys
import asyncio
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

async def test_mcp_tools():
    """Test MCP server tools."""
    print("Testing MCP server tools...")
    
    try:
        from aws_cli_assistant.mcp_server import generate_aws_cli, health_check, list_supported_services
        print("[OK] MCP server imports successful")
    except ImportError as e:
        print(f"[ERROR] MCP import failed: {e}")
        return False
    
    # Test health check
    try:
        health = await health_check()
        print(f"[OK] Health check: {health}")
    except Exception as e:
        print(f"[ERROR] Health check failed: {e}")
        return False
    
    # Test supported services
    try:
        services = await list_supported_services()
        print(f"[OK] Supported services: {services}")
    except Exception as e:
        print(f"[ERROR] List services failed: {e}")
        return False
    
    # Test AWS CLI generation
    try:
        result = await generate_aws_cli("list my s3 buckets")
        print(f"[OK] AWS CLI generation: {result['command']}")
        print(f"    Validation status: {result['validation']['status']}")
    except Exception as e:
        print(f"[ERROR] AWS CLI generation failed: {e}")
        return False
    
    print("\n[SUCCESS] MCP server is working correctly!")
    return True

if __name__ == "__main__":
    success = asyncio.run(test_mcp_tools())
    sys.exit(0 if success else 1)