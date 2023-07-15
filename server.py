from requests import request
from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    message = "Hello, welcome to the calculator application!"

    # Return the greeting message
    return message

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()

    # Retrieve the numbers to be added
    num1 = data['num1']
    num2 = data['num2']

    # Perform the addition operation
    result = num1 + num2

    # Create a response object with the result
    response = {
        'result': result
    }

    # Return the response as JSON
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()

    # Perform the subtraction operation
    result = data['num1'] - data['num2']

    # Create a response object with the result
    response = {
        'result': result
    }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
