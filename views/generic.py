from flask import jsonify, request

from database import Database


def index():
    return jsonify({"msg": "Healthy"})
