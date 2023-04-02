import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def add(x, y):
    result = x + y
    logging.info(f"{x} + {y} = {result}")
    return result


def subtract(x, y):
    result = x - y
    logging.info(f"{x} - {y} = {result}")
    return result


def multiply(x, y):
    result = x * y
    logging.info(f"{x} * {y} = {result}")
    return result


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logging.error("На ноль делить нельзя")
        return None
    logging.info(f"{x} / {y} = {result}")
    return result
