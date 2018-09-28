from unittest import TestCase
from flask import json
from myapp.api import app


class Testing(TestCase):

    def setUp(self):
        self.client=app.test_client

    def test_get_orders(self):
        
        gt=self.client().get('/fast-food-fast/api/v1/orders')
        self.assertEqual(gt.status_code,200)
        self.assertEqual(gt.data,b'{"orders":[{"dish":"fish","id":1,"price":1200},{"dish":"pork","id":2,"price":1500},{"dish":"mutton","id":3,"price":3400}]}\n')
    def test_get_order(self):
        gt = self.client().get('/fast-food-fast/api/v1/orders/1')
        self.assertEqual(gt.status_code,200)
        self.assertEqual(gt.data,b'{"order":{"dish":"fish","id":1,"price":1200}}\n')

    def test_create_order(self):
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data= json.dumps(dict(id=5,dish="mutton", price=3400)))
        self.assertEqual(gt.status_code,201)
    def test_update_order(self):
        gt = self.client().put('/fast-food-fast/api/v1/orders/1',content_type='application/json', data = json.dumps(dict(id=1,dish="fish", price=1800)))
        self.assertEqual(gt.status_code,201)

    def test_update_order_for_unknown_order_id(self):
        gt = self.client().put('/fast-food-fast/api/v1/orders/6',content_type='application/json', data = json.dumps(dict(id=6,dish="cake", price=2000)))
        self.assertEqual(gt.status_code,404)
            