from sqlalchemy.orm import Session
from app import models, schemas

def create_replay_session(db: Session, replay: schemas.replay_schema.ReplaySessionCreate):
    db_replay = models.replay.ReplaySession(
        attacker_steps=replay.attacker_steps,
        replay_status="pending"
    )
    db.add(db_replay)
    db.commit()
    db.refresh(db_replay)
    return db_replay

def get_all_replay_sessions(db: Session):
    return db.query(models.replay.ReplaySession).all()