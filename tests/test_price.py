# -*- coding: utf-8 -*-

import json

from resources import rest_api
from app import create_app
from unittest import TestCase


class PriceTests(TestCase):

    def setUp(self):
        rest_api.resources = []
        app = create_app(test=True)
        self.client = app.test_client()

    def test_get_avg_without_params(self):
        r = self.client.get('/average')
        self.assertEqual(200, r.status_code)
        data = json.loads(r.data)
        self.assertIsNotNone(data)
        self.assertEqual(data['average'], 112.73986526015811)
        self.assertEqual(data['period'], 'all_data')

    def test_get_avg_all_params(self):
        r = self.client.get('/average?from=2015-03-25&to=2015-06-30')
        self.assertEqual(200, r.status_code)
        data = json.loads(r.data)
        self.assertIsNotNone(data)
        self.assertEqual(data['average'], 127.6266200132353)
        self.assertEqual(data['period']['from'], '2015-03-25')
        self.assertEqual(data['period']['to'], '2015-06-30')

    def test_get_avg_without_from(self):
        r = self.client.get('/average?to=2015-06-30')
        self.assertEqual(200, r.status_code)
        data = json.loads(r.data)
        self.assertIsNotNone(data)
        self.assertEqual(data['average'], 112.73986526015811)
        self.assertEqual(data['period'], 'all_data')

    def test_get_avg_without_to(self):
        r = self.client.get('/average?from=2015-03-25')
        self.assertEqual(200, r.status_code)
        data = json.loads(r.data)
        self.assertIsNotNone(data)
        self.assertEqual(data['average'], 112.73986526015811)
        self.assertEqual(data['period'], 'all_data')

    def test_get_avg_with_invalid_to(self):
        r = self.client.get('/average?from=2015-03-25&to=20150630')
        self.assertEqual(500, r.status_code)

    def test_get_avg_with_invalid_from(self):
        r = self.client.get('/average?from=20150325&to=2015-06-30')
        self.assertEqual(500, r.status_code)

    def test_get_avg_with_invalid_params(self):
        r = self.client.get('/average?from=20150325&to=201506-30')
        self.assertEqual(500, r.status_code)
