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
# s3Client = boto3.client('s3')
# print(s3Client.get_bucket_acl(Bucket='second-bucket-csci-5410'))



"""set policy to block public access"""
import json
#s3Client = boto3.resource('s3')
#s3Client = boto3.client('s3')

#
# policy={
#   "Id": "Policy1590045787132",
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Sid": "Stmt1590045784956",
#       "Action": [
#         "s3:PutPublicAccessBlock"
#       ],
#       "Effect": "Deny",
#       "Resource": "arn:aws:s3:::fifth-bucket-csci-5410",
#       "Principal": "*"
#     }
#   ]
# }
# policy=json.dumps(policy)
# s3Client.put_bucket_policy(Bucket='fifth-bucket-csci-5410',Policy=policy)

# response = s3Client.get_public_access_block(Bucket='second-bucket-csci-5410')
# print(response)
#


"""ACL"""

# s3Client = boto3.client('s3')
# policy={
#     "Version": "2012-10-17",
#     "Id": "Policy1590103199246",
#     "Statement": [
#         {
#             "Sid": "Stmt1590103198148",
#             "Effect": "Allow",
#             "Principal": "*",
#             "Action": "*",
#             "Resource": "arn:aws:s3:::second-bucket-csci-5410"
#         }
#     ]
# }
# policy=json.dumps(policy)
# s3Client.put_bucket_policy(Bucket='second-bucket-csci-5410',Policy=policy)
#s3Client.put_bucket_acl(Bucket='second-bucket-csci-5410', ACL='private')






# s3Client = boto3.client('s3')
# response = s3Client.put(
#     ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
#     AccessControlPolicy={
#         'Grants': [
#             {
#                 'Grantee': {
#                     'DisplayName': 'string',
#                     'EmailAddress': 'string',
#                     'ID': 'string',
#                     'Type': 'CanonicalUser'|'AmazonCustomerByEmail'|'Group',
#                     'URI': 'string'
#                 },
#                 'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
#             },
#         ],
#         'Owner': {
#             'DisplayName': 'string',
#             'ID': 'string'
#         }
#     },
#     GrantFullControl='string',
#     GrantRead='string',
#     GrantReadACP='string',
#     GrantWrite='string',
#     GrantWriteACP='string'
# )