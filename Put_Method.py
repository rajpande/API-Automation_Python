import requests
headers = {
    'Accept': 'text/plain'
    }
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/12', headers=headers)
print("Before updating the resource")
print(response.json())

headers_Put = {
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
}
request_payload = {
    "id": 1,
  "title": "Raj",
  "dueDate": "2025-05-29T10:26:19.2Z",
  "completed": True
}
print("After updating the resource")
response_Put = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Activities/12', headers=headers_Put, json=request_payload)
print(response_Put.json())