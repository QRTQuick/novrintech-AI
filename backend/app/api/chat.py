from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_service import LLMService
from app.services.utils import handle_error

router = APIRouter()
llm_service = LLMService()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat_endpoint(req: ChatRequest):
    if not req.message or req.message.strip() == "":
        return handle_error("Message cannot be empty", 422)
    
    response = llm_service.generate_response(req.message)
    
    if response.startswith("Error:"):
        return handle_error(response, 500)
    
    return {"success": True, "reply": response}