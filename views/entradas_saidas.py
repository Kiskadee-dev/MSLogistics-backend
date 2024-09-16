from models import EntradaESaida, Usuario
from flask import jsonify, request
from playhouse.shortcuts import model_to_dict
from datetime import datetime
from peewee import DoesNotExist
from responses import Responses, Messages


def entradas_e_saidas_get_list():
    "Retorna lista de entradas e saídas"
    return jsonify(
        [
            model_to_dict(query, exclude=Usuario.senha)
            for query in EntradaESaida.select()
        ]
    )


def entradas_e_saidas_create():
    form = request.form
    mercadoria = EntradaESaida(
        mercadoria=form.get("mercadoria"),
        quantia=form.get("quantia"),
        tipo_operacao=form.get("tipo_operacao"),
        data_e_hora=form.get("data_e_hora"),
        local=form.get("local"),
        criado_por=1,
    )
    mercadoria.save()
    return Responses.created()


def entradas_e_saidas_read():
    form = request.form
    id = form.get("id")
    if not id:
        return Responses.bad_request(Messages.no_id)
    entradas_e_saidas = EntradaESaida.get(EntradaESaida.id == id)
    return jsonify(model_to_dict(entradas_e_saidas, exclude=[Usuario.senha])), 200


def entradas_e_saidas_update():
    form = request.form

    id = form.get("id")  # ID of the entry to update

    if not id:
        return Responses.bad_request(Messages.no_id)

    # Try to find the EntradaESaida record by id
    try:
        entrada_saida = EntradaESaida.get(EntradaESaida.id == id)
    except DoesNotExist:
        return Responses.bad_request(Messages.record_not_found)

    # Prepare the update data
    update_data = {}
    mercadoria = form.get("mercadoria")
    quantia = form.get("quantia")
    tipo_operacao = form.get("tipo_operacao")
    data_e_hora = form.get("data_e_hora")

    if mercadoria:
        update_data["mercadoria"] = mercadoria
    if quantia:
        update_data["quantia"] = quantia
    if tipo_operacao:
        update_data["tipo_operacao"] = tipo_operacao
    if data_e_hora:
        try:
            update_data["data"] = datetime.strptime(data_e_hora, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return Responses.bad_request(Messages.invalid_date)

    # Update the record if any fields were provided
    if update_data:
        EntradaESaida.update(**update_data).where(EntradaESaida.id == id).execute()
        return Messages.ok()
    else:
        return Responses.bad_request(Messages.no_fields_to_update)


def entradas_e_saidas_delete():
    form = request.form
    id = form.get("id")
    try:
        entrada_e_saida = EntradaESaida.get(EntradaESaida.id == id)
        entrada_e_saida.delete()
        return Responses.ok(Messages.deleted)
    except DoesNotExist:
        return Responses.not_found(Messages.record_not_found)
