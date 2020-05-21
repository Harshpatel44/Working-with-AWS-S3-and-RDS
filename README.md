<h2>Serverless-Data-Processing-A1</h2>
<p><i>This repository contains the A1 solutions of Course "Serverless Data Processing"</i></p>

<p>1. First I created the bucket with all public permissions, so I can use it freely the first time and to get it working.</p>
<p>2. I tried creating an IAM user and gave it programming access to connect python program to the bucket. tried creatign the first user but, it throws some error and can not create users succesfully. Then I found that, all the access ID and shared key and other credentials are provided by AWS educate on their workbench. We need to click on account details and fetch the credentials.</p>
<p>3. I got to know later that we need to paste all those credentials in a folder C:/users/username/.aws/credentials file, and then it worked.</p>



<h2>References</h2>
<p><i>https://docs.ceph.com/docs/master/radosgw/s3/python/</i></p>
<p><i>https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html</i></p>
<p><i>https://realpython.com/python-boto3-aws-s3/#creating-a-bucket</i></p>
