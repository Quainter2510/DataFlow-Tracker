from pydantic_settings import BaseSettings
from pydantic import Field

from .env_config import DataBaseConfig, APIConfig, DBConfig

class Config(BaseSettings):
    database: DataBaseConfig = Field(default_factory=DataBaseConfig)
    api: APIConfig = Field(default_factory=APIConfig)
    db: DBConfig = Field(default_factory=DBConfig)

    @classmethod
    def load(cls):
        return cls()