from flask import jsonify, request
from models import Mercadoria, Usuario
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
from responses import Responses, Messages


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
    form = request.form
    mercadoria = Mercadoria(
        nome=form.get("nome"),
        numero_registro=form.get("numero_registro"),
        fabricante=form.get("fabricante"),
        tipo=form.get("tipo"),
        descricao=form.get("descricao"),
        criado_por=1,
    )
    mercadoria.save()
    return Responses.created()


def mercadoria_read(pk: int):
    """Gets info about Mercadoria

    Parameters
    ----------
    pk : int
        Id of the object

    Returns
    -------
    Dict
        Returns the info about the object
    """
    try:
        query = Mercadoria.get(Mercadoria.id == pk)
    except DoesNotExist:
        return Responses.not_found()
    return jsonify(model_to_dict(query, exclude=[Usuario.senha]))


def mercadoria_update():
    """Updates Mercadoria object

    Parameters
    ----------
    None

    Returns
    -------
    Dict
        Returns status code and update message
    """

    form = request.form
    mercadoria_id = form.get("id")  # Assuming 'id' is passed to identify the object

    if not mercadoria_id:
        return Responses.bad_request(Messages.no_id)

    # Try to get the Mercadoria object by ID
    try:
        mercadoria = Mercadoria.get(Mercadoria.id == mercadoria_id)
    except DoesNotExist:
        return Responses.not_found()

    # Prepare the update data
    update_data = {}
    nome = form.get("nome")
    numero_registro = form.get("numero_registro")
    fabricante = form.get("fabricante")
    tipo = form.get("tipo")
    descricao = form.get("descricao")

    if nome:
        update_data["nome"] = nome
    if numero_registro:
        update_data["numero_registro"] = numero_registro
    if fabricante:
        update_data["fabricante"] = fabricante
    if tipo:
        update_data["tipo"] = tipo
    if descricao:
        update_data["descricao"] = descricao

    # Perform the update if there are fields to update
    if update_data:
        Mercadoria.update(**update_data).where(Mercadoria.id == mercadoria_id).execute()
        return Responses.ok()
    else:
        return Responses.bad_request(Messages.no_fields_to_update)


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
    form = request.form
    id = form.get("id")
    if not id:
        return Responses.bad_request(Messages.no_id)
    mercadoria = Mercadoria.get(Mercadoria.id == id)
    mercadoria.delete()
    return Responses.ok(Messages.deleted)
