from flask import Flask,jsonify,abort,make_response,request
from controllers.db import Dbase
from models.ordermodel import CustomerOrders
from models.usermodel import Users

myapp = Flask(__name__)


#order = self.orderm.get_order

@myapp.route("/", methods = ['GET'])
def index():
    return jsonify({'Hoody':'Welcome to my web app'}),200


@myapp.route("/auth/signup/",methods=['POST'])
def user_signup():
    log = request.json
    details = Users(log.get('username'),log.get('email'),log.get('password'))
    response = details.user_signup()
    return jsonify({'signup successful':response})



@myapp.route("/auth/login/",methods=['POST'])
def user_login():
    log = request.json
    username =log.get('username')
    password =log.get('password')
    details = Users(log.get('username'),log.get('email'),log.get('password'))
    
    response = details.user_login(username,password)
    
    return jsonify({'Successful':response}),200



@myapp.route("/users/orders/",methods=['GET'])
def get_orders():

    return jsonify({'orders':CustomerOrders.get_orders()}),200


@myapp.route("/users/orders/",methods=['POST'])
def make_order():
    order = request.json
    ordem = CustomerOrders(order.get('dish'),order.get('price'),order.get('status'),order.get('user_id'))

    return jsonify({'order':ordem.create_orders()}), 201



@myapp.route("/users/orders/<int:id>",methods=['GET'])
def get_order(id):
   
    order_no = id
    return jsonify({'order details':CustomerOrders.get_order(order_no)}),200
    


@myapp.route("/users/orders/<int:id>",methods=['PUT'])
def update_order_status(id):
    order = request.json
    ordem = CustomerOrders(order.get('dish'),order.get('price'),order.get('status'),order.get('user_id'))
    order_no = id
    status = order.get('status')
    return jsonify({'order':ordem.update_order_status(status,order_no)}),201


@myapp.route("/menu",methods=['GET'])
def get_menu():
    pass


@myapp.route("/menu",methods=['POST'])
def add_menu_item():
    pass
    
