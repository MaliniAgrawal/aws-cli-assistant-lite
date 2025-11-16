# AWS CLI Assistant - Quick Start Tutorial
## Get Started in 5 Minutes

Welcome! This tutorial will get you up and running with AWS CLI Assistant in just 5 minutes.

---

## Tutorial Overview

**What you'll learn:**
1. Basic natural language commands
2. Understanding validation results
3. Common operations for each service
4. Best practices

**Time required:** 5-10 minutes

---

## Step 1: Your First Command (1 minute)

Let's start with the simplest operation - listing your S3 buckets.

### Natural Language Input:
```
list my s3 buckets
```

### What You'll Get:
```json
{
  "command": "aws s3 ls",
  "explanation": "Lists S3 buckets in your account",
  "validation": {
    "intent": "list_s3_buckets",
    "region": "us-west-1",
    "status": "valid",
    "reason": "Listed buckets",
    "detail": {
      "buckets": ["my-app-bucket", "backup-bucket", "logs-bucket"]
    }
  }
}
```

### Understanding the Response:
- **command**: The actual AWS CLI command
- **explanation**: What the command does
- **validation.status**: Whether command is valid
- **validation.detail**: Actual results from your AWS account

✅ **Success!** You just converted natural language to AWS CLI!

---

## Step 2: Working with S3 (2 minutes)

### Operation 1: List Buckets
**Input:** `show all s3 buckets`  
**Command:** `aws s3 ls`

### Operation 2: Create Bucket
**Input:** `create s3 bucket named my-new-bucket`  
**Command:** `aws s3 mb s3://my-new-bucket --region us-west-1`

### Operation 3: List Objects in Bucket
**Input:** `list files in bucket my-app-bucket`  
**Command:** `aws s3 ls s3://my-app-bucket`

### Operation 4: Delete Bucket
**Input:** `delete s3 bucket my-old-bucket`  
**Command:** `aws s3 rb s3://my-old-bucket`

**💡 Pro Tip:** Be specific with bucket names for create/delete operations.

---

## Step 3: Lambda Functions (2 minutes)

### Operation 1: List All Functions
**Input:** `show my lambda functions`  
**Command:** `aws lambda list-functions --region us-west-1`

**Result:**
```json
{
  "functions": [
    "my-api-handler",
    "data-processor",
    "image-resizer"
  ]
}
```

### Operation 2: Get Function Details
**Input:** `describe lambda function my-api-handler`  
**Command:** `aws lambda get-function --function-name my-api-handler`

### Operation 3: Invoke Function
**Input:** `invoke lambda function my-api-handler`  
**Command:** `aws lambda invoke --function-name my-api-handler output.json`

**💡 Pro Tip:** Use descriptive function names in your queries.

---

## Step 4: DynamoDB Tables (2 minutes)

### Operation 1: List Tables
**Input:** `list dynamodb tables`  
**Command:** `aws dynamodb list-tables`

**Result:**
```json
{
  "tables": ["Users", "Products", "Orders"]
}
```

### Operation 2: Describe Table
**Input:** `describe dynamodb table Users`  
**Command:** `aws dynamodb describe-table --table-name Users`

### Operation 3: Scan Table
**Input:** `scan dynamodb table Users`  
**Command:** `aws dynamodb scan --table-name Users`

**💡 Pro Tip:** Be careful with scan operations on large tables - they can be slow and expensive.

---

## Step 5: EC2 Instances (2 minutes)

### Operation 1: List Instances
**Input:** `show all ec2 instances`  
**Command:** `aws ec2 describe-instances`

### Operation 2: List Running Instances
**Input:** `show running ec2 instances`  
**Command:** `aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"`

### Operation 3: Start Instance
**Input:** `start ec2 instance i-1234567890abcdef0`  
**Command:** `aws ec2 start-instances --instance-ids i-1234567890abcdef0`

### Operation 4: Stop Instance
**Input:** `stop ec2 instance i-1234567890abcdef0`  
**Command:** `aws ec2 stop-instances --instance-ids i-1234567890abcdef0`

**⚠️ Warning:** Starting/stopping instances affects your running applications!

---

## Step 6: IAM Users (1 minute)

### Operation 1: List Users
**Input:** `show iam users`  
**Command:** `aws iam list-users`

### Operation 2: Get User Details
**Input:** `describe iam user john-doe`  
**Command:** `aws iam get-user --user-name john-doe`

### Operation 3: List User Groups
**Input:** `show groups for user john-doe`  
**Command:** `aws iam list-groups-for-user --user-name john-doe`

**💡 Pro Tip:** IAM operations require elevated permissions.

---

## Common Patterns

### Pattern 1: List Operations
All services support listing:
- `list s3 buckets`
- `list dynamodb tables`
- `list lambda functions`
- `list ec2 instances`
- `list iam users`

### Pattern 2: Describe/Get Operations
Get details about specific resources:
- `describe dynamodb table <name>`
- `describe ec2 instance <id>`
- `get lambda function <name>`
- `get iam user <username>`

### Pattern 3: Create/Delete Operations
Manage resources:
- `create s3 bucket <name>`
- `delete s3 bucket <name>`
- `create dynamodb table <name>`

---

## Understanding Validation Status

### ✅ Valid
```json
{
  "status": "valid",
  "reason": "Listed buckets",
  "detail": { "buckets": [...] }
}
```
**Meaning:** Command executed successfully, results returned.

### ⚠️ Invalid
```json
{
  "status": "invalid",
  "reason": "403",
  "detail": {}
}
```
**Meaning:** Command syntax correct but execution failed (permissions, non-existent resource, etc.)

### ❌ Error
```json
{
  "status": "error",
  "reason": "Unable to parse query"
}
```
**Meaning:** Unable to understand the natural language query.

---

## Best Practices

### ✅ DO:
1. **Be specific** - "list s3 buckets in us-west-1" vs "show buckets"
2. **Use proper names** - Include exact bucket/function/table names
3. **Check validation** - Always review the validation status
4. **Start simple** - Begin with list operations before modify operations
5. **Test safely** - Use non-production resources for testing

### ❌ DON'T:
1. **Be vague** - "show me stuff" won't work well
2. **Delete without checking** - Verify resource names before deletion
3. **Ignore errors** - Read error messages carefully
4. **Exceed limits** - Lite edition has 100 queries/day limit
5. **Share credentials** - Keep AWS keys secure

---

## Real-World Examples

### Example 1: Morning DevOps Routine
```bash
# Check all services status
"show all s3 buckets"
"list running ec2 instances"
"show lambda functions"
"list dynamodb tables"
```

### Example 2: Debugging Lambda
```bash
# Investigate function issue
"show lambda functions"
"describe lambda function my-api-handler"
"check cloudwatch logs for my-api-handler"  # Coming in Pro
```

### Example 3: Resource Audit
```bash
# Audit AWS resources
"list all s3 buckets"
"list all ec2 instances"
"show all iam users"
"list dynamodb tables"
```

### Example 4: Cleanup Old Resources
```bash
# Safe cleanup process
"list s3 buckets"  # Review list
"list objects in bucket old-backup"  # Check contents
"delete s3 bucket old-backup"  # Remove if empty
```

---

## Troubleshooting Quick Tips

### Query Not Understood?
**Try:**
- Simplify your query
- Use service name explicitly: "list **s3** buckets"
- Check spelling
- Use keywords: list, show, describe, create, delete

### Permission Denied?
**Check:**
- AWS credentials configured correctly
- IAM user has required permissions
- Resource exists in your account
- Correct region specified

### Slow Response?
**Reasons:**
- First query loads model (10-15 seconds)
- Large result sets (thousands of resources)
- AWS API rate limiting
- Network latency

---

## Next Steps

**Completed the tutorial? You're ready to:**

1. **Explore Advanced Usage**
   - Read the [User Guide](USER_GUIDE.md)
   - Try [Complex Examples](EXAMPLES.md)

2. **Optimize Your Workflow**
   - Create custom shortcuts
   - Integrate with your scripts
   - Set up automation

3. **Get Support**
   - Join [Community Forum](https://community.yourdomain.com)
   - Email: support@yourdomain.com
   - Check [FAQ](FAQ.md)

4. **Upgrade to Pro** (when needed)
   - Unlimited queries
   - 15+ AWS services
   - Priority support
   - Cost estimation
   - Batch operations

---

## Quick Reference Card

| **Operation** | **Example Query** | **AWS CLI Output** |
|---------------|-------------------|-------------------|
| List S3 | `list s3 buckets` | `aws s3 ls` |
| List Lambda | `show lambda functions` | `aws lambda list-functions` |
| List DynamoDB | `list dynamodb tables` | `aws dynamodb list-tables` |
| List EC2 | `show ec2 instances` | `aws ec2 describe-instances` |
| List IAM | `show iam users` | `aws iam list-users` |

**Print this card** for quick reference!

---

## Feedback

**How was this tutorial?**
- Email: feedback@yourdomain.com
- Rate: [Tutorial Feedback Form](https://forms.yourdomain.com/quickstart)

Your feedback helps us improve!

---

**🎉 Congratulations! You're now ready to use AWS CLI Assistant effectively.**

Start simplifying your AWS workflows today!