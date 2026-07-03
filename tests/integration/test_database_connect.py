import pytest

from chess_ai_bot.db import run_database_health_check


@pytest.mark.integration
def test_database_health_check() -> None:
    try:
        result = run_database_health_check()
    except Exception as exc:
        pytest.skip(f"MySQL is not available: {exc}")

    assert result["status"] == "ok"
    assert result["select_1"] == 1
    assert result["database"] == "chess_ai_bot"