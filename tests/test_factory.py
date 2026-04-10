# snklogs/tests/test_factory.py

import logging
from pathlib import Path

import pytest

from snklogs.factory import configure_logging


def test_configure_logging_outputs_correctly(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
):
    # -------------------------------------------------------------------------
    # 1. 準備 (Arrange)
    # -------------------------------------------------------------------------
    def mock_find_project_root(*args, **kwargs):
        return tmp_path

    monkeypatch.setattr(
        "snklogs.settings.logpaths.find_project_root", mock_find_project_root
    )

    logger_name = "test_logger"
    test_message = "これはテスト用のログメッセージです"

    # -------------------------------------------------------------------------
    # 2. 実行 (Act)
    # -------------------------------------------------------------------------
    configure_logging(logger_name)
    logger = logging.getLogger(logger_name)

    logger.info(test_message)

    # -------------------------------------------------------------------------
    # 3. 検証 (Assert)
    # -------------------------------------------------------------------------

    # [検証A: コンソール(ストリーム)出力の検証]
    captured = capsys.readouterr()

    assert test_message in captured.err, (
        "コンソールにメッセージが出力されていません"
    )

    # [検証B: ファイル出力の検証]
    log_dir = tmp_path / "logs"
    assert log_dir.exists(), "logsディレクトリが作成されていません"

    log_files = list(log_dir.glob("*.log"))
    assert len(log_files) == 1, "ログファイルが正しく作成されていません"

    log_file_path = log_files[0]
    log_content = log_file_path.read_text(encoding="utf-8")
    assert test_message in log_content, (
        "ログファイルにメッセージが書き込まれていません"
    )
    assert 1 == 1
