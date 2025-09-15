from sqlalchemy.orm import Session
from app import models, schemas

def create_decoy_event(db: Session, decoy: schemas.decoy_schema.DecoyEventCreate):
    db_decoy = models.decoy.DecoyEvent(
        attacker_action=decoy.attacker_action,
        fake_response=decoy.fake_response
    )
    db.add(db_decoy)
    db.commit()
    db.refresh(db_decoy)
    return db_decoy

def get_all_decoys(db: Session):
    return db.query(models.decoy.DecoyEvent).all()