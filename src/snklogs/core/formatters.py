from logging import Formatter

STREAM_FMT = "%(asctime)s [%(levelname)-8s] %(name)-30s %(message)s"
FILE_FMT = "%(asctime)s [%(levelname)-8s] %(name)-30s :%(lineno)4d %(message)s"


def build_stream_formatter(stream_format: str = STREAM_FMT) -> Formatter:
    return Formatter(stream_format)


def build_file_formatter(
    file_format: str = FILE_FMT,
) -> Formatter:
    return Formatter(file_format)
