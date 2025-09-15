from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: schemas.user_schema.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.user.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.user.User).all()

def get_leaderboard(db: Session, limit: int = 10):
    """Returns users sorted by points for the leaderboard."""
    return db.query(models.user.User).order_by(models.user.User.points.desc()).limit(limit).all()