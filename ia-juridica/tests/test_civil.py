import unittest
from unittest.mock import AsyncMock, patch
from backend.chains.civil_chain import CivilChain

class TestCivilChain(unittest.IsolatedAsyncioTestCase):
    async def test_civil_chain_call(self):
        # Arrange
        mock_response = {
            "message": {
                "content": "Resposta simulada do modelo civil."
            }
        }

        with patch("backend.chains.base_chain.OllamaClient") as MockClient:
            mock_client_instance = MockClient.return_value
            mock_client_instance.chat = AsyncMock(return_value=mock_response)

            chain = CivilChain()

            # Act
            result = await chain.run("Caso de divórcio litigioso.")

            # Assert
            self.assertEqual(result, "Resposta simulada do modelo civil.")
            mock_client_instance.chat.assert_called_once()
            call_args = mock_client_instance.chat.call_args[0][0]

            # Verify system prompt contains civil specific instructions
            system_msg = call_args[0]["content"]
            self.assertIn("MÓDULO – DIREITO CIVIL", system_msg)
            self.assertIn("Priorizar:", system_msg)

if __name__ == "__main__":
    unittest.main()
