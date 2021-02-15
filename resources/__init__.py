# -*- coding: utf-8 -*-

import flask
import logging
from flask_restful import Api

from resources.price import Price


rest_api = Api()
log = logging.getLogger()


def create_routes(app, **kwargs):
    rest_api.add_resource(Price, '/average', endpoint='average')
    rest_api.init_app(app)

    @app.errorhandler(404)
    def not_found(e):
        return flask.jsonify(error=404, text=str(e)), 404

    @app.errorhandler(Exception)
    def exception(e):
        return flask.jsonify(error=500, text=str(e)), 500

    # Health check
    @app.route('/ping')
    def ping():
        log.info("Ping request!")
        return 'pong'
