from flask import Flask,jsonify,abort,make_response,request
from models.orders import CustomerOrders

app = Flask(__name__) 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

order1 = {'id':1,'dish':"fish",'price':1200}
order2 ={'id':2,'dish':"pork",'price':1500}

cus = CustomerOrders()        
cus.orders.append(order1)
cus.orders.append(order2)          

app.route("/" , methods=['GET'])
def get_orders():
    return jsonify({'orders high there welcome to my app'}),200
@app.route("/fast-food-fast/api/v1/orders" , methods=['GET'])
def get_orders():
    return jsonify({'orders':cus.orders}),200
    print (cus.orders)
@app.route("/fast-food-fast/api/v1/orders/<int:order_id>" , methods=['GET'])
def get_order(order_id):
    order = [order for order in cus.orders if order['id'] == order_id]
    if len(order)==0:
        abort(404)

    return jsonify({'order':order[0]}),200

@app.route("/fast-food-fast/api/v1/orders" , methods=['POST'])
def create_orders():
    order_id=len(cus.orders)+1
    order = {
        'id': order_id,
        'dish': request.json['dish'],
        'price': request.json['price']
    }
    cus.orders.append(order)
    return jsonify({'order': order}), 201


@app.route("/fast-food-fast/api/v1/orders/<int:order_id>" , methods=['PUT'])
def update_orders(order_id):
    order = [order for order in cus.orders if order['id'] == order_id]
    if len(order) == 0:
        abort(404)
    
    order[0]['dish'] = request.json.get('dish', order[0]['dish'])
    order[0]['price'] = request.json.get('price', order[0]['price'])
    return jsonify({'order': order[0]}),201
    
if __name__ == '__main__':
    app.run(debug=True)


