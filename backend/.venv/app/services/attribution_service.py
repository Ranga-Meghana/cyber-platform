from sqlalchemy.orm import Session
from app import models, schemas

def log_attribution(db: Session, attr: schemas.attribution_schema.AttributionLogCreate):
    db_attr = models.attribution.AttributionLog(
        tools_used=attr.tools_used,
        skill_level=attr.skill_level,
        suspected_actor=attr.suspected_actor
    )
    db.add(db_attr)
    db.commit()
    db.refresh(db_attr)
    return db_attr

def get_all_attributions(db: Session):
    return db.query(models.attribution.AttributionLog).all()