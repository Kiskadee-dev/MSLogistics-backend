from models import Mercadoria, Usuario
from flask import jsonify, request
from playhouse.shortcuts import model_to_dict


def entradas_e_saidas_get_list():
    "Retorna lista de entradas e saídas"
    return jsonify(
        [model_to_dict(query, exclude=Usuario.senha) for query in Mercadoria.select()]
    )


def create():
    pass
