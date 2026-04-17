# snklogs/src/snklogs/components/handlers.py

from logging import FileHandler, Handler, StreamHandler
from pathlib import Path

from ..config.constants import FHT_NAME, SH_NAME


def pick_provide_stream_handlers(
    hs: list[Handler], sh_name: str = SH_NAME
) -> list[StreamHandler]:
    results = []
    for h in hs:
        if (getattr(h, "name", None) == sh_name) and (type(h) is StreamHandler):
            results.append(h)
    return results


def pick_provide_file_handler_with_tss(
    hs: list[Handler], fht_name: str = FHT_NAME
) -> list[FileHandler]:
    results = []
    for h in hs:
        if (getattr(h, "name", None) == fht_name) and (type(h) is FileHandler):
            results.append(h)
    return results


def build_stream_handler(sh_name: str = SH_NAME) -> StreamHandler:
    sh = StreamHandler()
    sh.set_name(sh_name)
    return sh


def build_file_handler_with_ts(
    filepath: Path, fht_name: str = FHT_NAME
) -> FileHandler:
    fh = FileHandler(filepath, encoding="utf-8")
    fh.set_name(fht_name)
    return fh
