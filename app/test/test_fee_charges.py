import unittest
import random
from manage import *
from app.main.service import exchange_service, currencies


class FeeChargeTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['Debug'] = False
        self.app = app.test_client()
        self.accummulated_fee= exchange_service.accummulated_fee
        self.currencies = currencies

    def tearDown(self):
        pass

    def test_fee_charge(self):
        service_fee_sum = 0
        fee_sum = 0
        for i in range(1,1000):
            from_currency = random.choice(list(self.currencies['rates'].keys()))
            to_currency = random.choice(list(self.currencies['rates'].keys()))
            exchange_amount = random.randrange(1,999)
            base_amount = self.currencies['rates'][from_currency].exchange
            currency_credits = self.currencies['rates'][from_currency].credit
            if currency_credits < exchange_amount:
                break
            fee_sum += round(base_amount * exchange_amount * 0.01, 4)
            info = {"from":from_currency, 'to':to_currency, 'exchange_amount':exchange_amount}
            response = self.app.post('/exchange/transaction', json=info)
            service_fee_sum += round(response.json['fee_amount'], 4)
        self.assertEqual(fee_sum, service_fee_sum)

    if __name__ == "__main__":
        unittest.main()
    