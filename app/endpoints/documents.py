from fastapi import APIRouter, Request
from documents.service import service

router = APIRouter(prefix="/documents")

@router.post("/presigned-urls")
def generate_presigned_urls(request: Request):
    document_data = request.json()
    
    return service.generate_presigned_urls(document_data)
