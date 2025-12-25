from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "OK", 
        "message": "NovrinTech AI backend is running",
        "timestamp": time.time()
    }

@router.get("/keepalive")
def keep_alive():
    return {
        "status": "alive",
        "message": "Keep-alive ping successful",
        "timestamp": time.time()
    }