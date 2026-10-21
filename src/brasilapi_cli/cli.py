import re
from typing import Annotated

import typer

from brasilapi_cli import __version__, api

app = typer.Typer(
    help="Consulta CEP, CNPJ e feriados na BrasilAPI.",
    no_args_is_help=True,
    invoke_without_command=True,
)


@app.callback()
def main(
    version: bool = typer.Option(
        False, "--version", "-V", help="Mostra a versão e sai.", is_eager=True
    ),
) -> None:
    if version:
        typer.echo(f"brasilapi-cli {__version__}")
        raise typer.Exit()


def _apenas_digitos(valor: str) -> str:
    """01001-000, 01.001-000 e ' 01001000 ' viram 01001000."""
    return re.sub(r"\D", "", valor)


@app.command()
def cep(
    cep: Annotated[str, typer.Argument(help="CEP de 8 dígitos, com ou sem máscara.")],
) -> None:
    """Consulta o endereço de um CEP."""
    numero = _apenas_digitos(cep)
    if len(numero) != 8:
        typer.echo(f"CEP invalido: {cep!r} (esperado 8 digitos)", err=True)
        raise typer.Exit(1)

    dados = api.buscar_cep(numero)

    endereco = ", ".join(
        parte
        for parte in (dados.get("street"), dados.get("neighborhood"), dados.get("city"))
        if parte
    )
    uf = dados.get("state") or "?"
    typer.echo(f"{endereco} - {uf}" if endereco else f"Endereco nao informado - {uf}")
    typer.echo(f"CEP: {dados.get('cep', numero)}")
