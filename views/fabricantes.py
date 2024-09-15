from models import Fabricante, Usuario
from flask import jsonify
from database import Database


def get_list():
    fabs = [
        {
            "id": query.id,
            "nome": query.nome,
            "descricao": query.descricao,
            "criado_em": query.criado_em,
            "criado_por": {"id": query.criado_por.id, "nome": query.criado_por.nome},
        }
        for query in Fabricante.select()
    ]
    return jsonify(fabs)


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
