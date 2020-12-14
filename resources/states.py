
import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

state = Blueprint('states', 'state')


@dog.route('/', methods=["GET"])
def get_all_dogs():
    try:
        states = [model_to_dict(state) for state in models.State.select()]
        print(states)
        return jsonify(data=states, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})