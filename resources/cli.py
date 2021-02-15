# -*- coding: utf-8 -*-

import click
import json
import requests
import logging

from flask import current_app
from resources.utils import format_date
from pprint import pprint

project = 'BNP'
log = logging.getLogger()


def create_cli_commands(app):

    @app.cli.command('task-1a')
    def task_1a():
        log.info("Executing task-1 A ...")
        task_1 = current_app.config.get('TASK_1')
        response = requests.get(task_1).text
        data = json.loads(response)
        lines = sorted(data, key=lambda x: (x['author'], format_date(x["date"], "timestamp")), reverse=False)
        pprint(lines)

    @app.cli.command('task-1b')
    @click.argument('keyword', nargs=-1)
    def task_1b(keyword=None):
        log.info("Executing task-1 B ...")
        task_1 = current_app.config.get('TASK_1')
        response = requests.get(task_1).text
        data = json.loads(response)
        lines = []

        for line in data:
            line['date'] = format_date(line['date'], "%Y-%m-%d")
            if keyword:
                if keyword in line['title']:
                    lines.append(line)
            else:
                lines.append(line)
        pprint(lines)
