# jsonify is a method (lowercase) not a class
from flask import Flask, jsonify

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
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    # The stores list is defined above
    # Json cannot be a list so we convert to a dict
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name: price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run()