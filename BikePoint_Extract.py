#import packages
import requests
import os
import json
from datetime import datetime

#define the variables that allow us to call the API
url = 'https://api.tfl.gov.uk/BikePoint/'

#Create a folder for our extracted data if it doesn't already exist. exist_ok is a premade parameter
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

#Create a timestamp so each extract gets a unique filename
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'

#send the GET request to the API to see if it works
response = requests.get(url)

# Get Status
status = response.status_code

#Write an if statement based on the status code

#Convert the JSON response into python variable
data = response.json()

# Open the output file and write the API data to it as JSON
with open(filename, 'w') as file:
    json.dump(data,file)

#print the status code to see if the API call has worked. From the response, get the status code
print(response.status_code)