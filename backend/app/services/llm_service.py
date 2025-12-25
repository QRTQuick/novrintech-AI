import requests
from app.config import settings

class LLMService:
    def __init__(self):
        self.api_key = settings.GROQ_API_KEY
        self.api_url = settings.GROQ_API_URL

    def generate_response(self, message: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a helpful NovrinTech AI assistant."},
                {"role": "user", "content": message}
            ]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            if "choices" not in data or len(data["choices"]) == 0:
                raise ValueError("Invalid response from LLM API")
            
            return data["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            return f"Error: Could not reach LLM service ({e})"
        except ValueError as e:
            return f"Error: Invalid LLM response ({e})"
        except Exception as e:
            return f"Error: Unexpected error ({e})"