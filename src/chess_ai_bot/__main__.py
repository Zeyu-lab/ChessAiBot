import json

from chess_ai_bot.db import run_database_health_check


def main() -> None:
    result = run_database_health_check()

    print("ChessAiBot container environment started successfully.")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()