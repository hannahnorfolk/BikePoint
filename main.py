#Packages
from datetime import datetime

#Modules
from Modules.log_initialise import setup_logging
from Modules.extract import extract_json

##Logging
logger = setup_logging('log', timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
logger.info('Logger successfully initialised.')

##Extract Parameters
url = 'https://api.tfl.gov.uk/BikePoint/' #api link
max_retry = 5
delay = 10
data_dir = 'data' # folder
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
extract_json(url,data_dir, timestamp, max_retry, delay)