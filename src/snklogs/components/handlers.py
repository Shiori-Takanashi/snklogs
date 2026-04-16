# snklogs/src/snklogs/components/handlers.py

from logging import FileHandler, Handler, StreamHandler
from pathlib import Path

from ..config.constants import FH_NAME, SH_NAME


def pick_provide_stream_handlers(
    hs: list[Handler], sh_name: str = SH_NAME
) -> list[StreamHandler]:
    results = []
    for h in hs:
        if (getattr(h, "name", None) == sh_name) and (type(h) is StreamHandler):
            results.append(h)
    return results


def pick_provide_file_handlers(
    hs: list[Handler], fh_name: str = FH_NAME
) -> list[FileHandler]:
    results = []
    for h in hs:
        if (getattr(h, "name", None) == fh_name) and (type(h) is FileHandler):
            results.append(h)
    return results


def build_stream_handler(sh_name: str = SH_NAME) -> StreamHandler:
    sh = StreamHandler()
    sh.set_name(sh_name)
    return sh


def build_file_handler(filepath: Path, fh_name: str = FH_NAME) -> FileHandler:
    fh = FileHandler(filepath, encoding="utf-8")
    fh.set_name(fh_name)
    return fh
