# snklogs/src/snklogs/components/formatters.py

from logging import Formatter

from ..config.constants import (
    FILE_DATE_FMT,
    FILE_FMT,
    STREAM_DATE_FMT,
    STREAM_FMT,
)


def build_stream_formatter(
    stream_format: str = STREAM_FMT, date_format: str = STREAM_DATE_FMT
) -> Formatter:
    return Formatter(stream_format, date_format)


def build_file_formatter(
    file_format: str = FILE_FMT, date_format: str = FILE_DATE_FMT
) -> Formatter:
    return Formatter(file_format, date_format)
