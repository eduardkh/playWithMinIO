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

    # Upload a file with metadata to the bucket.
    metadata = {"X-Amz-Meta-Testing": "1234", "example": "5678"}
    minioClient.fput_object('dj-site', 'index.html',
                            'index.html', metadata=metadata)


except S3Error as err:
    print(err)
