from models import Mercadoria
from typing import Any, Optional


def mercadoria(form: dict[str, Any]) -> Mercadoria:
    mercadoria = Mercadoria(
        nome=form.get("nome"),
        fabricante=form.get("fabricante"),
        tipo=form.get("tipo"),
        descricao=form.get("descricao"),
        criado_por=form.get("criado_por"),
        numero_registro=form.get("numero_registro"),
    )
    return mercadoria
