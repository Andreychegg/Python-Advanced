import logging
from logging.handlers import TimedRotatingFileHandler
from logs_levels import LogsLevels


dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO'
        },
        'file': {
            '()': LogsLevels,
            'formatter': 'standard'
        },
        'utils_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filename': 'utils.log',
            'when': 'H',
            'interval': 10,
            'backupCount': 5
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'utils': {
            'handlers': ['utils_file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
