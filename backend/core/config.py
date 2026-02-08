from pydantic_settings import BaseSettings
from typing import List, Optional
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "Todo App Backend - Phase II"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"

    # Database settings
    DATABASE_URL: str = "sqlite:///./todo_app.db"  # Default to SQLite for local development

    # Auth settings
    BETTER_AUTH_SECRET: str
    BETTER_AUTH_URL: str = "http://localhost:3000"  # Updated to use underscore
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Updated from .env

    # CORS settings
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",  # Next.js default
        "http://localhost:3001",  # Alternative Next.js port
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
    ]

    # Google API settings
    GOOGLE_API_KEY: str = "your_google_api_key_here"  # Updated to remove alias

    model_config = {"env_file": ".env", "env_nested_delimiter": "__", "extra": "ignore"}

settings = Settings()
