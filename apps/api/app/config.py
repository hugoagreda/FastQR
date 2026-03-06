from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastQR API"
    app_env: str = "development"
    secret_key: str = "change-me"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/fastqr"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
