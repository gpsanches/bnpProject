# -*- coding: utf-8 -*-

from .config import Config


class Local(Config):
    LOGGING_LEVEL = 'DEBUG'
    MESSAGE_TYPE = 'Bnp-local'
    LOGGING_CONSOLE = ['console', ]
    ENV = 'local'
    DEBUG = True
    BNP_API_ENV = '\t%\x89I\x10\xa5\x88\x95\xcf\xb5\xe8Bu\x83\xcd\xb0'
