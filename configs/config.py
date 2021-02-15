# -*- coding: utf-8 -*-

import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class Config(object):
    LOGGING_CONSOLE = ['console']
    LOGSTASH_HOST = ''
    LOGSTASH_PORT = 5000
    LOGGING_LEVEL = 'INFO'
    DEBUG = False
    BASEDIR = basedir
    TASK_1 = 'https://raw.githubusercontent.com/ag-grid/ag-grid/master/grid-packages/ag-grid-docs/src/blogs.json'
    TASK_2 = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
