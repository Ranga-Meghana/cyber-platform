from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.services import token_service
from app.schemas import token_schema

router = APIRouter(prefix="/tokens", tags=["Tokens"])

@router.post("/", response_model=token_schema.TokenLogResponse)
def log_token(token: token_schema.TokenLogCreate, db: Session = Depends(get_db)):
    return token_service.log_token_event(db, token)

@router.get("/", response_model=list[token_schema.TokenLogResponse])
def get_tokens(db: Session = Depends(get_db)):
    return token_service.get_all_tokens(db)