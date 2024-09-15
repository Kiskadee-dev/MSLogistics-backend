import models
from database import Database
from os import getenv
from dotenv import load_dotenv


def create_tables():
    """Applies the schema to the db"""

    db = Database.get()
    with db:
        db.create_tables([models.Usuario, models.Mercadoria, models.EntradaESaida])


def dados_de_teste():
    load_dotenv()
    Database.get().connect()
    try:
        # Cria e insere admin
        admin = models.Usuario(
            nome=getenv("ADMIN_USER", "Admin"),
            senha=getenv("ADMIN_PASSWORD", "Admin"),
            email=getenv("ADMIN_EMAIL", "Admin@Admin.com"),
        )
        admin.save()

        # Cria um fabricante
        fab = models.Fabricante(
            nome="AgricultorXYZ", descricao="""Produtor de grãos""", criado_por=admin
        )
        fab.save()

        # Cria tipos de operações de entrada e saída
        models.Operacao(
            nome="entrada",
            descricao="""Produtos que entraram no armazém""",
            criado_por=admin,
        ).save()
        models.Operacao(
            nome="saida",
            descricao="""Produtos que saíram do armazém""",
            criado_por=admin,
        ).save()

        # Cria e salva alguns produtos
        models.Mercadoria(
            nome="Arroz",
            descricao="""
            O arroz é uma planta da família das gramíneas e gênero Oryza, que alimenta mais de metade da população humana do mundo. É a terceira maior cultura cerealífera do mundo, apenas ultrapassada pelas de milho e trigo.
            """.replace(
                "\n", ""
            ).strip(),
            criado_por=admin,
        ).save()

        models.Mercadoria(
            nome="Feijão",
            descricao="""
            Proporciona nutrientes essenciais como proteínas, ferro, cálcio, vitaminas (principalmente do complexo B), carboidratos e fibras. 
            """.replace(
                "\n", ""
            ).strip(),
            criado_por=admin,
        ).save()

    finally:
        Database.get().close()


if __name__ == "__main__":
    create_tables()
    dados_de_teste()
