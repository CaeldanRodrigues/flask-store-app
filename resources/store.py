import uuid
from flask import request
from  flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import StoreSchema

blp = Blueprint('Stores', __name__, description='Operations on stores')

@blp.route('/store/<string:store_id>')
class Store(MethodView):
    @blp.response(201, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {'message': 'store deleted'}
        except KeyError:
            abort(404, message='store not found')


@blp.route('/store')
class StoreList(MethodView):
    @blp.response(201, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
            
        for store in stores.values():
            if (store_data['name'] == store['name']):
                abort(400, message='store already exists')

        store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": store_id}
        stores[store_id] = new_store

        return new_store
