from sqlalchemy.orm import Session
from app import models, schemas

def log_token_event(db: Session, token: schemas.token_schema.TokenLogCreate):
    db_token = models.token.TokenLog(
        token_type=token.token_type,
        triggered_by_ip=token.triggered_by_ip,
        context=token.context
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def get_all_tokens(db: Session):
    return db.query(models.token.TokenLog).all()