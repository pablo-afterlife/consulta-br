# brasilapi-cli

CLI não oficial para consultar **CEP**, **CNPJ** e **feriados nacionais** na
[BrasilAPI](https://brasilapi.com.br) — direto do terminal, sem abrir navegador.

> Status: **v0.1.0** — apenas o comando `cep`. Veja o [roadmap](#roadmap).

## Instalação

Ainda não publicado no PyPI (isso é a v1.0). Por enquanto, direto do código:

```bash
git clone https://github.com/pablo-afterlife/brasilapi-cli.git
cd brasilapi-cli
uv sync
```

Requisitos: Python 3.12+ e [uv](https://docs.astral.sh/uv/).

## Uso

```console
$ brasilapi cep 01001-000
Praça da Sé, Sé, São Paulo - SP
CEP: 01001000
```

O CEP pode vir com máscara, com pontos ou sem nada — `01001-000`, `01.001-000`
e `01001000` são a mesma entrada.

```console
$ brasilapi --help
$ brasilapi --version
```

## Limitações conhecidas (v0.1.0)

- **Só o caminho feliz.** CEP inexistente ou falha de rede ainda imprime o
  traceback do Python em vez de uma mensagem decente → tratado na v0.2.
- Sem testes automatizados nem CI → v0.3.
- Saída em texto simples, sem `--json` nem tabelas → v0.6.

## Roadmap

| Versão | Entrega |
| --- | --- |
| v0.1 | Setup do pacote + comando `cep` |
| v0.2 | Tratamento de erros (CEP inválido, 404, rede, timeout) |
| v0.3 | Testes com pytest + respx, CI no GitHub Actions |
| v0.4 | Comando `cnpj` |
| v0.5 | Comando `feriados` |
| v0.6 | Saída com Rich + `--json` |
| v0.7 | Cache local |
| v1.0 | Publicação no PyPI + documentação completa |

## Licença

MIT — veja [LICENSE](LICENSE).

Dados fornecidos pela [BrasilAPI](https://brasilapi.com.br) (projeto público e
gratuito). Esta CLI não tem vínculo com os mantenedores da API.
