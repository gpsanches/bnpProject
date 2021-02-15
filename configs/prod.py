# -*- coding: utf-8 -*-

from .config import Config


class Local(Config):
    LOGGING_LEVEL = 'DEBUG'
    MESSAGE_TYPE = 'Bnp-prod'
    LOGGING_CONSOLE = ['console', ]
    ENV = 'prod'
    DEBUG = False
    BNP_API_ENV = 'q\xa4\trV\xc0\xefv\x8e\xb9:\x18\xe8\xc2\xf3\xac'