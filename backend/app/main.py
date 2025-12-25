from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.api.health import router as health_router
import asyncio
import httpx

app = FastAPI(
    title="NovrinTech AI Assistant Backend",
    description="Backend for AI assistant using Groq API with CORS and keep-alive",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(chat_router, prefix="/api")
app.include_router(health_router, prefix="/api")

# Keep-alive task
async def keep_alive_task():
    """Send keep-alive requests every 2 seconds"""
    while True:
        try:
            async with httpx.AsyncClient() as client:
                await client.get("http://127.0.0.1:8000/api/keepalive", timeout=5.0)
        except Exception as e:
            print(f"Keep-alive ping failed: {e}")
        
        await asyncio.sleep(2)

@app.on_event("startup")
async def startup_event():
    """Start the keep-alive task when the app starts"""
    asyncio.create_task(keep_alive_task())

@app.get("/")
def root():
    return {
        "message": "Welcome to NovrinTech AI Backend", 
        "features": ["CORS enabled", "Keep-alive every 2 seconds"]
    }