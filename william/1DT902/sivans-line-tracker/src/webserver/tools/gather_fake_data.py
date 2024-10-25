import requests
import json
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

def generate_fake_data(start_date, end_date):
    current_date = start_date

    while current_date < end_date:
        length = round(random.randint(0, 6))
        yield length, current_date
        current_date += timedelta(minutes=5)

# Set start and end date
start_date = datetime(2024, 1, 6, 21, 0)
end_date = datetime(2024, 1, 7, 0, 0)

# Specify the API endpoint
api_endpoint = 'http://server.alfredsson.xyz/upload'

# Set headers
headers = {'Content-Type': 'application/json'}

# Generate fake data and send POST requests
fake_data_generator = generate_fake_data(start_date, end_date)

for data_point in fake_data_generator:
    length, date = data_point
    data = {'length': length, 'date': str(date.strftime('%Y-%m-%d %H:%M:%S'))}
    json_data = json.dumps(data)
    response = requests.patch(api_endpoint, json=data, headers=headers)
    
    # Print the response status code
    print(f"Length: {length}, Date: {date}, Response Code: {response}")
