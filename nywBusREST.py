#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
from nywBusPos import nywBusPos

app = Flask(__name__)
api = Api(app)

todos = {}

class NywBusLocation(Resource):
    def get(self, route_id):
        a_route=nywBusPos(int(route_id))
        return a_route.queryBusGPSPositionORGeojson()

    # leave the put method exmpty for now, only GET
    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}

api.add_resource(NywBusLocation, '/nywaterway/<string:route_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=30444,debug=True)
