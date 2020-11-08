import requests

print(requests.post(
    "http://127.0.0.1:5000/api/signin",
    data={"name": "Flask", "email": "flask@example.org", "password": "12345"},
).text)
