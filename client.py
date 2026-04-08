import requests
import uuid

res = requests.post(
    "http://127.0.0.1:8000/task",
    json={
        "id": str(uuid.uuid4()),
        "action": "get_weather",
        "input": {"city": "Taipei"}
    }
)

print(res.json())
