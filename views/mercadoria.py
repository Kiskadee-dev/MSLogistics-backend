from flask import jsonify, request
from models import Mercadoria
from playhouse.shortcuts import model_to_dict


def get_list():
    lista_mercadorias = [
        {
            "id": m.id,
            "nome": m.nome,
            "descricao": m.descricao,
            "quantia": m.quantia,
            "criado_em": m.criado_em,
            "criado_por": {"id": m.criado_por.id, "nome": m.criado_por.nome},
        }
        for m in Mercadoria.select()
    ]
    # TODO: Retornar todas as mercadorias
    return jsonify(lista_mercadorias)


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
