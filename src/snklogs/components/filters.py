# snklogs/src/snklogs/components/filters.py

from logging import Filter, LogRecord
from pathlib import Path

from ..paths.root import find_project_root


class CustomLevelFilter(Filter):
    def __init__(self):
        super().__init__()
        keys = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        self.max_len = max(len(k) for k in keys)
        self.width = self.max_len + 4
        self.level_map = {k: f"[ {k} ]".ljust(self.width) for k in keys}

    def filter(self, record: LogRecord) -> bool:
        if record.levelname not in self.level_map:
            self.level_map[record.levelname] = f"[ {record.levelname} ]".ljust(
                self.width
            )

        record.custom_level = self.level_map[record.levelname]
        return True


class CustomPathNameFilter(Filter):
    def __init__(self) -> None:
        super().__init__()
        self.project_root = find_project_root()

    def filter(self, record: LogRecord) -> bool:
        record.custom_pathname = str(
            Path(record.pathname).relative_to(self.project_root)
        )
        return True
