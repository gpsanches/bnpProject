# -*- coding: utf-8 -*-

import os
import configs

from flask import Flask
from configs.logging import logging
from resources import create_routes
from resources.cli import create_cli_commands
import pandas as pd


def create_app(environment='local', test=False):
    app = Flask('bnp_{}'.format(environment))
    config_env = os.getenv('BNP_API_ENV', environment)
    app.config.from_object(getattr(configs, config_env.capitalize()))
    app.debug = app.config.get('DEBUG', False)
    if test:
        settings_override = {
            'TESTING': True,
        }
        app.config.update(settings_override)
    logging(app)
    create_routes(app)
    create_cli_commands(app)

    app.config['CACHE_FILE'] = pd.read_csv(app.config.get('TASK_2'), parse_dates=['Date'])

    return app
