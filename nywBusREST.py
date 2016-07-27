#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
from nywBusPos import nywBusPos
import json
app = Flask(__name__)
api = Api(app)

todos = {}

class NywBusLocation(Resource):
    def get(self, route_id):
        a_route=nywBusPos(int(route_id))
        #return 'callback('+json.dumps(a_route.queryBusGPSPositionORGeojson())+');'
        #return '{0}({1})'.format('callback',json.dumps(a_route.queryBusGPSPositionORGeojson()))
        s1=jsonify(a_route.queryBusGPSPositionORGeojson())
        return s1

    # leave the put method exmpty for now, only GET
    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}

api.add_resource(NywBusLocation, '/nywaterway/<string:route_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=30444,debug=True)
