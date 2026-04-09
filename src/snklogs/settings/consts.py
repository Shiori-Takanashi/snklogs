# snklogs/src/snklogs/settings/consts.py

STREAM_LEVEL = "INFO"
FILE_LEVEL = "DEBUG"

DIR_NAME = "logs"
FILE_NAME_OF_BASE = "app.log"

SH_NAME = "stream-h"
FH_NAME = "file-h"

STREAM_FMT = "%(asctime)s [%(levelname)-8s] %(name)-30s %(message)s"
FILE_FMT = "%(asctime)s [%(levelname)-8s] %(name)-30s :%(lineno)4d %(message)s"
