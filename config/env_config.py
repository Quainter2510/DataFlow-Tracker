from pydantic_settings import BaseSettings, SettingsConfigDict

class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="settings/.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

class DataBaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="db_")

    host: str
    username: str
    password: str
    
class APIConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="api_")
    
    url: str
    client: str 
    client_key: str 
    interval: int
    
class DBConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="db_")
    
    user: str 
    password: str 
    host: str 
    port: int 
    database: str 
    

