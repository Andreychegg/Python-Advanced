import logging


class LogsLevels(logging.Handler):
    def __init__(self, mode='a'):
        super().__init__()
        self.mode = mode

    def emit(self, record):
        message = self.format(record)
        with open(f'calc_{record.levelname.lower()}.log', mode=self.mode) as file:
            file.write(f'{message}\n')
