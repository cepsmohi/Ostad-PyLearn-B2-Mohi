# request payload

import requests

url = 'http://164.68.107.70:6060/api/v1/CreateProduct'

payload = {
    "ProductName": "Mohiuddin",
    "ProductCode": "890",
    "Img": "abc",
    "UnitPrice": "12",
    "Qty": "2",
    "TotalPrice": "24"
}

headers = {
    'Content-Type': 'application/json'
}

requests.post(url, json=payload, headers=headers)