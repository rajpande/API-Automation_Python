import requests

from Get_Method import response

headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
    }
request_payload = {
  "id": 1,
  "title": "Raj",
  "dueDate": "2025-05-29T10:26:19.2Z",
  "completed": True
}
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=headers, json=request_payload)
print(response.status_code)
print(response.text)

assert response.status_code == 200
assert response.json().get('id') == 1