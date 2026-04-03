from pathlib import Path
from logging import Logger, StreamHandler, FileHandler

SH_NAME = "stream-h"
FH_NAME = "file-h"


def build_stream_handler(logger: Logger, sh_name: str = SH_NAME) -> StreamHandler:
    target_handlers = []
    for h in logger.handlers:
        if (getattr(h, "name", None) == sh_name) and (type(h) is StreamHandler):
            target_handlers.append(h)

    for h in target_handlers:
        logger.removeHandler(h)
        h.close()

    sh = StreamHandler()
    sh.set_name(sh_name)
    return sh


def build_file_handler(
    logger: Logger,
    filepath: Path,
    fh_name: str = FH_NAME,
) -> FileHandler:
    target_handlers = []
    for h in logger.handlers:
        if (getattr(h, "name", None) == fh_name) and (type(h) is FileHandler):
            target_handlers.append(h)

    for h in target_handlers:
        logger.removeHandler(h)
        h.close()

    fh = FileHandler(filepath, encoding="utf-8")
    fh.set_name(fh_name)
    return fh
