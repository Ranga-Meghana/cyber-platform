from pydantic import BaseModel
from datetime import datetime

class DecoyEventCreate(BaseModel):
    attacker_action: str
    fake_response: str

class DecoyEventResponse(DecoyEventCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True