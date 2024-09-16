from typing import Tuple, Any
from flask import jsonify
from enum import Enum


class Messages(Enum):
    no_id = "Field id is required."
    bad_request = "Bad request."
    record_not_found = "Record not found."
    ok = "Ok."
    created = "Created."
    no_fields_to_update = "No fields to update."
    deleted = "Deleted."
    invalid_date = "Invalid date format."


class Responses:
    @staticmethod
    def bad_request(msg: Messages = Messages.bad_request) -> Tuple[Any, Any]:
        msg = msg.value
        return jsonify({"msg": msg}), 400

    @staticmethod
    def not_found(msg: Messages = Messages.record_not_found) -> Tuple[Any, Any]:
        msg = msg.value

        return jsonify({"msg": msg}), 404

    @staticmethod
    def ok(msg: Messages = Messages.ok) -> Tuple[Any, Any]:
        msg = msg.value
        return jsonify({"msg": msg}), 200

    @staticmethod
    def created(msg: Messages = Messages.created) -> Tuple[Any, Any]:
        msg = msg.value
        return jsonify({"msg": msg}), 201
