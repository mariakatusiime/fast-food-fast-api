from unittest import TestCase
from app import app

class Testing(TestCase):

    def setUp(self):
        self.client=app.test_client

    def test_get_orders(self):
        gt=self.client().get('/fast-food-fast/api/v1/orders')
        self.assertEquals(gt.status_code,201)
        