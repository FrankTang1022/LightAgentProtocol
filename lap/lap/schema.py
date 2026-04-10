from pydantic import BaseModel
from typing import Optional, Dict, Any

class Task(BaseModel):
    id: str
    action: str
    input: Optional[Dict[str, Any]] = None
    callback_url: Optional[str] = None
    sync: Optional[bool] = True
