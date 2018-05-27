#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.logic import price
from api.utils.test_base import BaseTestCase
from api.logic.pricing import ThirdPricingLogic, SecondPricingLogic, FirstPricingLogic


def create_pricing_calculators():
    FirstPricingLogic()
    SecondPricingLogic()
    ThirdPricingLogic()


class TestPricingCalculators(BaseTestCase):

    def setUp(self):
        super(TestPricingCalculators, self).setUp()
        create_pricing_calculators()

    def test_price_estimates(self):
        print(price[FirstPricingLogic.panel_id])
        print(price[SecondPricingLogic.panel_id])
        print(price[ThirdPricingLogic.panel_id])

        self.assertTrue(FirstPricingLogic.panel_id in price)
        self.assertTrue(SecondPricingLogic.panel_id in price)
        self.assertTrue(ThirdPricingLogic.panel_id in price)
