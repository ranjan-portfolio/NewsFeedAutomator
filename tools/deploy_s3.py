import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os
import json

load_dotenv()

def deploy_html_toS3(html:str)-> str:
    # AWS credentials (can also use environment variables or IAM roles)
    AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION=os.getenv("AWS_REGION")
    BUCKET_NAME=os.getenv("BUCKET_NAME")
    # Create S3 client
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    s3_bucket_policy={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::newsautomator.rancher-ranjanaws.com/*"
        }
    ]
   }
   

    try:
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key="index.html",
            Body=html,
            ContentType="text/html"
        )

        s3.put_bucket_policy(
            Bucket=BUCKET_NAME,
            Policy=json.dumps(s3_bucket_policy)
        )
        
        return f"✅ index.html uploaded to S3 bucket {BUCKET_NAME} successfully!"

    except FileNotFoundError:
        return "❌ File not found."
    except NoCredentialsError:
        return "❌ AWS credentials not available."
