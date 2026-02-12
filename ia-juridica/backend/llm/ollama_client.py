import httpx
import json
from typing import List, Dict, Optional, Any
from backend.config import settings

class OllamaClient:
    def __init__(self, base_url: str = settings.OLLAMA_BASE_URL, model: str = settings.MODEL_NAME):
        self.base_url = base_url
        self.model = model

    async def generate(self, prompt: str, system: Optional[str] = None, context: Optional[List[int]] = None) -> Dict[str, Any]:
        """
        Generate text using Ollama /api/generate endpoint.
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if system:
            payload["system"] = system
        if context:
            payload["context"] = context

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=60.0)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as exc:
                print(f"An error occurred while requesting {exc.request.url!r}.")
                raise
            except httpx.HTTPStatusError as exc:
                print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
                raise

    async def chat(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Chat using Ollama /api/chat endpoint.
        messages should be a list of dicts with "role" and "content".
        """
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=60.0)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as exc:
                print(f"An error occurred while requesting {exc.request.url!r}.")
                raise
            except httpx.HTTPStatusError as exc:
                print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
                raise
