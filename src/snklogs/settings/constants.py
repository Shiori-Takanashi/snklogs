# snklogs/src/snklogs/settings/constants.py

STREAM_LEVEL = "INFO"
FILE_LEVEL = "DEBUG"

DIR_NAME = "logs"
FILE_NAME_OF_BASE = "app.log"

SH_NAME = "stream-h"
FH_NAME = "file-h"

STREAM_FMT = "%(asctime)s [%(levelname)s] %(message)s"
FILE_FMT = "%(asctime)s.%(msecs)03d [%(levelname)-9s] %(name)30s :%(lineno)-4d %(message)s"
STREAM_DATE_FMT = r"%Y/%m/%d-%H:%M:%S"
FILE_DATE_FMT = r"%Y/%m/%d - %H:%M:%S"
