from pydantic import BaseModel
from datetime import datetime

class TokenLogCreate(BaseModel):
    token_type: str
    triggered_by_ip: str
    context: str

class TokenLogResponse(TokenLogCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True