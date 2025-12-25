# NovrinTech AI Backend

FastAPI backend for AI assistant using Groq API with CORS support and keep-alive functionality.

## Features

✅ Modular API design  
✅ CORS middleware for cross-origin requests  
✅ Keep-alive ping every 2 seconds  
✅ Environment variables for API keys  
✅ Comprehensive error handling  
✅ Groq API integration  
✅ Health check endpoints  

## Quick Start

1. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp backend/.env.example backend/.env
   # Edit backend/.env and add your actual Groq API key
   ```

3. **Run the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- **GET** `/` - Welcome message
- **GET** `/api/health` - Health check
- **GET** `/api/keepalive` - Keep-alive ping
- **POST** `/api/chat` - Chat with AI

### Chat Example

```bash
curl -X POST "http://127.0.0.1:8000/api/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello AI, write me a Python function."}'
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app with CORS & keep-alive
│   ├── config.py          # Environment variables
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py        # Chat endpoints
│   │   └── health.py      # Health & keep-alive endpoints
│   └── services/
│       ├── __init__.py
│       ├── llm_service.py # Groq API integration
│       └── utils.py       # Helper functions
├── requirements.txt
├── .env.example          # Template for environment variables
└── .env                  # Your actual API keys (DO NOT COMMIT)
```

## Security Notes

- The `.env` file is ignored by git to prevent API key leaks
- Copy `.env.example` to `.env` and add your actual API key
- Never commit real API keys to version control

The backend automatically pings itself every 2 seconds to prevent sleeping on hosting platforms.