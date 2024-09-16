from flask import jsonify, request

from models import Usuario


def usuario_get_list():
    query = Usuario.select()
    user_list = [
        {"id": usuario.id, "nome": usuario.nome, "email": usuario.email}
        for usuario in query
    ]
    return jsonify(user_list)
