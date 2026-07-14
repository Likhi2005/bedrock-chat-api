from fastapi import APIRouter, HTTPException

from simpleText.backend.app.schemas import (ChatRequest, ChatResponse)
from simpleText.backend.app.services.bedrock import ( bedrock_service )


router = APIRouter(
    prefix="/chat",
)

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = bedrock_service.generate_response(request.message)
        
        return ChatResponse(response=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
