from flask import g

from craton.inventory.api.v1 import base


class Regions(base.Resource):

    def get(self):

        return [], 200, None

    def post(self):
        print(g.json)

        return None, 200, None


class RegionsId(base.Resource):

    def put(self, id):
        print(g.json)

        return None, 400, None

    def delete(self, id):

        return None, 400, None


class RegionsData(base.Resource):

    def put(self, id):
        print(g.json)

        return None, 400, None

    def delete(self, id):

        return None, 400, None
