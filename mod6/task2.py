import re
import sys
import getpass
import hashlib
import logging


logger = logging.getLogger('password_checker')


def input_and_check_password():
    logger.debug('Начало input_and_check_password')
    password: str = getpass.getpass()

    if not password:
        logger.warning('Вы ввели пустой пароль.')
        return False

    if not is_strong_password(password):
        logger.warning('Пароль содержит слова английского языка.')
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode('latin-1'))

        if hasher.hexdigest() == '098f6bcd4621d373cade4e832627b4f6':
            return True

    except ValueError as ex:
        logger.exception('Вы ввели некорректный символ ', exc_info=False)

    return False


def is_strong_password(password):
    with open('words.txt', 'r') as file:
        words = file.read()
    words = re.findall(r'\b\S{5,}\b', words)

    for word in words:
        if word.lower() in password.lower():
            return False
    return True


if __name__ == '__main__':
    logging.basicConfig(
        filename='stderr.txt',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)

    count_number: int = 3
    logger.info(f'Вы пытаетесь аутентифицироваться в Skillbox. У вас есть {count_number} попытки.')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error('Пользователь трижды ввёл неправильный пароль!')
    exit(1)
