import unittest
from flask import json
from views.api import myapp
class Apptest(unittest.TestCase):
    def setUp(self):
        self.app = myapp.test_client()
    def test_index_method_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)
    def test_index_return(self): 
        response = self.app.get('/')
        self.assertEqual(response.data,b'{"Hoody":"Welcome to my web app"}\n')
