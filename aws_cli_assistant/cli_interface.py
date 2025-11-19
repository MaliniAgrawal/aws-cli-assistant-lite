# src/cli_interface.py
import subprocess
import sys
from core.nlp_utils import parse_nlp
from core.command_generator import generate_command
from core.aws_validator import validate_command_safe
from core.telemetry import telemetry_log_event

def run_cli_interface():
    """Interactive CLI interface for AWS CLI Assistant"""
    print("🚀 AWS CLI Assistant - Interactive Mode")
    print("Type 'exit' or 'quit' to stop, 'help' for supported services\n")
    
    while True:
        try:
            # Get user input
            query = input("Enter your request: ").strip()
            
            if not query:
                continue
                
            if query.lower() in ['exit', 'quit', 'q']:
                print("Goodbye! 👋")
                break
                
            if query.lower() == 'help':
                print("Supported services: S3, DynamoDB, EC2, Lambda, IAM")
                print("Example: 'list my s3 buckets' or 'describe ec2 instances'\n")
                continue
            
            # Process the query
            print(f"\n🔄 Processing: {query}")
            
            # Parse and generate command
            intent, entities = parse_nlp(query)
            command, explanation = generate_command(intent, entities)
            validation = validate_command_safe(intent, entities)
            
            # Display results
            print(f"\n📋 Generated Command: {command}")
            print(f"💡 Explanation: {explanation}")
            
            # Show validation status
            status = validation.get('status', 'unknown')
            if status == 'valid':
                print(f"✅ Validation: {validation.get('reason', 'Valid')}")
            else:
                print(f"⚠️  Validation: {validation.get('reason', 'Invalid')}")
            
            # Ask for execution
            execute = input(f"\nExecute this command? (y/n): ").strip().lower()
            
            if execute in ['y', 'yes']:
                print(f"\n⚡ Executing: {command}")
                try:
                    result = subprocess.run(
                        command.split(), 
                        capture_output=True, 
                        text=True, 
                        timeout=30
                    )
                    
                    if result.returncode == 0:
                        print("✅ Success!")
                        if result.stdout:
                            print(result.stdout)
                    else:
                        print("❌ Error:")
                        print(result.stderr)
                        
                except subprocess.TimeoutExpired:
                    print("⏰ Command timed out (30s limit)")
                except Exception as e:
                    print(f"❌ Execution failed: {str(e)}")
            else:
                print("Command not executed.")
            
            print("\n" + "="*50 + "\n")
            
            # Log telemetry
            telemetry_log_event("cli.interaction", {
                "query": query,
                "intent": intent,
                "executed": execute in ['y', 'yes']
            })
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            continue

if __name__ == "__main__":
    run_cli_interface()