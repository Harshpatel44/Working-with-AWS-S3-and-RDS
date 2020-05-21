import boto3

"""Get name of the buckets"""
s3 = boto3.client('s3')
print(s3.list_buckets())


"""Upload a file"""
s3Resource = boto3.resource('s3')
s3Resource.Object('first-bucket-csci-5410','harsh.txt').upload_file(Filename='harsh.txt')

