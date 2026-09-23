#import packages
import requests
import os
import json
from datetime import datetime
import time

#define the variables that allow us to call the API
url = 'https://api.tfl.gov.uk/BikePoint/'

#Create a folder for our extracted data if it doesn't already exist. exist_ok is a premade parameter
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

#Create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

# set up retry settings in case the API fails
max_retry = 5
attempt = 0
delay = 10

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

        #handle errors that occur while creating or writing to the file
            except Exception as e:
                print(f'An error has occurred: {e}')
            break

        #API request succeeded but no data was returned
        else:
            print('No data returned')
            break

    #Write the elif statement - for the server or client side errors
    elif status < 200 or status >= 500:
        time.sleep(delay)
        attempt +=1
        print(f'Status code:{status}.Retrying. Attempt number {attempt}')


    else:
        print(f'Error. Status code {status}. Fix it')
        break

    #print the status code to see if the API call has worked. From the response, get the status code
    #    print(response.status_code)