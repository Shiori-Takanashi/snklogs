# snklogs/src/snklogs/factory.py

import logging

from .core.formatters import build_file_formatter, build_stream_formatter
from .core.handlers import build_file_handler, build_stream_handler
from .core.levels import build_file_level, build_stream_level
from .core.logpaths import build_filepath
from .settings.root import find_project_root


def configure_logging(logger_name: str) -> None:
    logger = logging.getLogger(logger_name)

    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    sh = build_stream_handler(logger)
    sh.setFormatter(build_stream_formatter())
    sh.setLevel(build_stream_level())
    logger.addHandler(sh)

    fh = build_file_handler(logger, build_filepath(find_project_root()))
    fh.setFormatter(build_file_formatter())
    fh.setLevel(build_file_level())
    logger.addHandler(fh)


def main() -> None:
    logger_name = "snklogger"
    configure_logging(logger_name)
    logger = logging.getLogger(logger_name)
    logger.info("Wellcome to snklogs.")


if __name__ == "__main__":
    main()
