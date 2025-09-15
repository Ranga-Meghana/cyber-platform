from pydantic import BaseModel
from datetime import datetime

class ReplaySessionCreate(BaseModel):
    attacker_steps: str  

class ReplaySessionResponse(ReplaySessionCreate):
    id: int
    replay_status: str
    timestamp: datetime

    class Config:
        orm_mode = True