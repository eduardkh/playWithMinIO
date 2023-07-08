from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error
import os
import json

# Load the environment variables from the .env file.
load_dotenv()

MINIO_CONNECTION_STRING = os.getenv('MINIO_CONNECTION_STRING')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')

try:
    minioClient = Minio(MINIO_CONNECTION_STRING,
                        access_key=MINIO_ACCESS_KEY,
                        secret_key=MINIO_SECRET_KEY,
                        secure=False)
    # Create a new bucket.
    minioClient.make_bucket("dj-site-w-policy1", location="us-east-1")

    # Create bucket Policy.
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::dj-site-w-policy1/*"
            }
        ]
    }

    minioClient.set_bucket_policy("dj-site-w-policy1", json.dumps(policy))

except S3Error as err:
    print(err)
