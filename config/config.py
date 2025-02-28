from pydantic_settings import BaseSettings
from pydantic import Field

from .env_config import APIConfig, DBConfig, EmailConfig

class Config(BaseSettings):
    api: APIConfig = Field(default_factory=APIConfig)
    db: DBConfig = Field(default_factory=DBConfig)
    email: EmailConfig = Field(default_factory=EmailConfig)

    @classmethod
    def load(cls):
        return cls()