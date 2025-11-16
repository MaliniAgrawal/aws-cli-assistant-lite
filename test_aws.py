import boto3

print("Testing AWS connectivity...")

try:
    s3 = boto3.client('s3')
    print("✅ AWS credentials configured")
    
    buckets = s3.list_buckets()
    print(f" Found {len(buckets['Buckets'])} S3 buckets")
    
    # List first 5 bucket names
    for i, bucket in enumerate(buckets['Buckets'][:5]):
        print(f"   - {bucket['Name']}")
    
    if len(buckets['Buckets']) > 5:
        print(f"   ... and {len(buckets['Buckets']) - 5} more")
    
    print("\n AWS connectivity test passed!")
    
except Exception as e:
    print(f" AWS connection failed: {e}")
    print("\nTroubleshooting:")
    print("1. Run: aws configure")
    print("2. Check credentials file exists: ~/.aws/credentials")

