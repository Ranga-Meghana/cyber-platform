# app/models/user.py

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.utils.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    points = Column(Integer, default=0) 
    created_at = Column(DateTime, default=datetime.utcnow)