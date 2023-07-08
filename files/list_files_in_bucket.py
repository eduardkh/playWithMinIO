from dotenv import load_dotenv
from minio import Minio
from minio.commonconfig import CopySource
from minio.error import S3Error
import os

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

    # List files bucket.
    objects = minioClient.list_objects("dj-site")
    for obj in objects:
        print(obj.object_name)


except S3Error as err:
    print(err)
