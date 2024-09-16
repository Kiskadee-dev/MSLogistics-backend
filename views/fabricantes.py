from models import Fabricante, Usuario
from flask import jsonify, request
from database import Database
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
from datetime import datetime


def fabricante_get_list():
    return jsonify(
        [model_to_dict(query, exclude=[Usuario.senha]) for query in Fabricante.select()]
    )


def fabricante_create():
    """Cria um novo fabricante

    Parameters
    ----------
    nome : str
        Nome único do fabricante
    descricao : str
        Descrição do fabricante
    criado_por : Usuario
        O usuário que criou, proveniente da autenticação
    """
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    db = Database.get()
    # TODO: Obter usuário do token
    admin = Usuario.get(Usuario.nome == "Admin")
    with db.atomic:
        fab = Fabricante(nome=nome, descricao=descricao, criado_por=admin)
        fab.save()


def fabricante_read():
    id = request.form.get("id")
    if not id:
        return jsonify({"msg": "No id provided"}), 400
    fab = Fabricante.get_or_none(Fabricante.id == id)
    return jsonify(model_to_dict(fab, exclude=[Usuario.senha]))


def fabricante_update():
    form = request.form
    id = form.get("id")
    nome = form.get("nome")
    descricao = form.get("descricao")
    criado_em = form.get("criado_em")
    criado_por = form.get("criado_por")

    if not id:
        return jsonify({"msg": "No id provided"}), 400
    try:
        fabricante = Fabricante.get(Fabricante.id == id)
    except DoesNotExist:
        return jsonify({"msg": "Fabricante not found"}), 404

    update_data = {}
    if nome:
        update_data["nome"] = nome
    if descricao:
        update_data["descricao"] = descricao
    if criado_em:
        try:
            update_data["criado_em"] = datetime.strptime(criado_em, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"msg": "Invalid date format"}), 400
    if criado_por:
        update_data["criado_por"] = (
            criado_por  # Assuming this is the correct type (e.g., a user ID)
        )

    if update_data:
        Fabricante.update(**update_data).where(Fabricante.id == id).execute()
        return jsonify({"msg": "Fabricante updated successfully"}), 200
    else:
        return jsonify({"msg": "No fields to update"}), 400

def fabricante_delete():
    id = request.form.get('id')
    if not id:
        return jsonify({"msg": "No id provided"}), 400
    try:
        fab = Fabricante.get(Fabricante.id == id)
        fab.delete()
    except DoesNotExist:
        return jsonify({"msg": "Fabricante not found"}), 404
