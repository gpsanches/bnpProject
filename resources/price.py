# -*- coding: utf-8 -*-

import logging
import pandas as pd

from flask_restful import Resource, request
from flask import current_app
from resources.utils import validate


class Price(Resource):

    project = 'Bnp'
    log = logging.getLogger()

    def get(self):
        service_name = self.__class__.__name__
        extra = {
            "project": self.project,
            "service_name": service_name,
        }
        _from = request.args.get('from')
        _to = request.args.get('to')

        self.log.info('{} - GET -> {}'.format(
            service_name, 'Getting period avg, from: {}, to: {}'.format(_from, _to)), extra=extra)
        df = current_app.config.get('CACHE_FILE')
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        if _from and _to:
            [validate(i) for i in [_from, _to]]
            df = df[df["Date"].isin(pd.date_range(_from, _to))]
            return {"average": df['mavg'].mean(), "period": {"from": _from, "to": _to}}
        return {"average": df['mavg'].mean(), "period": "all_data"}
