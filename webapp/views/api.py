from flask import Flask,jsonify,abort,make_response,request
from flask_jwt_extended import (JWTManager,jwt_required,create_access_token,get_jwt_identity)
from webapp.controllers.db import Dbase
from webapp.models.ordermodel import CustomerOrders
from webapp.models.usermodel import Users
from webapp.models.menumodel import Menu

myapp = Flask(__name__)
myapp.config['JWT_SECRET_KEY'] = 'super_secret'
jwt = JWTManager(myapp)

@myapp.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
@myapp.errorhandler(409)
def already_exists(error):
    return make_response(jsonify( { 'error': 'Already exists' } ), 409)
@myapp.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
@myapp.errorhandler(501)
def whitespaces_or_empty(error):
    return make_response(jsonify( { 'error': 'Whitespace or empty or string length is less than 3' } ), 501)



#checking for the data types
def checkdatatypes(dish,status,price):
    if not isinstance(dish,str) or not isinstance(dish,str) or not isinstance(price, int):
        return True

#checking for white space and length
def check_for_whitespaces(dish,status):
    if dish.isspace() or status.isspace() :
        return True   
    if len(dish)<3:
        return True
def check_if_priceisnegative(price,quantity):
    if price <= 0:
        return True
    if quantity <= 0:
        return True



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
    dish = order.get('dish')
    price = order.get('price')
    quantity = order.get('quantity')
    status = order.get('status')

    if not request.is_json:
        return jsonify({"message":"Your input is not json format"}),400
    if check_for_whitespaces(dish,status):
        abort(501)
    if checkdatatypes(dish,status,price):
        abort(400)
    if check_if_priceisnegative(price,quantity):
        abort(400)
    ordem = CustomerOrders(dish,price,quantity,status,order.get('user_id'))
    response = ordem.create_orders()
    return jsonify({'order':response}), 201



@myapp.route("/api/v2/users/orders/<int:id>",methods=['GET'])
def get_order(id):
   
    order_no = id
    response = CustomerOrders.get_order(order_no)
    return jsonify({'order details':response}),200
    


@myapp.route("/api/v2/users/orders/<int:order_no>",methods=['PUT'])
def update_order_status(order_no):
    order = request.json
    status = order.get('status')
    ordem = CustomerOrders.update_order_status(status,order_no)
    return jsonify({'order':ordem}),201


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


    
