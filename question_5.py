from fastapi import File
import boto3
from botocore.exceptions import NoCredentialsError
import traceback
    
async def upload_to_aws(
    file: File,
):   
    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AWS_access_key",
        aws_secret_access_key="AWS_secret_access_key"
    )
    bucket = "BuketName"
    path = "PathName"
    filename = ""
    upload_file = ""
    try:
        upload_file = file['file_path']
        filename = file['file_name']
        s3_client.upload_file(
            upload_file, bucket, path + filename
        )
        
        return True, filename, bucket, path    
    except FileNotFoundError:
        print("The file was not found")
        return False, None, None, None
    except NoCredentialsError:
        print("Credentials not available")
        return False, None, None, None

upload_to_aws("Python_test.pdf")



