from pathlib import Path

import chess_ai_bot


def test_package_can_be_imported() -> None:
    assert chess_ai_bot is not None


def test_project_has_expected_root_files() -> None:
    project_root = Path(__file__).resolve().parents[2]

    assert (project_root / "pyproject.toml").exists()
    assert (project_root / "requirements.txt").exists()
    assert (project_root / "README.md").exists()


def test_project_has_expected_source_layout() -> None:
    project_root = Path(__file__).resolve().parents[2]

    assert (project_root / "src" / "chess_ai_bot").exists()
    assert (project_root / "src" / "chess_ai_bot" / "config").exists()
    assert (project_root / "src" / "chess_ai_bot" / "utils").exists()