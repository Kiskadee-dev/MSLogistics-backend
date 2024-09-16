from flask import jsonify, request
from playhouse.shortcuts import model_to_dict

from models import TipoOperacao, Usuario


def tipos_get_list():
    "Obtém lista de tipos de operações: entrada/saída/..."

    return jsonify(
        [
            model_to_dict(query, exclude=[Usuario.senha])
            for query in TipoOperacao.select()
        ]
    )
