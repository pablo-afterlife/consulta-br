"""CLI não oficial para a BrasilAPI."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("consulta-br")
except PackageNotFoundError:  # rodando direto do source, sem instalar
    __version__ = "0.0.0"
