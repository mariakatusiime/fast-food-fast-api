from flask import Flask,jsonify,abort,make_response,request
from controllers.db import Dbase
from models.ordermodel import CustomerOrders
from models.usermodel import Users

myapp = Flask(__name__)


#order = self.orderm.get_order

@myapp.route("/", methods = ['GET'])
def index(self):
    return jsonify({'Hoody':'Welcome to my web app'}),200


@myapp.route("/auth/signup/",methods=['POST'])
def user_signup(self):
    pass
    


@myapp.route("/auth/login/",methods=['POST'])
def user_login():
    pass


@myapp.route("/users/orders/",methods=['GET'])
def get_orders():
    order = request.json
    ordem = CustomerOrders(order.get('dish'),order.get('price'),order.get('status'),order.get('user_id'))

    return jsonify({'orders':ordem.get_orders()})


@myapp.route("/users/orders/",methods=['POST'])
def make_order():
    order = request.json
    ordem = CustomerOrders(order.get('dish'),order.get('price'),order.get('status'),order.get('user_id'))


    return jsonify({'order':ordem.create_orders()}), 201



@myapp.route("/users/orders/<int:id>",methods=['GET'])
def get_order(id):
    pass


@myapp.route("/users/orders/<int:id>",methods=['PUT'])
def update_order_status(id):
    pass


@myapp.route("/menu",methods=['GET'])
def get_menu():
    pass


@myapp.route("/menu",methods=['POST'])
def add_menu_item():
    pass
    
