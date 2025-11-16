# AWS CLI Assistant - Lite Edition
## Complete Installation Guide

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Pre-Installation Checklist](#pre-installation-checklist)
3. [Installation Steps](#installation-steps)
4. [Configuration](#configuration)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **Operating System:** Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum, 8GB recommended
- **Disk Space:** 500MB free space
- **Internet:** Required for AWS API calls

### Required Software
- Python 3.8+
- pip (Python package manager)
- AWS CLI v2
- Git (optional, for cloning repository)

---

## Pre-Installation Checklist

### ✅ Step 1: Verify Python Installation
```bash
python --version
# or
python3 --version
```
**Expected output:** Python 3.8.0 or higher

**Don't have Python?** Download from [python.org](https://www.python.org/downloads/)

### ✅ Step 2: Verify pip Installation
```bash
pip --version
# or
pip3 --version
```

### ✅ Step 3: Install/Verify AWS CLI
```bash
aws --version
```
**Expected output:** aws-cli/2.x.x or higher

**Don't have AWS CLI?**
- **Windows:** Download MSI installer from [AWS](https://aws.amazon.com/cli/)
- **macOS:** `brew install awscli`
- **Linux:** `sudo apt-get install awscli` or `sudo yum install awscli`

### ✅ Step 4: Configure AWS Credentials
```bash
aws configure
```
You'll need:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-west-1)
- Default output format (json recommended)

**Where to get credentials:**
1. Log into AWS Console
2. Go to IAM → Users → Your User → Security Credentials
3. Create Access Key

---

## Installation Steps

### Method 1: Using Package File (Recommended for customers)

#### Step 1: Download Package
```bash
# Download from AWS Marketplace or your distribution site
wget https://yourdomain.com/aws-cli-assistant-lite-v1.0.zip

# Or if provided via email/download link
# Extract the downloaded file
unzip aws-cli-assistant-lite-v1.0.zip
cd aws-cli-assistant-lite
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Expected packages:**
- boto3
- transformers
- torch
- fastapi (if using REST API mode)
- pydantic

#### Step 4: Verify Installation
```bash
python verify_installation.py
```

This script checks:
- Python version ✓
- Required packages ✓
- AWS credentials ✓
- AWS connectivity ✓

---

### Method 2: Using Git (For developers)

```bash
# Clone repository
git clone https://github.com/yourusername/aws-cli-assistant-lite.git
cd aws-cli-assistant-lite

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python verify_installation.py
```

---

## Configuration

### Basic Configuration

#### Step 1: Copy Configuration Template
```bash
cp config.template.yaml config.yaml
```

#### Step 2: Edit Configuration
Open `config.yaml` and customize:

```yaml
# AWS Configuration
aws:
  region: us-west-1          # Your primary AWS region
  profile: default           # AWS CLI profile name
  
# Service Configuration
services:
  enabled:
    - s3
    - dynamodb
    - ec2
    - lambda
    - iam
  
# Validation Settings
validation:
  enabled: true              # Enable real-time validation
  timeout: 30                # Timeout in seconds
  retry_attempts: 3
  
# Model Configuration
model:
  type: local-transformer
  cache_enabled: true
  cache_size: 1000           # Number of queries to cache
  
# Rate Limiting (Lite Edition)
limits:
  daily_queries: 100
  concurrent_requests: 5
  
# Logging
logging:
  level: INFO                # DEBUG, INFO, WARNING, ERROR
  file: logs/assistant.log
  max_size: 10MB
  backup_count: 5
```

### Advanced Configuration (Optional)

#### Multi-Region Support
```yaml
aws:
  regions:
    - us-west-1
    - us-east-1
    - eu-west-1
  default_region: us-west-1
```

#### Custom Endpoints (for LocalStack testing)
```yaml
aws:
  endpoints:
    s3: http://localhost:4566
    dynamodb: http://localhost:4566
```

---

## Verification

### Test 1: Health Check
```bash
python test_health.py
```
**Expected output:**
```json
{
  "status": "ok",
  "model": "local-transformer",
  "services": ["s3", "dynamodb", "ec2", "lambda", "iam"]
}
```

### Test 2: Simple Query
```bash
python test_query.py "list s3 buckets"
```
**Expected output:**
```json
{
  "command": "aws s3 ls",
  "explanation": "Lists S3 buckets in your account",
  "validation": {
    "status": "valid",
    "reason": "Listed buckets"
  }
}
```

### Test 3: MCP Server (If using with Claude)
```bash
# Start MCP server
python mcp_server.py
```

Then test connection from Claude Desktop.

---

## Troubleshooting

### Issue 1: "ModuleNotFoundError: No module named 'boto3'"
**Solution:**
```bash
pip install boto3
# or
pip install -r requirements.txt
```

### Issue 2: "AWS credentials not found"
**Solution:**
```bash
# Reconfigure AWS CLI
aws configure

# Or set environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-west-1
```

### Issue 3: "Connection timeout to AWS"
**Possible causes:**
- No internet connection
- AWS region is down (check AWS Status page)
- Firewall blocking outbound connections
- Incorrect AWS endpoint

**Solution:**
```bash
# Test AWS connectivity
aws s3 ls

# Try different region
aws s3 ls --region us-east-1
```

### Issue 4: "Permission denied" or "Access Denied"
**Solution:**
- Check IAM user has required permissions
- Minimum required permissions:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:ListBucket",
          "s3:ListAllMyBuckets",
          "dynamodb:ListTables",
          "ec2:DescribeInstances",
          "lambda:ListFunctions",
          "iam:ListUsers"
        ],
        "Resource": "*"
      }
    ]
  }
  ```

### Issue 5: Model loading errors
**Solution:**
```bash
# Clear cache and reinstall
rm -rf ~/.cache/huggingface
pip install --upgrade transformers torch
```

### Issue 6: Port already in use (MCP mode)
**Solution:**
```bash
# Find process using the port
# On Linux/Mac:
lsof -i :3000

# On Windows:
netstat -ano | findstr :3000

# Kill the process or change port in config.yaml
```

---

## Getting Help

### Support Channels
1. **Email Support:** support@yourdomain.com (Response: 24-48 hours)
2. **Documentation:** https://docs.yourdomain.com
3. **Community Forum:** https://community.yourdomain.com
4. **GitHub Issues:** https://github.com/yourrepo/issues

### When Reporting Issues
Please include:
- Operating system and version
- Python version (`python --version`)
- AWS CLI version (`aws --version`)
- Error message (full stack trace)
- Steps to reproduce
- Configuration file (remove sensitive data)

---

## Next Steps

✅ Installation complete? Great!

**Now you can:**
1. Read the [User Guide](USER_GUIDE.md) for detailed usage
2. Try the [Quick Start Tutorial](QUICKSTART.md)
3. Explore [Example Queries](EXAMPLES.md)
4. Join our [Community](https://community.yourdomain.com)

---

## License Activation

**Lite Edition requires activation:**
```bash
python activate_license.py --key YOUR-LICENSE-KEY
```

Your license key was provided:
- In purchase confirmation email
- On AWS Marketplace listing page
- In downloadable invoice

**Questions about licensing?** Contact sales@yourdomain.com

---

**Installation successful? Start using AWS CLI Assistant now!**

```bash
python mcp_server.py
```