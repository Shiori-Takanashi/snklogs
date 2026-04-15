# snklogs/src/snklogs/core/handlers.py

from logging import FileHandler, Handler, StreamHandler
from pathlib import Path

from ..settings.constants import FH_NAME, SH_NAME


def has_sh_name(h: Handler, sh_name: str = SH_NAME) -> bool:
    if (getattr(h, "name", None) == sh_name) and (type(h) is StreamHandler):
        return True
    else:
        return False


def build_stream_handler(sh_name: str = SH_NAME) -> StreamHandler:
    sh = StreamHandler()
    sh.set_name(sh_name)
    return sh


def has_fh_name(h: Handler, fh_name: str = FH_NAME) -> bool:
    if (getattr(h, "name", None) == fh_name) and (type(h) is FileHandler):
        return True
    else:
        return False


def build_file_handler(filepath: Path, fh_name: str = FH_NAME) -> FileHandler:
    fh = FileHandler(filepath, encoding="utf-8")
    fh.set_name(fh_name)
    return fh
