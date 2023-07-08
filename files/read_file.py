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

    # Get a file from the bucket.
    data = minioClient.get_object('dj-site', 'index.html')

    # Write the data to a file.
    with open('downloaded_index.html', 'wb') as file_data:
        for d in data.stream(32*1024):
            file_data.write(d)

except S3Error as err:
    print(err)
