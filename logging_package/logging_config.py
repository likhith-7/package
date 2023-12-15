import logging
from logging_package.handlers import LevelFilter, DateRotatingFileHandler
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
        'critical_file': {
            'level': 'CRITICAL',
            'class': 'logging_package.handlers.DateRotatingFileHandler',
            'filename': 'critical.log',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'verbose',
            'filters': ['critical_filter']
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'CRITICAL',  # Send emails for critical logs
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'custom_email_formatter',
        },
    },
    'formatters': {
        'verbose': {
            'format' : '{asctime}:{levelname} - {name} {module}.py (line {lineno:d}). {message}',
            'style' : "{",
        },
        'custom_email_formatter': {
            'format': '{asctime}:{levelname} - {name} {module}.py (line {lineno:d}). {subject}\n\n{message}',
            'style': '{',
        },
    },
    'filters': {
        'debug_filter': {'()': LevelFilter, 'level': logging.DEBUG},
        'error_filter': {'()': LevelFilter, 'level': logging.ERROR},
        'warning_filter': {'()': LevelFilter, 'level': logging.WARNING},
        'info_filter': {'()': LevelFilter, 'level': logging.INFO},
        'critical_filter': {'()': LevelFilter, 'level': logging.CRITICAL},
    },
    'loggers': {
        'django': {
            'handlers': ['debug_file', 'error_file', 'warning_file', 'info_file','critical_file', 'console','mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
