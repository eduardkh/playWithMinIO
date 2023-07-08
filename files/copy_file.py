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

    # Copy a file.
    source = CopySource("dj-site", "index.html")
    minioClient.copy_object("dj-site-w-policy1", "copied_index.html", source)

except S3Error as err:
    print(err)
