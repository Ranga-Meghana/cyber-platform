from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DecoyEventCreate(BaseModel):
    attacker_action: str
    fake_response: str
    parent_decoy_id: Optional[int] = None 

class DecoyEventResponse(DecoyEventCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True