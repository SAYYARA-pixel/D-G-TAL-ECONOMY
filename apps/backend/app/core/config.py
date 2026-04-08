from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    app_name: str = 'D-G-TAL Economy Platform'
    api_v1_prefix: str = '/api/v1'
    secret_key: str = 'change_me'
    access_token_expire_minutes: int = 60
    algorithm: str = 'HS256'
    database_url: str = 'sqlite+pysqlite:///./local.db'


settings = Settings()
