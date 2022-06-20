from pydantic import BaseSettings


class Config_settings(BaseSettings):
    # Postgresql params
    postgres_db: str
    postgres_name: str
    postgres_host: str
    postgres_password: str
    postgres_port: int


    class Config:
        env_file = "app/.env"