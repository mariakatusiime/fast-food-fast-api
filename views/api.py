from flask import Flask,jsonify,abort,make_response,request
from controllers.db import Dbase
from models.ordermodel import CustomerOrders
from models.usermodel import Users

myapp = Flask(__name__)



#userm = Users()
orderm = CustomerOrders(1,'fish',1500,'pending',1)

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
    return jsonify({'orders':orderm.get_orders()})


@myapp.route("/users/orders/",methods=['POST'])
def make_order():
    pass


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
    
