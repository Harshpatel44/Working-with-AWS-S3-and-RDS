<h2>Serverless-Data-Processing-A1</h2>
<p><i>This repository contains the A1 solutions of Course "Serverless Data Processing"</i></p>

<p>1. First I created the bucket with all public permissions, so I can use it freely the first time and to get it working.</p>
<p>2. I tried creating an IAM user and gave it programming access to connect python program to the bucket. tried creatign the first user but, it throws some error and can not create users succesfully. Then I found that, all the access ID and shared key and other credentials are provided by AWS educate on their workbench. We need to click on account details and fetch the credentials.</p>
<p>3. I got to know later that we need to paste all those credentials in a folder C:/users/username/.aws/credentials file, and then it worked.</p>
<p>4. After creating another bucket, I had to block the public access of that bucket. I searched and found about policies. I created a policy which did not work. Then I looked over the buckets in AWS and found a policy generator which helped.
<p>5. We need to change the credentials each time we open the aws educate again.
<p>6. I tried with policy but that did not work out. Then finally I got a function "put_public_access_block" in the s3 boto documentation which did the job.</p>
<p>7. We changed the ACL settings using the function "put_bucket_acl". I fetched the json file from "get_bucket_acl" and modified it so that to eliminate write access to root user as required. Then I set is using "put_bucket_acl" function.


<h2>References</h2>
<p><i>https://docs.ceph.com/docs/master/radosgw/s3/python/</i></p>
<p><i>https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html</i></p>
<p><i>https://realpython.com/python-boto3-aws-s3/#creating-a-bucket</i></p>
<p><i>https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_public_access_block</i></p>
