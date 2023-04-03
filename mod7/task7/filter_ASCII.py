import logging
import string


class FilterASCII(logging.Filter):
    def filter(self, record: logging.LogRecord) -> int:
        return not any(symb not in string.printable for symb in record.msg)
