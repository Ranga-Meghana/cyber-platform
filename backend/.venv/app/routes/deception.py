from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.services import deception_service
from app.schemas import decoy_schema

router = APIRouter(prefix="/decoys", tags=["Decoys"])

@router.post("/", response_model=decoy_schema.DecoyEventResponse)
def create_decoy(decoy: decoy_schema.DecoyEventCreate, db: Session = Depends(get_db)):
    return deception_service.create_decoy_event(db, decoy)

@router.get("/", response_model=list[decoy_schema.DecoyEventResponse])
def get_decoys(db: Session = Depends(get_db)):
    return deception_service.get_all_decoys(db)