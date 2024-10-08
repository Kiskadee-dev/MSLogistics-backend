from os import getenv

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from peewee import IntegrityError

import views.entradas_saidas as entradas_e_saidas
import views.fabricantes as fabricantes
import views.generic as generic
import views.mercadoria as mercadoria
import views.tipo_operacao as tipo_operacao
import views.tipos_mercadoria as tipos_mercadoria
import views.usuario as usuario
from database import Database
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)
cors = CORS(app)


@app.before_request
def before_request():
    Database.get().connect(reuse_if_open=True)


@app.after_request
def after_request(response):
    Database.get().close()
    return response


@app.errorhandler(IntegrityError)
def handle_bad_request(e):
    app.logger.error(e)
    return jsonify({"msg": "Bad request", "error": f"{str(e)}"}), 400


app.add_url_rule("/", view_func=generic.index)

# Mercadoria, CRUD
app.add_url_rule("/mercadoria/", view_func=mercadoria.mercadoria_get_list)
app.add_url_rule(
    "/mercadoria", view_func=mercadoria.mercadoria_create, methods=["POST"]
)
app.add_url_rule(
    "/mercadoria/<int:id>", view_func=mercadoria.mercadoria_read, methods=["GET"]
)
app.add_url_rule(
    "/mercadoria/<int:id>",
    view_func=mercadoria.mercadoria_update,
    methods=["PATCH"],
)
app.add_url_rule(
    "/mercadoria/<int:id>",
    view_func=mercadoria.mercadoria_delete,
    methods=["DELETE"],
)

# Usuario, não há funcionalidade para registro de novos, R
app.add_url_rule("/usuario/", view_func=usuario.usuario_get_list, methods=["GET"])

# Fabricante, CRUD
app.add_url_rule(
    "/fabricante/", view_func=fabricantes.fabricante_get_list, methods=["GET"]
)
app.add_url_rule(
    "/fabricante", view_func=fabricantes.fabricante_create, methods=["POST"]
)
app.add_url_rule(
    "/fabricante/<int:id>", view_func=fabricantes.fabricante_read, methods=["GET"]
)
app.add_url_rule(
    "/fabricante/<int:id>", view_func=fabricantes.fabricante_update, methods=["PATCH"]
)
app.add_url_rule(
    "/fabricante/<int:id>", view_func=fabricantes.fabricante_delete, methods=["POST"]
)

# Tipos de operações, R
app.add_url_rule(
    "/operacao/tipos/", view_func=tipo_operacao.tipos_get_list, methods=["GET"]
)

# Entradas e saídas, CRUD
app.add_url_rule(
    "/operacao/",
    view_func=entradas_e_saidas.entradas_e_saidas_get_list,
    methods=["GET"],
)
app.add_url_rule(
    "/operacao",
    view_func=entradas_e_saidas.entradas_e_saidas_create,
    methods=["POST"],
)
app.add_url_rule(
    "/operacao/<int:id>",
    view_func=entradas_e_saidas.entradas_e_saidas_read,
    methods=["GET"],
)
app.add_url_rule(
    "/operacao/<int:id>",
    view_func=entradas_e_saidas.entradas_e_saidas_update,
    methods=["PATCH"],
)
app.add_url_rule(
    "/operacao/<int:id>",
    view_func=entradas_e_saidas.entradas_e_saidas_delete,
    methods=["DELETE"],
)

# Tipos de mercadorias, CRUD
app.add_url_rule(
    "/mercadoria/tipos/",
    view_func=tipos_mercadoria.tipos_mercadoria_get_list,
    methods=["GET"],
)
app.add_url_rule(
    "/mercadoria/tipos",
    view_func=tipos_mercadoria.tipos_mercadoria_create,
    methods=["POST"],
)
app.add_url_rule(
    "/mercadoria/tipos/<int:id>",
    view_func=tipos_mercadoria.tipos_mercadoria_read,
    methods=["GET"],
)
app.add_url_rule(
    "/mercadoria/tipos/<int:id>",
    view_func=tipos_mercadoria.tipos_mercadoria_update,
    methods=["PATCH"],
)
app.add_url_rule(
    "/mercadoria/tipos/<int:id>",
    view_func=tipos_mercadoria.tipos_mercadoria_delete,
    methods=["DELETE"],
)


if __name__ == "__main__":
    app.run(debug=getenv("debug") is not None)
