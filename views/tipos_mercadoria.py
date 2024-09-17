from flask import jsonify, request
from playhouse.shortcuts import model_to_dict

from models import TipoMercadoria, Usuario
from responses import Messages, Responses


def tipos_mercadoria_get_list():
    return jsonify(
        [
            model_to_dict(query, exclude=[Usuario.senha])
            for query in TipoMercadoria.select()
        ]
    )


def tipos_mercadoria_create():
    form = request.form
    nome = form.get("nome")
    tipo_mercadoria = TipoMercadoria(nome=nome, criado_por=1)
    tipo_mercadoria.save()
    return Responses.created()


def tipos_mercadoria_read():
    form = request.form
    id = form.get("id")
    if not id:
        return Responses.bad_request(Messages.no_id)


def tipos_mercadoria_update():
    form = request.form
    id = form.get("id")
    if not id:
        return Responses.bad_request(Messages.no_id)

    updated_data = {}
    nome = form.get("nome")
    if nome:
        updated_data["nome"] = nome
    if updated_data:
        tipo_mercadoria = TipoMercadoria.get(TipoMercadoria.id == id)
        tipo_mercadoria.update(**updated_data)
        return Responses.ok()
    return Responses.bad_request(Messages.no_fields_to_update)


def tipos_mercadoria_delete():
    form = request.form
    id = form.get("id")
    if not id:
        return Responses.bad_request(Messages.no_id)
