from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
import sys

# Initialize Flask App
app = Flask(__name__)
api = Api(app)

# Helper function to get numbers safely
def get_numbers():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return num1, num2
    except (TypeError, ValueError):
        return None, None

# Define API Resources
class Add(Resource):
    def get(self):
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            return jsonify(error="Invalid or missing numbers")
        return jsonify(result=num1 + num2)

class Subtract(Resource):
    def get(self):
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            return jsonify(error="Invalid or missing numbers")
        return jsonify(result=num1 - num2)

class Multiply(Resource):
    def get(self):
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            return jsonify(error="Invalid or missing numbers")
        return jsonify(result=num1 * num2)

class Divide(Resource):
    def get(self):
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            return jsonify(error="Invalid or missing numbers")
        if num2 == 0:
            return jsonify(error="Division by zero is not allowed")
        return jsonify(result=num1 / num2)

# Assign Endpoints
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)

# Test in your browser or Postman:
# Addition: http://127.0.0.1:5000/add?num1=10&num2=5
# Subtraction: http://127.0.0.1:5000/subtract?num1=10&num2=5
# Multiplication: http://127.0.0.1:5000/multiply?num1=10&num2=5
# Division: http://127.0.0.1:5000/divide?num1=10&num2=5
