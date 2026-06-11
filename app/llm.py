
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def generate_answer(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
                "seed": 42
            }
        }
    )
    return response.json()["response"].strip()
