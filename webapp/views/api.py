from flask import Flask,jsonify,abort,make_response,request
from flask_jwt_extended import (JWTManager,jwt_required,create_access_token,get_jwt_identity)
from webapp.controllers.db import Dbase
from webapp.models.ordermodel import CustomerOrders
from webapp.models.usermodel import Users
from webapp.models.menumodel import Menu

myapp = Flask(__name__)
myapp.config['JWT_SECRET_KEY'] = 'super_secret'
jwt = JWTManager(myapp)


#order = self.orderm.get_order

@myapp.route("/", methods = ['GET'])
def index():
    return jsonify({'Hoody':'Welcome to my web app'}),200


@myapp.route("/api/v2/auth/signup/",methods=['POST'])
def user_signup():
    log = request.json
    username = log.get('username')
    email = log.get('email')
    details = Users(username,email,log.get('password'))
    response = details.user_signup()
    if response == "success":
       return ('User successfully registered')
    return("User with username:{} and email:  {} already exists".format(username,email),409)
    



@myapp.route("/api/v2/auth/login/",methods=['POST'])
def user_login():
    if not request.is_json:
        return jsonify({"message":"Your input is not json format"}),400
    log = request.json
    usernam =log.get('username')
    passwor =log.get('password')
    if not usernam:
        return jsonify({"message":"username parameter is missing"}),400
    if not passwor:
        return jsonify({"message":"password parameter is missing"}),400
    details = Users(log.get('username'),log.get('email'),log.get('password'))
    
    response = details.user_login()
    
    if response == "none":
        return jsonify({"message":"User name or password is wrong"}),404

    access_token = create_access_token(identity=response,expires_delta=None)
    
    return jsonify({'Message':access_token}),200



@myapp.route("/api/v2/users/orders/",methods=['GET'])
def get_orders():
    response =CustomerOrders.get_orders()

    return jsonify({'orders':response}),200


@myapp.route("/api/v2/users/orders/",methods=['POST'])
@jwt_required
def make_order():
    order = request.json
    ordem = CustomerOrders(order.get('dish'),order.get('price'),order.get('status'),order.get('user_id'))
    quantity = 1
    response = ordem.create_orders(quantity)
    return jsonify({'order':response}), 201



@myapp.route("/api/v2/users/orders/<int:id>",methods=['GET'])
def get_order(id):
   
    order_no = id
    response = CustomerOrders.get_order(order_no)
    return jsonify({'order details':response}),200
    


@myapp.route("/api/v2/users/orders/<int:id>",methods=['PUT'])
def update_order_status(id):
    order = request.json
    ordem = CustomerOrders(order.get('dish'),order.get('price'),order.get('status'),order.get('user_id'))
    order_no = id
    status = order.get('status')
    response = ordem.update_order_status(status,order_no)
    return jsonify({'order':response}),201


@myapp.route("/api/v2/menu",methods=['GET'])
def get_menu():
    response = Menu.get_menu()
    return jsonify({'Available_menu':response}),200
    

@myapp.route("/api/v2/menu",methods=['POST'])
def add_menu_item():
    menu = request.json
    ordem = Menu(menu.get('dish'),menu.get('price'))
    response = ordem.add_menu_items()

    return jsonify({'Menu added':response}),201


    
