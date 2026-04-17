# snklogs/src/snklogs/loggers.py

import logging

from snklogs.components.filters import CustomLevelFilter

from .components.formatters import build_file_formatter, build_stream_formatter
from .components.handlers import (
    build_file_handler_with_ts,
    build_stream_handler,
    pick_provide_file_handler_with_tss,
    pick_provide_stream_handlers,
)
from .components.levels import (
    build_level_of_fh_with_ts,
    build_level_of_sh_level,
)
from .paths.logfiles import build_filepath
from .paths.root import find_project_root


def configure_logging(logger_name: str) -> None:
    logger = logging.getLogger(logger_name)

    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    # StreamHandler
    for h in pick_provide_stream_handlers(logger.handlers):
        logger.removeHandler(h)
        h.close()

    sh = build_stream_handler()
    sh.setFormatter(build_stream_formatter())
    sh.setLevel(build_level_of_sh_level())

    logger.addFilter(CustomLevelFilter())
    logger.addHandler(sh)

    # FileHandler
    for h in pick_provide_file_handler_with_tss(logger.handlers):
        logger.removeHandler(h)
        h.close()

    fp = build_filepath(find_project_root())
    fh = build_file_handler_with_ts(fp)
    fh.setFormatter(build_file_formatter())
    fh.setLevel(build_level_of_fh_with_ts())

    logger.addFilter(CustomLevelFilter())
    logger.addHandler(fh)


def main() -> None:
    logger_name = "snklogger"
    configure_logging(logger_name)
    logger = logging.getLogger(logger_name)
    logger.debug("This is debug message.")
    logger.info("This is info message.")
    logger.warning("This is warning message.")
    logger.error("This is error message.")
    logger.critical("This is critical message.")


if __name__ == "__main__":
    main()
