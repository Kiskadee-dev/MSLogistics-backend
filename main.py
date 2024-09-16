from flask import Flask, request, jsonify
from os import getenv
from dotenv import load_dotenv
import views.mercadoria as mercadoria
import views.usuario as usuario
import views.generic as generic
import views.entradas_saidas as entradas_e_saidas
import views.fabricantes as fabricantes
import views.tipos as tipos
from database import Database
from peewee import IntegrityError

load_dotenv()

app = Flask(__name__)

@app.before_request
def before_request():
    Database.get().connect()

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
    "/mercadoria/<int:pk>", view_func=mercadoria.mercadoria_read, methods=["GET"]
)
app.add_url_rule(
    "/mercadoria/<int:pk>",
    view_func=mercadoria.mercadoria_update,
    methods=["PATCH"],
)
app.add_url_rule(
    "/mercadoria/<int:pk>",
    view_func=mercadoria.mercadoria_delete,
    methods=["DELETE"],
)

# Usuario, não há funcionalidade para registro de novos, R
app.add_url_rule("/usuario/", view_func=usuario.usuario_get_list, methods=["GET"])

# Fabricante, CRUD
app.add_url_rule(
    "/fabricante/", view_func=fabricantes.fabricante_get_list, methods=["GET"]
)

# Tipos de operações, R
app.add_url_rule(
    "/operacao/tipos/", view_func=tipos.tipos_get_list, methods=["GET"]
)

# Entradas e saídas, CRUD
app.add_url_rule(
    "/operacao/",
    view_func=entradas_e_saidas.entradas_e_saidas_get_list,
    methods=["GET"],
)


if __name__ == "__main__":
    app.run(debug=getenv("debug") is not None)
