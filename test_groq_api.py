import requests
import json
import os

# Test Groq API directly
def test_groq_api():
    # Use environment variable or prompt for API key
    api_key = os.getenv("GROQ_API_KEY") or input("Enter your Groq API key: ")
    api_url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, say hi back!"}
        ],
        "temperature": 0.7,
        "max_tokens": 100,
        "top_p": 1,
        "stream": False
    }
    
    try:
        print("🧪 Testing Groq API directly...")
        print(f"API URL: {api_url}")
        print(f"API Key: {api_key[:20]}...")
        
        response = requests.post(api_url, headers=headers, json=payload, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ SUCCESS!")
            print(f"Response: {data['choices'][0]['message']['content']}")
        else:
            print("❌ FAILED!")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

if __name__ == "__main__":
    test_groq_api()