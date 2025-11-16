#!/usr/bin/env python3
"""Basic test to verify AWS CLI Assistant functionality"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'aws_cli_assistant'))

def test_command_generator():
    """Test command generation"""
    try:
        from aws_cli_assistant.core.command_generator import generate_command, list_supported_services
        
        print("[OK] Testing command generator...")
        
        # Test supported services
        services = list_supported_services()
        print(f"   Supported services: {services}")
        assert len(services) > 0, "No services found"
        
        # Test S3 command generation
        cmd, desc = generate_command("list_s3_buckets", {})
        print(f"   S3 command: {cmd}")
        assert "aws s3api list-buckets" in cmd, "S3 command incorrect"
        
        # Test DynamoDB command generation
        cmd, desc = generate_command("list_dynamodb_tables", {})
        print(f"   DynamoDB command: {cmd}")
        assert "aws dynamodb list-tables" in cmd, "DynamoDB command incorrect"
        
        print("[OK] Command generator working!")
        return True
        
    except Exception as e:
        print(f"[FAIL] Command generator failed: {e}")
        return False

def test_imports():
    """Test basic imports"""
    try:
        print("[OK] Testing imports...")
        
        # Test core imports
        from aws_cli_assistant.core import command_generator
        from aws_cli_assistant.core import aws_validator
        print("   Core modules imported")
        
        # Test config imports
        from config import settings
        print("   Config modules imported")
        
        print("[OK] All imports working!")
        return True
        
    except Exception as e:
        print(f"[FAIL] Import failed: {e}")
        return False

def main():
    """Run basic tests"""
    print("AWS CLI Assistant - Basic Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_command_generator
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("SUCCESS: All tests passed! Your project is working.")
    else:
        print("WARNING: Some tests failed. Check the errors above.")
    
    return passed == len(tests)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)