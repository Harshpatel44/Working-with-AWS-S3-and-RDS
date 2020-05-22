import boto3
s3Client = boto3.client('s3',region_name='us-east-1')

s3Client.put_public_access_block(
    Bucket = "fourth-bucket-csci-5410",
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True,
        'BlockPublicPolicy': True,
        'RestrictPublicBuckets': True
    },
)