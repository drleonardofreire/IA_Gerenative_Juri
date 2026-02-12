from typing import Dict, Any, List
import os
from backend.llm.ollama_client import OllamaClient
from backend.config import settings

class BaseChain:
    def __init__(self):
        self.llm_client = OllamaClient()
        self.system_prompt = self._load_prompt("system_prompt.txt")

    def _load_prompt(self, filename: str) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return ""

    async def run(self, input_text: str) -> str:
        raise NotImplementedError("Subclasses must implement run method")
