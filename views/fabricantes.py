from models import Fabricante, Usuario
from flask import jsonify
from database import Database
from playhouse.shortcuts import model_to_dict


def fabricante_get_list():
    return jsonify(
        [model_to_dict(query, exclude=[Usuario.senha]) for query in Fabricante.select()]
    )


def create(nome: str, descricao: str):
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
    db = Database.get()
    # TODO: Obter usuário do token
    admin = Usuario.get(Usuario.nome == "Admin")
    with db.atomic:
        fab = Fabricante(nome=nome, descricao=descricao, criado_por=admin)
        fab.save()
