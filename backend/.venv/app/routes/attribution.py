from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.db import get_db
from app.services import attribution_service
from app.schemas import attribution_schema

router = APIRouter(prefix="/attribution", tags=["Attribution"])

@router.post("/", response_model=attribution_schema.AttributionLogResponse)
def create_attribution(attr: attribution_schema.AttributionLogCreate, db: Session = Depends(get_db)):
    return attribution_service.log_attribution(db, attr)

@router.get("/", response_model=list[attribution_schema.AttributionLogResponse])
def get_attributions(db: Session = Depends(get_db)):
    return attribution_service.get_all_attributions(db)