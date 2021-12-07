import requests
import urllib.parse

url = 'http://localhost:8000/api/departments/'

myJson = {
    'data': [{
        "dep_id": "T02",
        "dep_name": "Test Department 2",
        "master_name": "TestD2-Master",
        "slogan": "Here is Slogan of Test Department 2!"
    }]
}

response = requests.post(url=url, json=myJson)

print('Request Url:', urllib.parse.unquote(response.url))
print('Request Body:', response.request.body)
print('Status Code:', response.status_code)
print('Response Body:', response.text)
