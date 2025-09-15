from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.utils.db import Base

class ReplaySession(Base):
    _tablename_ = "replay_sessions"

    id = Column(Integer, primary_key=True, index=True)
    attacker_steps = Column(Text)   # stored as JSON string
    replay_status = Column(String(20), default="pending")
    timestamp = Column(DateTime, default=datetime.utcnow)