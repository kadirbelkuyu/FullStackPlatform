from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

@main.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return jsonify(message=f"Hello, {name}!")