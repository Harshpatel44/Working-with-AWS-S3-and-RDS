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
#print(s3Client.get_bucket_acl(Bucket='second-bucket-csci-5410'))

"""Set ACL permissions"""
s3Client.put_bucket_acl(
    Bucket='second-bucket-csci-5410',
    AccessControlPolicy={
        'Grants': [
            {
                'Grantee': {
                    'DisplayName': 'awslabsc0w758896t1588300632',
                    # 'EmailAddress': '',
                    'ID': '303d17372927d47a314483c707fd247cacfb8334cbbb190f9477a980ffdf3c5a',
                    'Type': 'CanonicalUser',
                    # 'URI': 'string'
                },
                'Permission': 'READ_ACP'
            },
        ],
        'Owner': {
            'DisplayName': 'awslabsc0w758896t1588300632',
            'ID': '303d17372927d47a314483c707fd247cacfb8334cbbb190f9477a980ffdf3c5a'
        }
    },
)
print(s3Client.get_bucket_acl(Bucket='second-bucket-csci-5410'))





