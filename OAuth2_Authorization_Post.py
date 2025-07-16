import requests

from Get_Method import response

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ab3ea9745f2e8c860aede8c6b6afc64f42c03921ffe6cef1c4983d528067061d',}
payload = {
    "name": "Raj",
    "email": "dummyemail@email.com",
    "gender": "Male",
    "status": "Active"
}

response = requests.post('https://gorest.co.in/public/v2/users', headers=headers, json=payload)

print(response.json())
assert response.status_code == 201