import main
from models import *
from database import Database
import pytest
from manage import dados_de_teste
import json

MODELS = [Usuario, Mercadoria, Fabricante, TipoMercadoria, Operacao]
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

# Testar as views...
# Usuário
def test_usuario(client):
    response = client.get("/usuario/")
    data = json.loads(response.data)
    assert len(data) > 0, "Has data"