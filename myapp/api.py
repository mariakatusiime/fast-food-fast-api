from flask import Flask,jsonify,abort,make_response,request
from models.orders import CustomerOrders

#instantiating a flask app/ creating app oject from Flask class
app = Flask(__name__) 

#error handling done here
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
@app.errorhandler(409)
def already_exists(error):
    return make_response(jsonify( { 'error': 'Already exists' } ), 409)
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
@app.errorhandler(501)
def whitespaces_or_empty(error):
    return make_response(jsonify( { 'error': 'Whitespace or empty or string length is less than 3' } ), 501)
@app.errorhandler(500)
def whitespaces_or_empty(error):
    return make_response(jsonify( { 'error': 'Negative or zero price' } ), 500)



#initialising some orders
order1 = {'id':1,'dish':"fish",'price':1200}
order2 ={'id':2,'dish':"pork",'price':1500}

#creating instance of class CustomerOrders
cus = CustomerOrders()        
cus.orders.append(order1)
cus.orders.append(order2)   

#Checking if dish already exists
def checkdishname(dish):
    return next(filter(lambda d : d['dish'] == dish,cus.orders),None)

#checking for the data types
def checkdatatypes(dish,price):
    if not isinstance(dish,str) or not isinstance(price, int):
        return True

#checking for white space and length
def check_for_whitespaces(dish, price):
    if dish.isspace() :
        return True
    if len(dish)<3:
        return True
def check_if_priceisnegative(price):
    if price <= 0:
        return True
#home endpoint
@app.route("/", methods=['GET'])
def get_index():
    return jsonify({'Hoolay':'Hi there welcome to my app'}),200

#get all orders endpoint
@app.route("/fast-food-fast/api/v1/orders" , methods=['GET'])
def get_orders():
    return jsonify({'orders':cus.orders}),200
    print (cus.orders)

#get a specific order using its id
@app.route("/fast-food-fast/api/v1/orders/<int:order_id>" , methods=['GET'])
def get_order(order_id):
    order = [order for order in cus.orders if order['id'] == order_id]
    if len(order)==0:
        abort(404)

    return jsonify({'order':order[0]}),200

# make order endpoint
@app.route("/fast-food-fast/api/v1/orders" , methods=['POST'])
def create_orders():
    if not request.json or 'dish' not in request.json or 'price' not in request.json :
        abort(400)


    order_id=len(cus.orders)+1
    dish = request.json['dish']
    price = request.json['price']

    if check_for_whitespaces(dish,price):
        abort(501)
    if checkdatatypes(dish,price):
        abort(400)
    if checkdishname(dish) is not None:
        abort(409)
    if check_if_priceisnegative(price):
        abort(500)

    
    order = {
        'id': order_id,
        'dish': dish,
        'price': price
    }
   
    cus.orders.append(order)
    return jsonify({'order': order}), 201
    
#updating order endpoint
@app.route("/fast-food-fast/api/v1/orders/<int:order_id>" , methods=['PUT'])
def update_orders(order_id):
    order = [order for order in cus.orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    #checking for json format
    if not request.json or 'dish' not in request.json or 'price' not in request.json :
        abort(400)
 
    order[0]['dish'] = request.json.get('dish', order[0]['dish'])
    order[0]['price'] = request.json.get('price', order[0]['price'])
    
    if check_for_whitespaces(order[0]['dish'],order[0]['dish']):
        abort(501)
    if checkdatatypes(order[0]['dish'],order[0]['price']):
        abort(400)

    return jsonify({'order': order[0]}),201
    


