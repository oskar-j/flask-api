#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from api.logic.pricing import FirstPricingLogic, SecondPricingLogic, ThirdPricingLogic
from api.utils.test_base import BaseTestCase
from api.models.model_country import Country
from api.models.model_panel_provider import PanelProvider


TIME_DOT_COM = FirstPricingLogic.panel_id
OPEN_LIBRARY = SecondPricingLogic.panel_id
TIME_DOT_COM_ALT = ThirdPricingLogic.panel_id


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


def safe_json_loads(s):
    try:
        # Python 3.6 compliant
        result = json.loads(s)
    except TypeError:
        # Raw fix for situation when we have Python 3.5 or older
        result = json.loads(s.decode('utf-8'))
    return result


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
        data = safe_json_loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('countries' in data, msg="test_get_countries has empty result")

    def test_get_country_detail(self):
        response = self.app.get(
            '/country/UK',
            content_type='application/json'
            )
        data = safe_json_loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('country' in data, msg="test_get_country_detail has empty result")

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
        data = safe_json_loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('country' in data, msg="test_create_country has empty result")
