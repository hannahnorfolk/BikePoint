#import packages
import requests
import os
import json
from datetime import datetime
import time
import logging

#defining logger function. We don't have to set it up because its in the main script
logger = logging.getLogger(__name__)

def extract_json(url:str, data_dir:str, timestamp:str, max_retry:int, delay:int):
    """Extracts JSON from specified URL amd saves it locally in the data_dir

    Args:
        url (str): The URL you want to download JSON from
        data_dir (str): The folder you want the JSON to be saved to
        timestamp (str): This will be the filename
        max_retry (int): Maximum number of attempts to call the API if there is an error.
        delay (int): Duration in seconds to wait between attempts
    """
    #define the variables that allow us to call the API

    #Create a folder for our extracted data if it doesn't already exist. exist_ok is a premade parameter
    os.makedirs(data_dir, exist_ok = True)

    #Create a timestamp so each extract gets a unique filename
    filename = f'{data_dir}/{timestamp}.json'

    # set up retry settings in case the API fails
    attempt = 0
    # Keep trying until the maximum number of attempts is reached

    while attempt < max_retry:
            
        #send the GET request to the API to see if it works
        response = requests.get(url)

        # Get Status
        status = response.status_code

        #Write an if statement based on the status code
        if 200 <= status < 300:
            #Convert the JSON response into python variable
            data = response.json()

            # Check that the API returned data before trying to save it
            if len(data)>0:
                try:

                    # Open the output file and write the API data to it as JSON
                    with open(filename, 'w') as file:
                        json.dump(data,file)

                # print the success comment, and break out the while loop
                    print(f'{filename} was successfully saved. Yipee!')
                    logger.info(f'{filename} was successfully saved. Yipee!')

            #handle errors that occur while creating or writing to the file
                except Exception as e:
                    print(f'An error has occurred: {e}')
                    logger.error(f'An error has occurred: {e}')
                break

            #API request succeeded but no data was returned
            else:
                print('No data returned')
                logger.warning('No data returned')
                break

        #Write the elif statement - for the server or client side errors
        elif status < 200 or status >= 500:
            time.sleep(delay)
            attempt +=1
            print(f'Status code:{status}.Retrying. Attempt number {attempt}')
            logger.info(f'Status code:{status}.Retrying. Attempt number {attempt}')
            
        else:
            print(f'Error. Status code {status}. Fix it')
            logger.critical(f'Error. Status code {status}. Fix it')
            break