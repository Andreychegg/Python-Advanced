import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def add(x, y):
    result = x + y
    logger.info(f"{x} + {y} = {result}")
    return result


def subtract(x, y):
    result = x - y
    logger.info(f"{x} - {y} = {result}")
    return result


def multiply(x, y):
    result = x * y
    logger.info(f"{x} * {y} = {result}")
    return result


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error("На ноль делить нельзя")
        return None
    logger.info(f"{x} / {y} = {result}")
    return result
