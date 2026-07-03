from __future__ import annotations

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from chess_ai_bot.config.settings import get_settings


_engine: Engine | None = None


def get_engine() -> Engine:
    global _engine

    if _engine is None:
        settings = get_settings()

        _engine = create_engine(
            settings.build_database_url(),
            echo=settings.sql_echo,
            pool_pre_ping=True,
            pool_recycle=1800,
            future=True,
        )

    return _engine


def run_database_health_check() -> dict[str, object]:
    engine = get_engine()

    with engine.connect() as connection:
        select_1 = connection.execute(text("SELECT 1")).scalar_one()
        database_name = connection.execute(text("SELECT DATABASE()")).scalar_one()
        mysql_version = connection.execute(text("SELECT VERSION()")).scalar_one()

    return {
        "status": "ok",
        "select_1": select_1,
        "database": database_name,
        "mysql_version": mysql_version,
    }