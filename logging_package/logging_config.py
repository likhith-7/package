import logging
import os
from logging_package.handlers import LevelFilter, DateRotatingFileHandler

LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging_package.handlers.DateRotatingFileHandler',
            'filename': 'debug.log',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'verbose',
            'filters': ['debug_filter']
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging_package.handlers.DateRotatingFileHandler',
            'filename': 'error.log',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'verbose',
            'filters': ['error_filter']
        },
        'warning_file': {
            'level': 'WARNING',
            'class': 'logging_package.handlers.DateRotatingFileHandler',
            'filename': 'warning.log',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'verbose',
            'filters': ['warning_filter']
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging_package.handlers.DateRotatingFileHandler',
            'filename': 'info.log',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'verbose',
            'filters': ['info_filter']
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'celery_file': {
            'level': 'DEBUG',
            'class': 'logging_package.handlers.DateRotatingFileHandler',
            'filename': 'celery.log',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format' : '{asctime}:{levelname} - {name} {module}.py (line {lineno:d}). {message}',
            'style' : "{",
        }
    },
    'filters': {
        'debug_filter': {'()': LevelFilter, 'level': logging.DEBUG},
        'error_filter': {'()': LevelFilter, 'level': logging.ERROR},
        'warning_filter': {'()': LevelFilter, 'level': logging.WARNING},
        'info_filter': {'()': LevelFilter, 'level': logging.INFO},
    },
    'loggers': {
        'django': {
            'handlers': ['debug_file', 'error_file', 'warning_file', 'info_file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'celery': {
            'handlers': ['celery_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
logging.config.dictConfig(LOGGING)
