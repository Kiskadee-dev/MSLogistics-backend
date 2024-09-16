from flask import jsonify, request
from models import TipoMercadoria, Usuario
from playhouse.shortcuts import model_to_dict
from responses import Responses, Messages


def tipos_mercadoria_get_list():
    tipos = [
        model_to_dict(query, exclude=[Usuario.senha])
        for query in TipoMercadoria.select()
    ]
    return jsonify({tipos})


def tipos_mercadoria_create():
    form = request.form
    nome = form.get("nome")
    tipo_mercadoria = TipoMercadoria(nome=nome, criado_por=1)
    return Responses.created()


def tipos_mercadoria_read():
    form = request.form
    id = form.get("id")
    if not id:
        return Responses.bad_request(Messages.no_id)
