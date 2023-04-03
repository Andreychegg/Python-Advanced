import logging.config
from dict_config import dict_config

logging.config.dictConfig(dict_config)


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
