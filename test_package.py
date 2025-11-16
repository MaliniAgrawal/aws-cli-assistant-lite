#!/usr/bin/env python3
"""Quick test to verify the AWS CLI Assistant package works correctly."""

import sys
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

def test_basic_functionality():
    """Test core functionality without AWS calls."""
    print("Testing AWS CLI Assistant package...")
    
    # Test imports
    try:
        from aws_cli_assistant.core.command_generator import generate_command
        from aws_cli_assistant.core.nlp_utils import parse_nlp
        print("[OK] Imports successful")
    except ImportError as e:
        print(f"[ERROR] Import failed: {e}")
        return False
    
    # Test command generation
    try:
        intent = "list_s3_buckets"
        entities = {"region": "us-west-1"}
        command, explanation = generate_command(intent, entities)
        print(f"[OK] Command generation: {command}")
        print(f"   Explanation: {explanation}")
    except Exception as e:
        print(f"[ERROR] Command generation failed: {e}")
        return False
    
    # Test NLP parsing
    try:
        intent, entities = parse_nlp("list my s3 buckets")
        print(f"[OK] NLP parsing: intent='{intent}', entities={entities}")
    except Exception as e:
        print(f"[ERROR] NLP parsing failed: {e}")
        return False
    
    print("\n[SUCCESS] Package is working correctly!")
    return True

if __name__ == "__main__":
    success = test_basic_functionality()
    sys.exit(0 if success else 1)