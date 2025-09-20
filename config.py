from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings."""
    # CORS settings
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000", 
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        # Add the exact origin of your frontend application
    ]
    cors_headers: List[str] = ["*"]
    cors_methods: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    cors_allow_credentials: bool = True

    class Config:
        env_file = ".env"
        env_prefix = "APP_"


# Create a global instance
settings = Settings()
