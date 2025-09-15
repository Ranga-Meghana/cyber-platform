from fastapi import FastAPI
from app.routes import users, tokens, deception, replay, attribution

app = FastAPI(title="Cyber Threat Platform")

app.include_router(users.router)
app.include_router(tokens.router)
app.include_router(deception.router)
app.include_router(replay.router)
app.include_router(attribution.router)

@app.get("/")
def root():
    return {"msg": "Cyber Threat Platform API is running 🚀"}