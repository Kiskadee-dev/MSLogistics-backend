import main
from models import *
from database import Database
import pytest
from manage import dados_de_teste
import json

MODELS = [Usuario, Mercadoria, Fabricante, TipoMercadoria, TipoOperacao]
db = Database.get(testing=True)


@pytest.fixture
def setup_db():
    db.bind(MODELS, bind_refs=False, bind_backrefs=False)
    db.connect()
    db.create_tables(MODELS)
    dados_de_teste(testing=True)
    yield db

    db.drop_tables(MODELS)
    db.close()


@pytest.fixture
def app():
    app = main.app
    app.config.update({"TESTING": True})

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_usuario_presente():
    assert len(Usuario.select()) > 0, "Usuário foi inserido com sucesso"


def test_mercadoria_presente():
    assert len(Mercadoria.select()) > 0, "Existem mercadorias"


## Pelo tempo não será possível fazer TDD..
# TODO: Testar as views...
# Usuário
def test_usuario(client):
    response = client.get("/usuario/")
    data = json.loads(response.data)
    assert len(data) > 0, "Possui dados"
    assert data[0]["nome"] == "Admin", "Usuário 0 é o admin"


def test_tipos_operacoes(client):
    response = client.get("/operacao/tipos/")
    data = json.loads(response.data)
    assert len(data) > 1
    assert data[0]["nome"] == "entrada"
    assert data[1]["nome"] == "saída"
