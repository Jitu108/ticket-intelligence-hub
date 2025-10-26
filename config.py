# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLSERVER_CONN_STR: str 
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    GOOGLE_API_KEY: str
    DEEPSEEK_API_KEY: str
    LLM_PROVIDER: str = "openai"
    LLM_MODEL: str = "gpt-4o-mini"
    OPENAI_API_KEY: str = ""
    EMBED_MODEL: str = "text-embedding-3-small"  # 👈 add this line

    class Config:
        env_file = ".env"


settings = Settings()