from backend.chains.base_chain import BaseChain

class TrabalhistaChain(BaseChain):
    def __init__(self):
        super().__init__()
        self.module_prompt = self._load_prompt("trabalhista_prompt.txt")

    async def run(self, input_text: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt + "\n\n" + self.module_prompt},
            {"role": "user", "content": input_text}
        ]

        response = await self.llm_client.chat(messages)
        return response.get("message", {}).get("content", "")
