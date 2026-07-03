from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "ChessAiBot"
    app_env: str = "local"
    sql_echo: bool = False

    mysql_host: str = "127.0.0.1"
    mysql_port: int = 3307
    mysql_database: str = "chess_ai_bot"
    mysql_user: str = "chess_user"
    mysql_password: str = "chess_password"

    database_url: str | None = Field(default=None)

    def build_database_url(self) -> str:
        if self.database_url:
            return self.database_url

        return (
            f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}"
            "?charset=utf8mb4"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()