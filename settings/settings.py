# settings/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    DEBUG: bool = True

    # DATABASE
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    JWT_SECRET_KEY: str
    JWT_ALGO: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    
    DATABASE_URL: str  # postgresql+asyncpg://user:pass@localhost/db

    @property
    def database_url_sync(self) -> str:
        
        return self.DATABASE_URL.replace("+asyncpg", "")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()

