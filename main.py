from flask import Flask, request, jsonify
from os import getenv
from dotenv import load_dotenv
import views
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

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/mercadoria/", view_func=views.get_list)
app.add_url_rule("/mercadoria", view_func=views.create, methods=["POST"])
app.add_url_rule("/mercadoria/<int:pk>", view_func=views.read, methods=["GET"])
app.add_url_rule("/mercadoria/<int:pk>", view_func=views.update, methods=["PATCH"])
app.add_url_rule("/mercadoria/<int:pk>", view_func=views.delete, methods=["DELETE"])


if __name__ == "__main__":
    app.run(debug=getenv("debug") is not None)
