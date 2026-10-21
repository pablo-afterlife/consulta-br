"""Camada HTTP: fala com a BrasilAPI e devolve os dados já decodificados.

Regra da casa: nada aqui imprime. Quem decide o que mostrar na tela é o cli.py.
"""

from typing import Any

import httpx

BASE_URL = "https://brasilapi.com.br/api"
TIMEOUT_SEGUNDOS = 10.0


def buscar_cep(cep: str) -> dict[str, Any]:
    """Busca o endereço de um CEP (só dígitos, 8 caracteres)."""
    resposta = httpx.get(f"{BASE_URL}/cep/v2/{cep}", timeout=TIMEOUT_SEGUNDOS)
    resposta.raise_for_status()
    return resposta.json()
