from fastapi import FastAPI
from lap.schema import Task

app = FastAPI()


@app.get("/")
def root():
    return {"message": "LAP server running"}


@app.post("/task")
def handle_task(task: Task):
    if task.action == "get_weather":
        return {
            "id": task.id,
            "status": "success",
            "output": {
                "city": task.input.get("city"),
                "temperature": 28
            }
        }

    return {
        "id": task.id,
        "status": "error",
        "error": {
            "code": "UNKNOWN_ACTION"
        }
    }
