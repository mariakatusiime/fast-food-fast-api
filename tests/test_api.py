from unittest import TestCase
from flask import json
from myapp.api import app,cus
from models.orders import CustomerOrders #joel
# cus = CustomerOrders() #joel

class Testing(TestCase):
    def setUp(self):
        self.client=app.test_client
        self.cus = CustomerOrders()
    def tearDown(self):
        cus.orders=[]
        
    def test_get_orders(self):

        order1 = {"dish":"fish","id":1,"price":1200}
        # cus.orders.append(order1)
        l1 = len(cus.orders)
        self.client().post('/fast-food-fast/api/v1/orders', data = json.dumps(order1), content_type='application/json')
        l2 = len(cus.orders)
        gt=self.client().get('/fast-food-fast/api/v1/orders')
        self.assertEqual(gt.status_code,200)
        self.assertEqual(l2, l1+1)

        # self.assertEqual(gt.data,b'{"orders":[{"dish":"fish","id":1,"price":1200},{"dish":"pork","id":2,"price":1500},{"dish":"mutton","id":3,"price":3400}]}\n')
    
    
    def test_get_order(self):
        
        order = dict(id=1,dish="fish",price=1200)
        cus.orders.append(order)
        gt = self.client().get('/fast-food-fast/api/v1/orders/1')
        self.assertEqual(gt.status_code,200)
        self.assertEqual(gt.data,b'{"order":{"dish":"fish","id":1,"price":1200}}\n')
    
    
    def test_get_order_with_unknown_id(self):
        gt = self.client().get('/fast-food-fast/api/v1/orders/6')
        self.assertEqual(gt.status_code,404)


    def test_create_order(self):
        # self.assertFalse(cus.orders)
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data = json.dumps({'dish':"mutton",'price':3400}))
        self.assertEqual(gt.status_code,201)


    def test_created_order_already_exist(self):
        order = dict(id=4,dish="fish",price=3400)
        cus.orders.append(order)
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data = json.dumps(order))
        self.assertEqual(gt.status_code,409)

    def test_if_string_is_empty(self):
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data= json.dumps(dict(id=5,dish="",price=3400)))
        self.assertEqual(gt.status_code,501)
    def test_if_check_for_negative_integer(self):
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data= json.dumps(dict(id=6,dish="cake",price=-400)))
        self.assertEqual(gt.status_code,400)
    def test_if_check_for_zero_price(self):
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data= json.dumps(dict(dish="milk",price= 0)))
        self.assertEqual(gt.status_code,400)
    def test_if_check_for_string_in_place_of_price(self):
        gt = self.client().post('/fast-food-fast/api/v1/orders', content_type='application/json',data= json.dumps(dict(dish="mutton",price="read")))
        self.assertEqual(gt.status_code,400)

    def test_update_order(self):
        order = dict(id=4,dish="fish",price=1200)
        cus.orders.append(order)
        gt = self.client().put('/fast-food-fast/api/v1/orders/4',content_type='application/json', data = json.dumps({"dish":"juicy","price":1000}))
        self.assertEqual(gt.status_code,201)

    def test_update_order_for_unknown_order_id(self):
        gt = self.client().put('/fast-food-fast/api/v1/orders/6',content_type='application/json', data = json.dumps(dict(dish="cake", price=2000)))
        self.assertEqual(gt.status_code,404)  

# print()