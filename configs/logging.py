# -*- coding: utf-8 -*-

import logging

from logging.config import dictConfig


class Formatter(logging.StreamHandler):
    def_keys = ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module', 'exc_info',
                'exc_text', 'stack_info', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'thread',
                'threadName', 'processName', 'process', 'message']

    def format(self, record):
        string = super(self).format(record)
        extra = {k: v for k, v in record.__dict__.items() if k not in self.def_keys}
        if len(extra) > 0:
            string += " - extra: " + str(extra)
        return string


def logging(app):
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format':
                    '%(asctime)s [%(levelname)s] %(message)s %(threadName)s',
            },
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format':
                    '%(asctime)s  %(bold)s%(log_color)s[%(levelname)s]%(reset)s'
                    '  %(cyan)s%(message)s%(reset)s'
            }
        },
        'handlers': {
            'logstash': {
                'class': 'logstash.TCPLogstashHandler',
                'host': app.config['LOGSTASH_HOST'],
                'port': app.config['LOGSTASH_PORT'],
                'message_type': app.config['MESSAGE_TYPE']
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored'
            }
        },
        'root': {
            'level': app.config['LOGGING_LEVEL'],
            'handlers': app.config['LOGGING_CONSOLE']
        }
    })
