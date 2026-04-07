import logging

from .core.formatters import build_file_formatter, build_stream_formatter
from .core.handlers import build_file_handler, build_stream_handler
from .core.levels import build_file_level, build_stream_level
from .settings.logpaths import build_filepath


# ============================================================
# Builder パターン
# 役割: Loggerを段階的に組み立てる
# ============================================================
class LoggerBuilder:
    """Builderパターン: Loggerをステップごとに組み立てる。

    メソッドチェーンにより、追加するハンドラの種類と順序を
    呼び出し側 (Director) が自由に制御できる。
    """

    def __init__(self, logger_name: str) -> None:
        self._logger = logging.getLogger(logger_name)
        self._logger.propagate = False
        self._logger.setLevel(logging.DEBUG)

    def add_stream_handler(self) -> "LoggerBuilder":
        sh = build_stream_handler(self._logger)
        sh.setFormatter(build_stream_formatter())
        sh.setLevel(build_stream_level())
        self._logger.addHandler(sh)
        return self

    def add_file_handler(self) -> "LoggerBuilder":
        fh = build_file_handler(self._logger, build_filepath())
        fh.setFormatter(build_file_formatter())
        fh.setLevel(build_file_level())
        self._logger.addHandler(fh)
        return self

    def build(self) -> logging.Logger:
        return self._logger


# ============================================================
# Director パターン
# 役割: Builderを使ってLoggerの構築手順を定義する
# ============================================================
def configure_logging(logger_name: str) -> logging.Logger:
    """Directorパターン: LoggerBuilderを使ってLoggerを構築する。

    ストリームハンドラとファイルハンドラの両方を付与する
    標準的な構築手順をカプセル化している。
    """
    return (
        LoggerBuilder(logger_name)
        .add_stream_handler()
        .add_file_handler()
        .build()
    )
