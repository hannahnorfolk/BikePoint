#import necessary packages
import os
import boto3 #pip install needed 
from dotenv import load_dotenv #pip install needed 

#load_dotenv stuff to activate .env
load_dotenv()

#authentication. getting all the user authentication stuff over
AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

#set up s3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

#set up upload file variables
file_to_upload = 'data/2026-09-28 10-43-27.json'
filename_s3 = '2026-09-28 10-43-27.json'

s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,filename_s3)
