import requests
import json

data = {'length': 3, 'date': '2024-01-09 13:29:22'}

headers = {'Content-Type': 'application/json'}

# Convert the data dictionary to JSON
json_data = json.dumps(data)

# Use the json parameter in the requests.patch method
response = requests.patch('http://server.alfredsson.xyz/upload', json=data, headers=headers)

# Print the response status code
print(response)