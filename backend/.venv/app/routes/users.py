from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.services import user_service
from app.schemas import user_schema

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=user_schema.UserResponse)
def register_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=list[user_schema.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/leaderboard", response_model=list[user_schema.UserResponse])
def get_leaderboard(db: Session = Depends(get_db)):
    return user_service.get_leaderboard(db)