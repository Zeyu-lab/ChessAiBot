import json
import sys

from chess_ai_bot.db import run_database_health_check


def main() -> int:
    try:
        result = run_database_health_check()
        print(json.dumps(result, indent=2))
        return 0
    except Exception as exc:
        print(f"Database health check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())