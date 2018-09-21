from flask import Flask,jsonify,abort,make_response,request

app =Flask(__name__) 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


orders = [
    {'id':1,
     'dish':"fish",
     'price':1200
    },
    {'id':2,
     'dish':"pork",
     'price':1500
    }
]

@app.route("/fast-food-fast/api/v1/orders" , methods=['GET'])
def get_orders():
    return jsonify({'orders':orders}),200
@app.route("/fast-food-fast/api/v1/orders/<int:order_id>" , methods=['GET'])
def get_order(order_id):
    order = [order for order in orders if order['id'] == order_id]
    if len(order)==0:
        abort(404)

    return jsonify({'order':order[0]}),200

@app.route("/fast-food-fast/api/v1/orders" , methods=['POST'])
def create_orders():
    if not request.json or not 'dish' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'dish': request.json['dish'],
        'price': request.json.get('price', 1200)
    }
    order.append(orders)
    return jsonify({'task': order}), 201


@app.route("/fast-food-fast/api/v1/orders" , methods=['PUT'])
def update_orders():
    pass
@app.route("/fast-food-fast/api/v1/orders" , methods=['DELETE'])
def delete_orders():
    pass


if __name__ == '__main__':
    app.run(debug=True)
