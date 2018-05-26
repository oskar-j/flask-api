#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from api.utils.test_base import BaseTestCase
from api.models.model_country import Country
from api.models.model_panel_provider import PanelProvider
from datetime import datetime


TIME_DOT_COM = 'time dot com'
OPEN_LIBRARY = 'open library'
TIME_DOT_COM_ALT = 'time dot com [alt]'


def create_panel_providers():
    # 3 Panel Providers
    panel1 = PanelProvider(code=TIME_DOT_COM).create()
    panel2 = PanelProvider(code=OPEN_LIBRARY).create()
    panel3 = PanelProvider(code=TIME_DOT_COM_ALT).create()


def create_countries():
    # 3 Countries, each with different panel provider
    country1 = Country(country_code='UK',
                       panel_provider_id=PanelProvider.query.filter_by(code=TIME_DOT_COM).first().id).create()
    country2 = Country(country_code='US',
                       panel_provider_id=PanelProvider.query.filter_by(code=OPEN_LIBRARY).first().id).create()
    country3 = Country(country_code='PL',
                       panel_provider_id=PanelProvider.query.filter_by(code=TIME_DOT_COM_ALT).first().id).create()


class TestCountries(BaseTestCase):

    def setUp(self):
        super(TestCountries, self).setUp()  # hence BaseTestCase
        create_panel_providers()
        create_countries()

    def test_get_countries(self):
        response = self.app.get(
            '/countries',
            content_type='application/json'
        )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('countries' in data)

    def test_get_country_detail(self):
        response = self.app.get(
            '/country/UK',
            content_type='application/json'
            )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('country' in data)

    def test_create_country(self):
        country = {
            'country_code': 'ZA',
            'panel_provider_id': '1'
        }

        response = self.app.post(
            '/country',
            data=json.dumps(country),
            content_type='application/json'
            )
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('country' in data)
