import requests

url = 'http://164.68.107.70:6060/api/v1/ReadProduct'

response = requests.get(url)

status_code = response.status_code

json_data = response.json()

header = response.headers

print(header)