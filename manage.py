from os import getenv

from dotenv import load_dotenv

import models
from database import Database


def create_tables():
    """Applies the schema to the db"""

    db = Database.get()
    with db:
        db.create_tables(
            [
                models.Usuario,
                models.Fabricante,
                models.TipoMercadoria,
                models.TipoOperacao,
                models.Mercadoria,
                models.EntradaESaida,
            ]
        )


def dados_de_teste(testing=False):
    load_dotenv()
    Database.get(testing=testing).connect()
    try:
        adm_name = getenv("ADMIN_USER", "Admin")
        user_exists = (
            len(models.Usuario.select().where(models.Usuario.nome == adm_name)) == 1
        )

        if not user_exists:
            # Cria e insere admin
            admin = models.Usuario(
                nome=adm_name,
                senha=getenv("ADMIN_PASSWORD", "Admin"),
                email=getenv("ADMIN_EMAIL", "Admin@Admin.com"),
            )
            admin.save()
        admin = models.Usuario.get(models.Usuario.id == 1)

        # Cria um fabricante
        fab_exists = (
            len(
                models.Fabricante.select().where(
                    models.Fabricante.nome == "AgricultorXYZ"
                )
            )
            == 1
        )
        if not fab_exists:
            fab = models.Fabricante(
                nome="AgricultorXYZ",
                descricao="""Produtor de grãos""",
                criado_por=admin,
            )
            fab.save()
        fab = models.Fabricante.get(models.Fabricante.nome == "AgricultorXYZ")

        # Cria tipos de operações de entrada e saída

        ops_entrada_exists = (
            len(
                models.TipoOperacao.select().where(
                    models.TipoOperacao.nome == "entrada"
                )
            )
            == 1
        )
        if not ops_entrada_exists:
            models.TipoOperacao(
                nome="entrada",
                descricao="""Produtos que entraram no armazém""",
                criado_por=admin,
            ).save()

        ops_saida_exists = (
            len(models.TipoOperacao.select().where(models.TipoOperacao.nome == "saida"))
            == 1
        )
        if not ops_saida_exists:
            models.TipoOperacao(
                nome="saída",
                descricao="""Produtos que saíram do armazém""",
                criado_por=admin,
            ).save()

        # Cria alguns tipos de produtos, imagino que seja algo genérico como alimento, eletrônico, etc...
        tipos_produtos_existe = (
            len(
                models.TipoMercadoria.select().where(
                    models.TipoMercadoria.nome == "Grão"
                )
            )
            == 1
        )
        if not tipos_produtos_existe:
            models.TipoMercadoria(nome="Grão", criado_por=admin).save()

        tipo_mercadoria = models.TipoMercadoria.get(
            models.TipoMercadoria.nome == "Grão"
        )

        # Cria e salva alguns produtos
        produtos_existem = (
            len(models.Mercadoria.select().where(models.Mercadoria.nome == "Arroz"))
            == 1
        )

        if not produtos_existem:
            models.Mercadoria(
                nome="Arroz",
                descricao="""
                O arroz é uma planta da família das gramíneas e gênero Oryza, que alimenta mais de metade da população humana do mundo. É a terceira maior cultura cerealífera do mundo, apenas ultrapassada pelas de milho e trigo.
                """.replace(
                    "\n", ""
                ).strip(),
                numero_mercadoria=1234,
                tipo=tipo_mercadoria,
                fabricante=fab,
                criado_por=admin,
            ).save()

    finally:
        Database.get().close()


if __name__ == "__main__":
    db = Database.get()
    create_tables()
    dados_de_teste()
