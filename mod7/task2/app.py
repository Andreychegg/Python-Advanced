import logging.config
import sys
import utils
from method_config import configure_logging


def get_number():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            return num1, num2
        except ValueError:
            logging.warning("Неверный ввод")


def get_operation():
    while True:
        operation = input("+ - сложение \n- - вычитание \n* - умножение \n/ - деление \n0 - выход \nВыберите действие: ")
        if operation in ["+", "-", "*", "/", "0"]:
            return operation
        logging.warning("Неверная операция: %s", operation)


def main():
    logging.info("Калькулятор запущен")
    while True:
        action = get_operation()

        if action == "0":
            logger.info("Калькулятор остановлен")
            sys.exit()

        nums = get_number()
        x = nums[0]
        y = nums[1]

        if action == "+":
            result = utils.add(x, y)
        elif action == "-":
            result = utils.subtract(x, y)
        elif action == "*":
            result = utils.multiply(x, y)
        elif action == "/":
            result = utils.divide(x, y)

        logging.info(f"Результат: {result}")


if __name__ == '__main__':
    configure_logging()
    logger = logging.getLogger(__name__)
    main()
