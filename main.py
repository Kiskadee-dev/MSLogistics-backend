from flask import Flask, request, jsonify
from os import getenv
from dotenv import load_dotenv
import views.mercadoria as mercadoria
import views.usuario as usuario
import views.generic as generic
from database import Database

load_dotenv()

app = Flask(__name__)


@app.before_request
def before_request():
    Database.get().connect()


@app.after_request
def after_request(response):
    Database.get().close()
    return response


app.add_url_rule("/", view_func=generic.index)
app.add_url_rule("/mercadoria/", view_func=mercadoria.get_list)
app.add_url_rule("/mercadoria", view_func=mercadoria.create, methods=["POST"])
app.add_url_rule("/mercadoria/<int:pk>", view_func=mercadoria.read, methods=["GET"])
app.add_url_rule("/mercadoria/<int:pk>", view_func=mercadoria.update, methods=["PATCH"])
app.add_url_rule(
    "/mercadoria/<int:pk>", view_func=mercadoria.delete, methods=["DELETE"]
)

app.add_url_rule("/usuario/", view_func=usuario.get_list, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=getenv("debug") is not None)
