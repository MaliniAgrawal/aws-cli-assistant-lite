# AWS CLI Assistant - Usage Modes

After installing from PyPI, you can use AWS CLI Assistant in three different modes:

## 🔗 MCP Mode (Default)
**For Claude Desktop integration**
```bash
aws-cli-assistant
# or explicitly
aws-cli-assistant --mode mcp
```
- Runs MCP server for Claude Desktop
- No user interaction needed
- Configure in `claude_desktop_config.json`

## 🌐 Web Mode
**HTTP server with web interface**
```bash
aws-cli-assistant --mode web
```
- Starts web server on http://127.0.0.1:8000
- Simple HTML interface for testing
- REST API endpoints: `/generate`, `/health`, `/services`

**Example API usage:**
```bash
curl -X POST http://127.0.0.1:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"query": "list my s3 buckets"}'
```

## 💻 CLI Mode
**Interactive command-line interface**
```bash
aws-cli-assistant --mode cli
```

**Example session:**
```
🚀 AWS CLI Assistant - Interactive Mode
Type 'exit' or 'quit' to stop, 'help' for supported services

Enter your request: list my s3 buckets

🔄 Processing: list my s3 buckets

📋 Generated Command: aws s3 ls
💡 Explanation: Lists all S3 buckets in your account
✅ Validation: Found 19 buckets

Execute this command? (y/n): y

⚡ Executing: aws s3 ls
✅ Success!
2023-01-15 12:34:56 my-bucket-1
2023-01-15 12:34:56 my-bucket-2

==================================================

Enter your request: _
```

## 🔧 Commands Reference

| Command | Description |
|---------|-------------|
| `help` | Show supported services |
| `exit`, `quit`, `q` | Exit CLI mode |
| `y`, `yes` | Execute generated command |
| `n`, `no` | Skip command execution |

## 🛡️ Safety Features

- **Validation**: All commands validated against your AWS account
- **Confirmation**: CLI mode asks before executing commands
- **Timeout**: 30-second execution limit
- **Error handling**: Clear error messages and recovery

## 📊 Supported Services

All modes support the same AWS services:
- **S3**: List/create/delete buckets, list objects
- **DynamoDB**: List/describe/query/scan tables  
- **EC2**: List/describe/start/stop instances
- **Lambda**: List/invoke functions, get configuration
- **IAM**: List users/roles, get user details

## 🔄 Migration from Previous Version

Old command still works for backward compatibility:
```bash
aws-cli-assistant --http  # Deprecated, use --mode web
```