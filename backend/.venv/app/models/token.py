from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.utils.db import Base

class TokenLog(Base):
    _tablename_ = "token_logs"

    id = Column(Integer, primary_key=True, index=True)
    token_type = Column(String(50))
    triggered_by_ip = Column(String(50))
    context = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)