from flask import jsonify, request
from models import Operacao, Usuario
from playhouse.shortcuts import model_to_dict


def tipos_get_list():
    "Obtém lista de tipos de operações: entrada/saída/..."

    return jsonify(
        [
            model_to_dict(query, exclude=[Usuario.senha])
            for query in Operacao.select()
        ]
    )
