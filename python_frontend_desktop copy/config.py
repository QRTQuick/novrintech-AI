"""
Configuration settings for Novrintech Desktop Client with AI Integration
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Embedded API Configuration - Ready to use!
DEFAULT_API_URL = "https://novrintech-data-fall-back.onrender.com"
DEFAULT_API_KEY = "novrintech_api_key_2024_secure"

# AI Backend Configuration
AI_API_URL = "https://novrintech-ai.onrender.com"
AI_ENDPOINTS = {
    "chat": "/api/chat",
    "health": "/api/health",
    "keepalive": "/api/keepalive"
}

# Application Context for AI Understanding
APP_CONTEXT = {
    "name": "Novrintech Data Fall Back Desktop Client",
    "version": "2.0 with AI Integration",
    "description": "A comprehensive desktop application for file management, data operations, and AI assistance",
    "features": [
        "Secure file upload and download with user tracking",
        "Bulk file operations and management",
        "JSON data storage and retrieval",
        "Real-time server monitoring with keep-alive",
        "AI-powered assistance and support",
        "Chat system with activity logging",
        "Notification system with EXE compatibility",
        "Responsive UI with zoom capabilities",
        "Keyboard shortcuts and context menus",
        "Comprehensive error handling and recovery"
    ],
    "components": {
        "frontend": "Python tkinter desktop application with modern UI",
        "backend": "FastAPI server for file and data operations",
        "ai_backend": "FastAPI server with Groq LLM integration",
        "storage": "Local JSON files for history and settings",
        "notifications": "Cross-platform notification system"
    },
    "technical_details": {
        "ui_framework": "tkinter with ttk styling",
        "http_client": "requests library for API communication",
        "file_handling": "hashlib for duplicate detection",
        "threading": "background keep-alive and non-blocking operations",
        "data_format": "JSON for configuration and history",
        "security": "API key authentication",
        "deployment": "EXE compilation with PyInstaller support"
    },
    "api_endpoints": {
        "file_operations": [
            "POST /file/upload - Upload files with user tracking",
            "GET /file/list - List all uploaded files",
            "GET /file/download/{file_id} - Download specific file",
            "DELETE /file/delete/{file_id} - Delete file from server",
            "GET /file/read/{file_id} - Get file information"
        ],
        "data_operations": [
            "POST /data/save - Store JSON data with custom keys",
            "GET /data/read/{key} - Retrieve stored data",
            "PUT /data/update/{key} - Update existing data",
            "DELETE /data/delete/{key} - Delete stored data"
        ],
        "ai_operations": [
            "POST /api/chat - Chat with AI assistant",
            "GET /api/health - Check AI backend health",
            "GET /api/keepalive - Keep-alive ping"
        ]
    },
    "user_workflows": [
        "Upload files with automatic duplicate detection",
        "Manage files with bulk operations",
        "Store and retrieve configuration data",
        "Monitor system health and connectivity",
        "Get AI assistance for application usage",
        "View activity logs and statistics",
        "Export data and file lists"
    ],
    "troubleshooting": {
        "connection_issues": "Check internet connection and API URLs",
        "upload_failures": "Verify file size limits and API key",
        "missing_files": "Server restarts may clear temporary storage",
        "notification_problems": "EXE compatibility mode available",
        "performance_issues": "Use keep-alive to prevent server sleep"
    }
}

# File Upload Settings
MAX_FILE_SIZE_MB = 100  # Maximum file size in MB
ALLOWED_FILE_TYPES = [
    ".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", 
    ".jpg", ".jpeg", ".png", ".gif", ".mp4", ".avi",
    ".zip", ".rar", ".json", ".xml", ".csv",".html"
]

# UI Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
THEME = "default"  # Can be "default", "dark", etc.

# Local Storage
HISTORY_FILE = "upload_history.json"
CONFIG_FILE = "app_config.json"
CHAT_HISTORY_FILE = "chat_history.json"
AI_CHAT_HISTORY_FILE = "ai_chat_history.json"

# API Endpoints
ENDPOINTS = {
    "health": "/health",
    "file_upload": "/file/upload",
    "file_read": "/file/read",
    "data_save": "/data/save",
    "data_read": "/data/read",
    "data_update": "/data/update",
    "data_delete": "/data/delete"
}

# Duplicate Detection
ENABLE_HASH_CHECK = True
HASH_ALGORITHM = "md5"  # md5, sha1, sha256

# Logging
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "app.log"