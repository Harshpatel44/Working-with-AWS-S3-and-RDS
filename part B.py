import boto3

class s3Api:

    """ Get name of the buckets """
    def listBuckets(self):
        s3 = boto3.client('s3')
        return s3.list_buckets()

    """ Upload a file """
    def fileUpload(self,bucketName,sourceFileName,fileName):
        s3Resource = boto3.resource('s3')
        s3Resource.Object(bucketName,sourceFileName).upload_file(Filename=fileName)
        print('file uploaded')

    """ Creating another bucket """
    def createBucket(self,bucketName):
        s3Resource = boto3.resource('s3')
        s3Resource.create_bucket(Bucket=bucketName, )
        print('Bucket created')

    """ Change bucket access (private, public etc) """
    def manageBucketAccess(self,bucketName,blockPublicAcls=True,ignorePublicAcls=True,blockPublicPolicy=True,restrictPublicBuckets=True,region='us-east-1'):
        s3Client = boto3.client('s3',region_name=region)
        s3Client.put_public_access_block(
            Bucket = bucketName,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': blockPublicAcls,
                'IgnorePublicAcls': ignorePublicAcls,
                'BlockPublicPolicy': blockPublicAcls,
                'RestrictPublicBuckets': restrictPublicBuckets
            },
        )
        print('Access Changed')

    """ Get ACL permissions """
    def getAclPermissions(self,bucketName):
        s3Client = boto3.client('s3')
        return s3Client.get_bucket_acl(Bucket=bucketName)

    """ Set ACL permissions """
    def changeAclPermissions(self,bucketName,permission):
        s3Client = boto3.client('s3')
        json_file=s3Client.get_bucket_acl(Bucket=bucketName)
        json_file.pop('ResponseMetadata')
        json_file['Grants'][0]['Permission']=permission
        s3Client.put_bucket_acl( Bucket=bucketName, AccessControlPolicy=json_file)
        print('ACL permission changed')


s3 = s3Api()
s3.listBuckets()
s3.fileUpload("first-bucket-csci-5410","harsh.txt","harsh.txt")
s3.createBucket("second-bucket-csci-5410")
s3.manageBucketAccess("second-bucket-csci-5410")
s3.getAclPermissions("second-bucket-csci-5410")
s3.changeAclPermissions("second-bucket-csci-5410","READ")




