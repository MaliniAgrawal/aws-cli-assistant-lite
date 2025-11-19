# AWS CLI Assistant - Lite Edition

## Overview
AWS CLI Assistant converts your natural language requests into proper AWS CLI commands with real-time validation against your AWS environment.

## Features
✅ **Natural Language Processing** - Just describe what you want to do  
✅ **5 AWS Services** - S3, DynamoDB, EC2, Lambda, IAM  
✅ **Real-time Validation** - Commands tested against your actual AWS account  
✅ **3 Usage Modes** - MCP, Web Interface, Interactive CLI  
✅ **Instant Results** - Get command syntax and execution results immediately  

## Supported Operations

### S3 Operations
- List buckets
- Create buckets
- Delete buckets
- List objects in bucket

### DynamoDB Operations
- List tables
- Describe table
- Query table
- Scan table

### EC2 Operations
- List instances
- Describe instances
- Start/stop instances

### Lambda Operations
- List functions
- Invoke function
- Get function configuration

### IAM Operations
- List users
- List roles
- Get user details

## Installation

### Prerequisites
- Python 3.10 or higher
- AWS CLI configured with credentials
- Valid AWS account

### Quick Start

1. **Install from PyPI**
```bash
pip install aws-cli-assistant-lite
```

2. **Configure AWS credentials**
```bash
aws configure
```

3. **Choose your mode and start using:**

**MCP Mode (Claude Desktop):**
```bash
aws-cli-assistant --mode mcp
```
Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "aws-cli-assistant-lite": {
      "command": "aws-cli-assistant",
      "args": ["--mode", "mcp"],
      "env": {
        "AWS_REGION": "us-west-1"
      }
    }
  }
}
```

**Web Interface Mode:**
```bash
aws-cli-assistant --mode web
# Visit http://127.0.0.1:8000
```

**Interactive CLI Mode:**
```bash
aws-cli-assistant --mode cli
```

## Usage Modes

### 🔗 MCP Mode (Claude Desktop Integration)
```bash
aws-cli-assistant --mode mcp  # Default mode
```
- Integrates directly with Claude Desktop
- No user interaction needed
- Configure once in Claude settings

### 🌐 Web Interface Mode
```bash
aws-cli-assistant --mode web
```
- Opens web interface at http://127.0.0.1:8000
- Simple HTML form for testing
- REST API endpoints available

### 💻 Interactive CLI Mode
```bash
aws-cli-assistant --mode cli
```
**Example session:**
```
Enter your request: list my s3 buckets

📋 Generated Command: aws s3 ls
💡 Explanation: Lists all S3 buckets in your account
✅ Validation: Found 19 buckets

Execute this command? (y/n): y

⚡ Executing: aws s3 ls
✅ Success!
2023-01-15 12:34:56 my-bucket-1
2023-01-15 12:34:56 my-bucket-2
```

## Usage Examples

### Example 1: List S3 Buckets
**Input:** "list all my s3 buckets"  
**Output:** `aws s3 ls`  
**Validation:** ✅ Valid - Found 19 buckets

### Example 2: List Lambda Functions
**Input:** "show me lambda functions"  
**Output:** `aws lambda list-functions --region us-west-1`  
**Validation:** ✅ Valid - Found 11 functions

### Example 3: List DynamoDB Tables
**Input:** "list dynamodb tables"  
**Output:** `aws dynamodb list-tables`  
**Validation:** ✅ Valid - Found 4 tables

## Architecture

```
User Input (Natural Language)
    ↓
NLP Transformer Model
    ↓
AWS CLI Command Generation
    ↓
Boto3 Validation (Real AWS)
    ↓
Result + Validation Status
```

## API Reference

### Web Mode Endpoints

**POST /generate** - Convert natural language to AWS CLI
```bash
curl -X POST http://127.0.0.1:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"query": "list my s3 buckets"}'
```

**Response:**
```json
{
  "command": "aws s3 ls",
  "explanation": "Lists S3 buckets in your account",
  "validation": {
    "intent": "list_s3_buckets",
    "region": "us-west-1",
    "status": "valid",
    "reason": "Listed buckets",
    "detail": { "buckets": [...] }
  }
}
```

**GET /health** - Service health check
**GET /services** - List supported services  
**GET /** - Web interface

### MCP Mode Functions

- `generate_aws_cli(query: str)` - Main conversion function
- `health_check()` - Service status
- `list_supported_services()` - Available services

## Configuration

### Environment Variables
```bash
AWS_REGION=us-west-1          # Your preferred AWS region
AWS_PROFILE=default           # AWS profile to use
MCP_PORT=3000                 # Server port (optional)
```

### Custom Settings
Edit `config.yaml`:
```yaml
services:
  - s3
  - dynamodb
  - ec2
  - lambda
  - iam

validation:
  enabled: true
  timeout: 30

model:
  type: local-transformer
  cache_size: 1000
```

## Pricing

**Lite Edition:** $49/month or $500 one-time purchase

**Includes:**
- 5 AWS services
- 100 queries per day
- Email support
- Monthly updates

**Need more?** Contact us about Pro Edition (15+ services, unlimited queries)

## Support

- **Email:** aws2minutes@gmail.com
- **Documentation:** https://docs.yourdomain.com
- **Issues:** https://github.com/yourrepo/issues

## FAQ

**Q: Does this work with all AWS regions?**  
A: Yes, specify your region in AWS configuration.

**Q: Can I use this with multiple AWS accounts?**  
A: Lite edition supports one account. Pro edition supports multiple.

**Q: Is my AWS data secure?**  
A: Yes, all processing is local. We never store your AWS credentials or data.

**Q: What happens if I exceed 100 queries/day?**  
A: Service pauses until next day. Upgrade to Pro for unlimited queries.

## Roadmap

**Coming in Q1 2026:**
- RDS support
- CloudFormation support
- Cost estimation
- Batch operations

## License

Commercial License - See LICENSE.txt

## About

Created by [Malini Agrawal] - AWS Certified Solutions Architect & Developer  
Transitioned from Banking & Finance to AWS Cloud Engineering in 2021

---

**Ready to simplify your AWS CLI experience?**  

```bash
pip install aws-cli-assistant-lite
aws-cli-assistant --mode cli  # Start interactive mode
```

**Choose your preferred mode:**
- `--mode mcp` - Claude Desktop integration
- `--mode web` - Web interface  
- `--mode cli` - Interactive command line