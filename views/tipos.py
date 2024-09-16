from flask import jsonify
from models import TipoMercadoria, Usuario
from playhouse.shortcuts import model_to_dict


def tipos_get_list():
    "Obtém lista de tipos de mercadoria"

    return jsonify(
        [model_to_dict(query, exclude=Usuario) for query in TipoMercadoria.select()]
    )
