import requests
import urllib.parse

url = 'http://localhost:8000/api/departments/T02/'

myJson = {
    'data': [{
        "dep_id": "T03",
        "dep_name": "Test Department 3",
        "master_name": "TestD3-Master",
        "slogan": "Here is Slogan of Test Department 3!"
    }]
}

response = requests.put(url=url, json=myJson)

print('Request Url:', urllib.parse.unquote(response.url))
print('Request Body:', response.request.body)
print('Status Code:', response.status_code)
print('Response Body:', response.text)
