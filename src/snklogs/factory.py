import logging

from .core.formatters import build_stream_formatter, build_file_formatter
from .core.handlers import build_stream_handler, build_file_handler
from .core.levels import build_stream_level, build_file_level

from .settings.logpaths import build_filepath


def configure_logging(logger_name: str) -> None:
    logger = logging.getLogger(logger_name)

    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    sh = build_stream_handler(logger)
    sh.setFormatter(build_stream_formatter())
    sh.setLevel(build_stream_level())
    logger.addHandler(sh)

    fh = build_file_handler(logger, build_filepath())
    fh.setFormatter(build_file_formatter())
    fh.setLevel(build_file_level())
    logger.addHandler(fh)
