from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TokenLogCreate(BaseModel):
    token_type: str
    triggered_by_ip: str
    context: str
    user_context: Optional[str] = None 

class TokenLogResponse(TokenLogCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True