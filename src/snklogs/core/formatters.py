# snklogs/src/snklogs/core/formatters.py


from logging import Formatter

from ..settings.consts import FILE_FMT, STREAM_FMT


def build_stream_formatter(stream_format: str = STREAM_FMT) -> Formatter:
    return Formatter(stream_format)


def build_file_formatter(file_format: str = FILE_FMT) -> Formatter:
    return Formatter(file_format)
