from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")
