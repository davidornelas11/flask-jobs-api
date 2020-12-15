from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy

states = Blueprint('states', 'state')

@get_states.route('/', methods=["GET"])
def get_all_states():
    print(request.form['state'])
    try:
        print('it worked')
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})