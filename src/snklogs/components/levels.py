# snklogs/src/snklogs/components/levels.py

import logging

from ..config.constants import FILE_LEVEL, STREAM_LEVEL


def build_level_of_sh_level(level_name: str = STREAM_LEVEL) -> int:
    return _resolve_level_name(level_name)


def build_level_of_fh_with_ts(level_name: str = FILE_LEVEL) -> int:
    return _resolve_level_name(level_name)


def _resolve_level_name(level_name: str) -> int:
    upper_name = level_name.upper()
    level = logging.getLevelNamesMapping().get(upper_name)

    if level is None:
        raise ValueError(f"不正なログレベル名です: {level_name}")

    return level
