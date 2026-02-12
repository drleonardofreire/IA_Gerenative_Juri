import os

class Settings:
    PROJECT_NAME: str = "IA Jurídica Modular"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # LLM Settings
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "llama3")  # Default model

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
