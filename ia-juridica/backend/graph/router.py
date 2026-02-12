from typing import Dict
from backend.llm.ollama_client import OllamaClient
from backend.chains.civil_chain import CivilChain
from backend.chains.trabalhista_chain import TrabalhistaChain

class Router:
    def __init__(self):
        self.llm_client = OllamaClient()
        self.chains = {
            "civil": CivilChain(),
            "trabalhista": TrabalhistaChain()
        }

    async def route(self, input_text: str) -> str:
        """
        Determines the legal area and routes the request to the appropriate chain.
        """
        classification = await self._classify(input_text)
        print(f"Classified as: {classification}")

        chain = self.chains.get(classification.lower())
        if chain:
            return await chain.run(input_text)
        else:
            return "Desculpe, não consegui identificar a área jurídica ou o módulo ainda não está implementado."

    async def _classify(self, input_text: str) -> str:
        prompt = f"""
        Classifique o seguinte caso jurídico em UMA das seguintes categorias: Civil, Trabalhista.
        Se não tiver certeza ou for outra área, responda "Outros".
        Responda APENAS com uma palavra.

        Caso: "{input_text}"
        """
        result = await self.llm_client.generate(prompt)
        classification = result.get("response", "").strip().lower()

        if "civil" in classification:
            return "civil"
        elif "trabalhista" in classification:
            return "trabalhista"
        else:
            return "outros"
