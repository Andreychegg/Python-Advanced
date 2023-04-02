import logging
from method_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


def add(x, y):
    result = x + y
    logging.debug(f"{x} + {y} = {result}")
    return result


def subtract(x, y):
    result = x - y
    logging.debug(f"{x} - {y} = {result}")
    return result


def multiply(x, y):
    result = x * y
    logging.debug(f"{x} * {y} = {result}")
    return result


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("На ноль делить нельзя")
        return None
    logging.debug(f"{x} / {y} = {result}")
    return result
