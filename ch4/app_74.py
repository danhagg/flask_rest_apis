from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

# Flask restful returns dictionaries so we no longer have to jsonify
class Item(Resource):
    def get(self, name):
        [item for item in items if item['name'] == name]
        # Next gives first item
        # next can also raise an error if no items left (None)
        item = next(filter(lamda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lamda x: x['name'] == name, items), None) is not None:
            return {'message': f'An item with name {name} already exists'}, 400

        # postman requires Content-Type = Application/json for below line
        request_data = request.get_json()
        new_item = {'name': name, 'price': request_data['price']}
        items.append(new_item)
        return jsonify(new_item)

class ItemList(Resource):
    def get(self):
        return({'items': items})

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run()