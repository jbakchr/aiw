import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate(prompt: str, model: str = "llama3") -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
        timeout=60,
    )

    response.raise_for_status()
    data = response.json()

    return data["response"]