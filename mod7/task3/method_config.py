import logging
import sys
from logs_levels import LogsLevels


def configure_logging():
    formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    file_handler = LogsLevels()
    file_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[stream_handler, file_handler])
