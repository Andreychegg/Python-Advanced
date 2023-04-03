import logging
import string


class FilterASCII(logging.Filter):
    def filter(self, record: logging.LogRecord) -> int:
        return not any(symbol not in string.printable for symbol in record.msg)
