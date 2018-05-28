from api.logic import recur_collection_search, ilen
from api.utils.test_base import BaseTestCase


def create_test_dict():
    return {'a': list(range(1, 15)), 'b': [], 'c': {'ce': list(range(1, 13)), 'cd': 'aa'}}


class TestPricingCalculators(BaseTestCase):

    def setUp(self):
        super(TestPricingCalculators, self).setUp()
        self.test_dict = create_test_dict()

    def test_price_estimates(self):
        result = ilen(recur_collection_search(self.test_dict))
        self.assertIsInstance(result, int, msg="TestPricingCalculators returns odd type")
        self.assertEqual(result, 2, msg="TestPricingCalculators failed to match properly")
