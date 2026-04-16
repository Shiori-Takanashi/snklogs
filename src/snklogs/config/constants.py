# snklogs/src/snklogs/config/constants.py

STREAM_LEVEL = "INFO"
FILE_LEVEL = "DEBUG"

DIR_NAME = "logs"
FILE_NAME_OF_BASE = "app.log"

SH_NAME = "stream-h"
FH_NAME = "file-h"

STREAM_FMT = "%(asctime)s [%(levelname)s] %(message)s"
FILE_FMT = r"%(asctime)s.%(msecs)03d %(custom_level)s: %(name)-20s :%(lineno)4d | %(message)s"
STREAM_DATE_FMT = r"%Y/%m/%d-%H:%M:%S"
FILE_DATE_FMT = r"%Y/%m/%d - %H:%M:%S"

# JSON_FMT = r"%(asctime)s.%(msecs)03d %(custom_level)s: logger_name=`%(name)s` path=`%(custom_pathname)s` `%(funcName)s` - %(message)s"
