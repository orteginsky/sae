#backend.sae.py
from fastapi import FastAPI
from backend.api import user

app = FastAPI()
app.include_router(user.router, prefix="/users")

@app.get("/")
async def root():
    return {"message": "hola"}
