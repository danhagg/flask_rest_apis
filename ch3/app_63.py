# jsonify is a method (lowercase) not a class
from flask import Flask, jsonify, request

app = Flask(__name__)

# stores list is a list of dicts
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

# JSON NOT a dictionary. 
# It is a long string.
# " not '
# Javascript does not understand Python dictionaries but does understand strings.
# jsonift converts dictionaries to json
# CANNOT return a list


# POST /store data: {name:}
@app.route('/store', methods=['POST']) # only accessible by post
def create_store():
    # This is the request to this endpoint
    # Gets that data (store name) back
    # get json also converts that json string to python dict. 
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    # Append stores list
    stores.append(new_store)
    # Has to be jsonified for browser
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # If store name matches, return it
    # If non match return error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': store not found})


# GET /store
@app.route('/store')
def get_stores():
    # The stores list is defined above
    # Json cannot be a list so we convert to a dict
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name: price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})

app.run()