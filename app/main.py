"""
API Gateway for Revix backend

python -m uvicorn app.main:app --reload
ngrok http 8000
"""
from fastapi import FastAPI, BackgroundTasks
from app.endpoints import auth

app = FastAPI(title="Revix Backend")

@app.get("/")
async def read_root():
    return {
        "status": "200",
        "message": "healthy!"
    }

""" Initialize Routers """
api_prefix = "/api/v1"
app.include_router(auth.router, prefix=api_prefix)