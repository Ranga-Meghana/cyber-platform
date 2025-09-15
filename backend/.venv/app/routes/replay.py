from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.services import replay_service
from app.schemas import replay_schema

router = APIRouter(prefix="/replay", tags=["Replay"])

@router.post("/", response_model=replay_schema.ReplaySessionResponse)
def create_replay(replay: replay_schema.ReplaySessionCreate, db: Session = Depends(get_db)):
    return replay_service.create_replay_session(db, replay)

@router.get("/", response_model=list[replay_schema.ReplaySessionResponse])
def get_replays(db: Session = Depends(get_db)):
    return replay_service.get_all_replay_sessions(db)