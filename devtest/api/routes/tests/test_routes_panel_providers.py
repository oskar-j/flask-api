#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from api.logic.pricing import FirstPricingLogic, SecondPricingLogic, ThirdPricingLogic
from api.utils.test_base import BaseTestCase
from api.models.model_panel_provider import PanelProvider


TIME_DOT_COM = FirstPricingLogic.panel_id
OPEN_LIBRARY = SecondPricingLogic.panel_id
TIME_DOT_COM_ALT = ThirdPricingLogic.panel_id


def create_panel_providers():
    # 3 Panel Providers
    panel1 = PanelProvider(code=TIME_DOT_COM).create()
    panel2 = PanelProvider(code=OPEN_LIBRARY).create()
    panel3 = PanelProvider(code=TIME_DOT_COM_ALT).create()


def safe_json_loads(s):
    try:
        # Python 3.6 compliant
        result = json.loads(s)
    except TypeError:
        # Raw fix for situation when we have Python 3.5 or older
        result = json.loads(s.decode('utf-8'))
    return result


class TestPanelProviders(BaseTestCase):

    def setUp(self):
        super(TestPanelProviders, self).setUp()
        create_panel_providers()

    def test_get_panels(self):
        response = self.app.get(
            '/panels',
            content_type='application/json'
        )
        data = safe_json_loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('panels' in data)
