from flask import request, jsonify
from database import Database


def index():
    return jsonify({"msg": "Healthy"})
