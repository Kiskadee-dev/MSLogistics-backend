from datetime import datetime

import bcrypt
from peewee import (
    CharField,
    Check,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    TextField,
)

from database import Database


class BaseModel(Model):
    class Meta:
        database = Database.get()


class Usuario(BaseModel):
    nome = CharField(max_length=256)
    email = CharField(
        max_length=256,
        unique=True,
    )
    senha = CharField(max_length=256)  # salted and hashed with bcrypt

    def save(self, *args, **kwargs):
        if not "@" in self.email:
            # TODO: Use regex to properly validate
            raise ValueError("Invalid email address")

        if not self.senha.startswith("$2b$"):
            self.senha = bcrypt.hashpw(
                f"{self.senha}".encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")

        return super().save(*args, **kwargs)


class Fabricante(BaseModel):
    nome = CharField(unique=True)
    descricao = TextField()
    criado_em = DateTimeField(default=datetime.now)
    criado_por = ForeignKeyField(
        Usuario, backref="fabricantes_usuario", on_delete=["CASCADE"]
    )


class TipoMercadoria(BaseModel):
    nome = CharField(max_length=256, unique=True)
    criado_em = DateTimeField(default=datetime.now)
    criado_por = ForeignKeyField(
        Usuario, backref="tipos_mercadoria_usuario", on_delete=["CASCADE"]
    )


class Mercadoria(BaseModel):
    nome = CharField(max_length=256)
    numero_registro = IntegerField(unique=True, null=None)
    fabricante = ForeignKeyField(
        Fabricante, backref="mercadorias_fabricante", on_delete=["CASCADE"]
    )
    tipo = ForeignKeyField(
        TipoMercadoria, backref="mercadorias_tipo", on_delete=["CASCADE"]
    )
    descricao = TextField()
    criado_em = DateTimeField(default=datetime.now)
    criado_por = ForeignKeyField(
        Usuario, backref="mercadorias_usuario", on_delete=["CASCADE"]
    )


class TipoOperacao(BaseModel):
    nome = CharField(max_length=10, unique=True)
    descricao = TextField()
    criado_em = DateTimeField(default=datetime.now)
    criado_por = ForeignKeyField(
        Usuario, backref="operacao_usuario", on_delete=["CASCADE"]
    )


class EntradaESaida(BaseModel):
    mercadoria = ForeignKeyField(
        Mercadoria, backref="entrada_saida_mercadoria", on_delete=["CASCADE"]
    )
    quantia = IntegerField(Check("quantia > 0"))
    tipo_operacao = ForeignKeyField(
        TipoOperacao, backref="entrada_saida_operacao", on_delete=["CASCADE"]
    )
    data_e_hora = DateTimeField()
    local = CharField(max_length=256)
    criado_em = DateTimeField(default=datetime.now)
    criado_por = ForeignKeyField(
        Usuario, backref="entrada_saida_usuario", on_delete=["CASCADE"]
    )

    def __str__(self):
        return (
            f"Mercadoria: {self.mercadoria.nome}, Operação: {self.tipo_operacao.nome}"
        )
