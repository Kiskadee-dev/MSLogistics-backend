from flask import jsonify, request
from models import Mercadoria, Usuario
from playhouse.shortcuts import model_to_dict
import serializer
from peewee import IntegrityError


def mercadoria_get_list():
    return jsonify(
        [model_to_dict(item, exclude=[Usuario.senha]) for item in Mercadoria.select()]
    )


def mercadoria_create():
    """Creates an object

    Parameters
    ----------

    Returns
    -------
    Dict
        Returns status code
    """

    mercadoria = serializer.mercadoria(request.form)
    mercadoria.save()


    return jsonify({"msg": "Created."}), 200


def mercadoria_read(pk: int):
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
    query = Mercadoria.get_or_none(Mercadoria.id == pk)
    if query is None:
        return jsonify({"msg": "not found"}), 404
    return jsonify(deserialize_mercadoria(model_to_dict(query)))


def mercadoria_update():
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


def mercadoria_delete(pk: int):
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
