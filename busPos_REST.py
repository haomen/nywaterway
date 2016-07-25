#!/usr/bin/env python

# from flask import Flask,request
# from flask_restful import Resource, Api

# app=Flask(__name__)
# api=Api(app)
# totos={}

# class TodoSimple(Resource):
#     def get(self,todo_id):
#         return {todo_id,totos[todo_id]}

#     def put(self,todo_id):
#         totos[todo_id]=request.form['data']
#         return {todo_id,totos[todo_id]}

# api.add_resource(TodoSimple,'/<string:todo_id>')

# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=30444,debug=True)
