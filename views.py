from flask import request, jsonify
from database import Database


def index():
    return "Hello"


def get_list():
    # TODO: Retornar todas as mercadorias
    return jsonify({"example": "get"})


def create():
    """Creates an object

    Parameters
    ----------


    Returns
    -------
    Dict
        Returns the info about the object
    """
    # TODO: Retornar JSON do objeto
    pk = request.form["pk"] if "pk" in request.form else None
    return f"get {jsonify(request.form)}"


def read(pk: int):
    """Gets info about an object

    Parameters
    ----------
    pk : int
        Id of the object

    Returns
    -------
    Dict
        Returns the info about the object
    """
    # TODO: Retornar JSON do objeto
    return jsonify({"pk": pk})


def update():
    """Updates an object

    Parameters
    ----------


    Returns
    -------
    Dict
        Returns the info about the object
    """
    # TODO: Retornar JSON do objeto
    pk = request.form["pk"] if "pk" in request.form else None
    return jsonify(request.form)


def delete(pk: int):
    """Deletes an object

    Parameters
    ----------
    pk : int
        Id of the object

    Returns
    -------
    200 Ok or 404.
    """
    # TODO: Retornar JSON do objeto
    return jsonify({"pk": pk})
