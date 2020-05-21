import boto3

# """Get name of the buckets"""
# s3 = boto3.client('s3')
# print(s3.list_buckets())
#
#
# """Upload a file"""
# s3Resource = boto3.resource('s3')
# s3Resource.Object('first-bucket-csci-5410','harsh.txt').upload_file(Filename='harsh.txt')

"""Creating another bucket"""
s3Resource = boto3.resource('s3')
s3Resource.create_bucket(Bucket="second-bucket-csci-5410",)



# """get ACL permissions"""
# s3Client = boto3.client('s3')
# print(s3Client.get_bucket_acl(Bucket='second-bucket-csci-5410'))
#


"""set policy to block public access"""
import json
s3Client = boto3.client('s3')
policy={
  "Id": "Policy1590045787132",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1590045784956",
      "Action": [
        "s3:PutPublicAccessBlock"
      ],
      "Effect": "allow",
      "Resource": "arn:aws:s3:::second-bucket-csci-5410",
      "Principal": "*"
    }
  ]
}

policy=json.dumps(policy)

s3Client.put_bucket_policy(Bucket='second-bucket-csci-5410',Policy=policy)


