import logging

DEFAULT_MAP = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

STREAM_LEVEL = "INFO"
FILE_LEVEL = "DEBUG"


def build_stream_level(level_name: str = STREAM_LEVEL) -> int:
    return _resolve_level_name(level_name)


def build_file_level(level_name: str = FILE_LEVEL) -> int:
    return _resolve_level_name(level_name)


def _resolve_level_name(level_name: str) -> int:
    level_name = level_name.upper()
    try:
        return DEFAULT_MAP[level_name]
    except KeyError:
        raise ValueError(f"不正: {level_name}")
