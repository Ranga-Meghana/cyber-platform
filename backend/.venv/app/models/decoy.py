from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.utils.db import Base

class DecoyEvent(Base):
    _tablename_ = "decoy_events"

    id = Column(Integer, primary_key=True, index=True)
    attacker_action = Column(Text)
    fake_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)