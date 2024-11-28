import requests

url = "http://localhost:8888/upload"
files = {'file': open('../lab1/img/T4-1-win.png', 'rb')}
response = requests.post(url, files=files)
print(response.status_code, response.text)

