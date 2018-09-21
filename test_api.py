from unittest import TestCase
from flask import json
from app import app

class Testing(TestCase):

    def setUp(self):
        self.client=app.test_client

    def test_get_orders(self):
        gt=self.client().get('/fast-food-fast/api/v1/orders')
        self.assertEquals(gt.status_code,200)
    def test_get_order(self):
        gt = self.client().get('/fast-food-fast/api/v1/orders/1')
        self.assertEquals(gt.status_code,200)
    def test_create_order(self):
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data= json.dumps(dict(id=5,dish="mutton", price="3400")))
        self.assertEquals(gt.status_code,201)
    def test_update_order(self):
        gt = self.client().put('/fast-food-fast/api/v1/orders/1',content_type='application/json', data = json.dumps(dict(status="accepted")))
        self.assertEquals(gt.status_code,201)
    