from fastapi import APIRouter, Request

from app.schemas.interactions import InteractionResponse

router = APIRouter(prefix="/study-sets")

@router.post("/create")
def placeholder():
    return