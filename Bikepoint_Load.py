#import necessary packages
import os
import boto3 #pip install needed 
from dotenv import load_dotenv #pip install needed 

#load_dotenv stuff to activate .env
load_dotenv()

#stating all the user authentication up from the .env file
AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

#connecting to the AWS user
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

#set up upload file variables for bucket. So we know what file to upload and how we want it to be placed in the bucket
files_to_upload = os.listdir('data')  # the files we extracted that we would like to upload to s3

#linking the file to the s3 bucket.
# s3_client = linking the user detail
# upload_file = uploading it to the s3 bucket


#plan: loop through anything in the data folder and push it to the s3 bucket. then delete the files locally
for file in files_to_upload:
    file_to_upload = f'data/{file}' #one file we extracted that we would like to upload to s3
    try:
        #file_to_upload = the file we extracted that we would like to upload to s3
        #filename_s3 = what we want the file to appear as in s3
        #files_to_upload = all the files we extracted that we want to uplod to s3
        s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,file)
        
        print(f'{file} has uploaded successfully.')
        os.remove(file_to_upload)
    except Exception as e:
        print(f'An error has occurred. {e}')




