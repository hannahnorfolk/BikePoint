#Packages
from datetime import datetime
import os

#Modules
from Modules.log_initialise import setup_logging
from Modules.extract import extract_json
from Modules.load import load_to_s3
from dotenv import load_dotenv

##Logging
logger = setup_logging('log', timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
logger.info('Logger successfully initialised.')

##Extract Parameters
url = 'https://api.tfl.gov.uk/BikePoint/' #api link
max_retry = 5
delay = 10
data_dir = 'data' # folder
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#Extract execution
extract_json(url,data_dir, timestamp, max_retry, delay)

#Load Parameters
load_dotenv()
#stating all the user authentication up from the .env file
AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

load_to_s3(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME)
