from sqlalchemy.orm import Session
from app import models, schemas
import random
import json

def create_decoy_event(db: Session, decoy: schemas.decoy_schema.DecoyEventCreate):
    db_decoy = models.decoy.DecoyEvent(
        attacker_action=decoy.attacker_action,
        fake_response=decoy.fake_response,
        parent_decoy_id=decoy.parent_decoy_id
    )
    db.add(db_decoy)
    db.commit()
    db.refresh(db_decoy)
    return db_decoy

def get_all_decoys(db: Session):
    return db.query(models.decoy.DecoyEvent).all()

def generate_next_decoy(attacker_action: str, user_context: str):
    """
    This function simulates the AI-driven logic for the deception maze.
    For a hackathon, this can be simple rules. In a real product, this would be an ML model.
    """
    user_data = json.loads(user_context)
    user_email = user_data.get("email")

    if "login" in attacker_action.lower():
        fake_email_response = f"A password reset link has been sent to {user_email}. Please check your inbox to continue."
        return {"action_to_prompt": "Check Email", "response": fake_email_response}
    elif "password reset" in attacker_action.lower():
        fake_password_reset_url = f"https://fake-reset-password-page.com/token={random.randint(1000, 9999)}"
        return {"action_to_prompt": "Navigate to URL", "response": fake_password_reset_url}
    else:
        return {"action_to_prompt": "Continue", "response": "The system is responding normally."}

def check_threat_level(attacker_ip: str, action: str) -> str:
    """
    Simulates a "smarter response" by checking if the action is truly suspicious.
    """

    if "nmap" in action.lower() or "mimikatz" in action.lower():
        return "HIGH"
    if attacker_ip in ["1.1.1.1", "2.2.2.2"]:  
        return "HIGH"
    return "LOW"