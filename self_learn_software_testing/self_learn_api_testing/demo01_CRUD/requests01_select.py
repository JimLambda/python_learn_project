import requests
import urllib.parse

url = 'http://localhost:8000/api/departments/'

myParams = {
    '$dep_id_list': 'T01,T04'
}

response = requests.get(url=url, params=myParams)

print('Request Url:', urllib.parse.unquote(response.url))
print('Status Code:', response.status_code)
print('Response Body:', response.text)
