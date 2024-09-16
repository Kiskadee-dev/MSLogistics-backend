from flask import jsonify, request
from models import TipoMercadoria, Usuario
from playhouse.shortcuts import model_to_dict


def tipos_mercadoria_get_list():
    tipos = [
        model_to_dict(query, exclude=[Usuario.senha])
        for query in TipoMercadoria.select()
    ]
