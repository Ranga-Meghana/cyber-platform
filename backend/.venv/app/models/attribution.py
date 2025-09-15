from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.utils.db import Base

class AttributionLog(Base):
    _tablename_ = "attribution_logs"

    id = Column(Integer, primary_key=True, index=True)
    tools_used = Column(Text)          # e.g., nmap, mimikatz
    skill_level = Column(String(50))   # beginner, intermediate, advanced
    suspected_actor = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)