from api.logic import recur_dict_search
from api.utils.test_base import BaseTestCase


def create_test_dict():
    return {'a': list(range(1, 15)), 'b': [], 'c': {'ce': list(range(1, 13)), 'cd': 'aa'}}


class TestPricingCalculators(BaseTestCase):

    def setUp(self):
        super(TestPricingCalculators, self).setUp()
        self.test_dict = create_test_dict()

    def test_price_estimates(self):
        result = len(list(recur_dict_search(self.test_dict)))
        self.assertIsInstance(result, int)
        self.assertTrue(result == 2)
