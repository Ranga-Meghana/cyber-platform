from pydantic import BaseModel
from datetime import datetime

class AttributionLogCreate(BaseModel):
    tools_used: str
    skill_level: str
    suspected_actor: str

class AttributionLogResponse(AttributionLogCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True