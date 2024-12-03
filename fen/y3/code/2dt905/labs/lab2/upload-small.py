import requests

url = "http://localhost:8888/upload"
file = {'file': open('../lab1/img/test.png', 'rb')}
response = requests.post(url, files=file)
print(response.status_code, response.text)
