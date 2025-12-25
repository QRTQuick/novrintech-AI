from fastapi.responses import JSONResponse

def handle_error(message: str, status_code: int = 400):
    return JSONResponse(
        status_code=status_code,
        content={"success": False, "error": message}
    )