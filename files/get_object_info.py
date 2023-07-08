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

    # Get object info.
    info = minioClient.stat_object("dj-site", "index.html")

    # Get and print the metadata of the object.
    # print("Metadata: ", info.metadata)

    # Get and print object name.
    print("Object Name: ", info.object_name)

    # Get and print object size.
    print("Object Size: ", info.size)

    # Get and print the ETag of the object.
    print("ETag: ", info.etag)

    # Get and print the last modified time of the object.
    print("Last Modified: ", info.last_modified)

    # Get and print the content type of the object.
    print("Content Type: ", info.content_type)

    # Get and print whether the object is a directory.
    print("Is Directory: ", info.is_dir)


except S3Error as err:
    print(err)
