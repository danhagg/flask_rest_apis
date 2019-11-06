from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret_key_innit'
api = Api(app)

# jwt creates a new endpoint /auth
# we send /auth a username and password to endpoint
# jwt sends it over to authenticate function (that we defined)
# cmpares the user password from /auth
# returns a jwt token
# jwt sent on all futue request
# jwt identity function
jwt = JWT(app, authenticate, identity)

items = []

# Flask restful returns dictionaries so we no longer have to jsonify
class Item(Resource):
    @jwt_required()
    def get(self, name):
        # [item for item in items if item['name'] == name]
        # Next gives first item
        # next can also raise an error if no items left (None)
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': f'An item with name {name} already exists'}, 400

        # postman requires Content-Type = Application/json for below line
        request_data = request.get_json()
        new_item = {'name': name, 'price': request_data['price']}
        items.append(new_item)
        return jsonify(new_item)

    def delete(self, name):
        global items
        items = list(filter(lambda X: x['name'] != name, items))
        return {'message': 'item deleted'}

    def put(self, name):
        data =  request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return({'items': items})

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)