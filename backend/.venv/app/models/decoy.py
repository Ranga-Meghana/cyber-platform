from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from datetime import datetime
from app.utils.db import Base

class DecoyEvent(Base):
    __tablename__ = "decoy_events"

    id = Column(Integer, primary_key=True, index=True)
    attacker_action = Column(Text)
    fake_response = Column(Text)
    parent_decoy_id = Column(Integer, ForeignKey("decoy_events.id"), nullable=True) # New field for deception maze
    timestamp = Column(DateTime, default=datetime.utcnow)