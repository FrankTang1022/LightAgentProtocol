from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict, Any

app = FastAPI()

class Task(BaseModel):
    id: str
    action: str
    input: Optional[Dict[str, Any]] = None

def get_weather(input_data):
    input_data = input_data or {}
    city = input_data.get("city", "unknown")
    return {
        "city": city,
        "temperature": 28
    }

@app.post("/task")
async def handle_task(task: Task):
    if task.action == "get_weather":
        result = get_weather(task.input)
        return {
            "id": task.id,
            "status": "success",
            "output": result
        }

    return {
        "id": task.id,
        "status": "error",
        "error": {
            "message": "unknown action"
        }
    }

@app.get("/actions")
def actions():
    return {
        "actions": ["get_weather"]
    }
