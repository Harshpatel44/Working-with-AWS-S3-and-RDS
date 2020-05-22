import boto3

"""Get name of the buckets"""
# s3 = boto3.client('s3')
# print(s3.list_buckets())



"""Upload a file"""
# s3Resource = boto3.resource('s3')
# s3Resource.Object('first-bucket-csci-5410','harsh.txt').upload_file(Filename='harsh.txt')



"""Creating another bucket"""
# s3Resource = boto3.resource('s3')
# s3Resource.create_bucket(Bucket="fifth-bucket-csci-5410",)

"""No Public Access"""
# s3Client = boto3.client('s3',region_name='us-east-1')
# # s3Client.put_public_access_block(
# #     Bucket = "second-bucket-csci-5410",
# #     PublicAccessBlockConfiguration={
# #         'BlockPublicAcls': True,
# #         'IgnorePublicAcls': True,
# #         'BlockPublicPolicy': True,
# #         'RestrictPublicBuckets': True
# #     },
# # )


"""get ACL permissions"""
s3Client = boto3.client('s3')
json_file=s3Client.get_bucket_acl(Bucket='second-bucket-csci-5410')
json_file.pop('ResponseMetadata')
json_file['Grants'][0]['Permission']='READ'
s3Client.put_bucket_acl( Bucket='second-bucket-csci-5410', AccessControlPolicy=json_file)

print(s3Client.get_bucket_acl(Bucket='second-bucket-csci-5410'))





