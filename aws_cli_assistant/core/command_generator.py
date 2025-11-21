# src/core/command_generator.py
# Use package-root imports (when `src` is on PYTHONPATH) — avoid importing `src.` prefix which breaks
# when running files under `src/` directly.
from loguru import logger
from aws_cli_assistant.core.aws_parsers.s3_parser import parse_s3_intent
from aws_cli_assistant.core.aws_parsers.ec2_parser import parse_ec2_intent
from aws_cli_assistant.core.aws_parsers.lambda_parser import parse_lambda_intent
from aws_cli_assistant.core.aws_parsers.dynamodb_parser import parse_dynamodb_intent
from aws_cli_assistant.core.aws_parsers.iam_parser import parse_iam_intent

def list_supported_services():
    return ["s3", "ec2", "dynamodb", "iam", "lambda"]

def generate_command(intent: str, entities: dict):
    """Generate AWS CLI commands based on intent and entities.
    
    Args:
        intent: The classified intent string
        entities: Dict of extracted entities
        
    Returns:
        tuple: (command_str, description_str)
    """
    if intent.startswith("s3_") or intent == "list_s3_buckets":
        return parse_s3_intent(intent, entities), f"S3 operation: {intent}"
    elif intent.startswith("ec2_") or intent == "list_ec2_instances" or intent == "describe_ec2_instances":
        return parse_ec2_intent(intent, entities), f"EC2 operation: {intent}"
    elif intent.startswith("lambda_") or intent == "list_lambda_functions":
        return parse_lambda_intent(intent, entities), f"Lambda operation: {intent}"
    elif intent.startswith("dynamodb_") or intent == "list_dynamodb_tables":
        return parse_dynamodb_intent(intent, entities), f"DynamoDB operation: {intent}"
    elif intent.startswith("iam_") or intent == "list_iam_users" or intent == "list_iam_roles":
        return parse_iam_intent(intent, entities), f"IAM operation: {intent}"

    logger.warning("Unsupported intent: %s", intent)
    return "echo 'Unknown service intent'", "Service not supported or intent unclear"
