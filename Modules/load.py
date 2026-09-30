#import necessary packages
import os
import boto3 #pip install needed 
import logging

#defining logger function. We don't have to set it up because its in the main script
logger = logging.getLogger(__name__)

def load_to_s3(data_dir:str, AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str):
    """Uploads all files in the folder to S3

    Args:
        data_dir (str): What folder the data is in
        AWS_ACCESS_KEY (str): Linked to AWS IAM User
        AWS_SECRET_ACCESS_KEY (str): Linked to AWS IAM User
        AWS_BUCKET_NAME (str): S3 bucket to uplaod
    """
    #connecting to the AWS user
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    #set up upload file variables for bucket. So we know what file to upload and how we want it to be placed in the bucket
    files_to_upload = os.listdir('data')  # the files we extracted that we would like to upload to s3

    #plan: loop through anything in the data folder and push it to the s3 bucket. then delete the files locally

    for file in files_to_upload:
        file_to_upload = f'{data_dir}/{file}' #one file we extracted that we would like to upload to s3
        try:
            #file_to_upload = the file we extracted that we would like to upload to s3
            #file = what we want the file to appear as in s3
            #files_to_upload = all the files we extracted that we want to uplod to s3

            s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,file)
            
            print(f'{file} has uploaded successfully.')
            logger.info(f'{file} has uploaded successfully')
            os.remove(file_to_upload)
        except Exception as e:
            print(f'An error has occurred. {e}')
            logger.error(f'An error has occurred. {e}')
            