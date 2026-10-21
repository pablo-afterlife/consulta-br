# consulta-br

> Consulte CEP, CNPJ e feriados nacionais direto do terminal, usando a [BrasilAPI](https://brasilapi.com.br).

<!-- Descomente o badge de CI quando chegar na v0.3 -->
<!-- [![CI](https://github.com/pablo-afterlife/consulta-br/actions/workflows/ci.yml/badge.svg)](https://github.com/pablo-afterlife/consulta-br/actions/workflows/ci.yml) -->
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

```console
$ consulta-br cep 01001-000
Praça da Sé, Sé, São Paulo - SP
CEP: 01001000
```

<!-- Quando a v0.6 estiver pronta, grave um GIF (ex.: com o "vhs" ou "asciinema") e coloque aqui:
![Demonstração](docs/demo.gif)
-->

## Por que este projeto?

Às vezes você só quer saber o endereço de um CEP, conferir os dados de uma empresa ou descobrir quando é o próximo feriado, sem abrir o navegador. O `consulta-br` resolve isso com um comando. A opção `--json`, prevista para a v0.6, vai permitir usar a saída em scripts e automações.

## Funcionalidades

| Comando | O que faz | Status |
|---|---|---|
| `cep <cep>` | Endereço completo a partir do CEP | ✅ pronto (v0.1) |
| `cnpj <cnpj>` | Razão social, situação cadastral e endereço da empresa | 📋 planejado (v0.4) |
| `feriados <ano>` | Lista os feriados nacionais do ano | 📋 planejado (v0.5) |
| `feriados --proximo` | Mostra o próximo feriado | 📋 planejado (v0.5) |
| `--json` | Saída em JSON, para usar com `jq` e scripts | 📋 planejado (v0.6) |

## Instalação

> Por enquanto a instalação é a partir do código-fonte. A publicação no PyPI (`pip install consulta-br`) está prevista para a v1.0.

Requisitos: **Python 3.12 ou superior**, **Git** e **[uv](https://docs.astral.sh/uv/)**.

```bash
git clone https://github.com/pablo-afterlife/consulta-br.git
cd consulta-br
uv sync
uv run consulta-br cep 01001000
```

`uv sync` cria o `.venv` com a versão de Python pedida pelo projeto, instala as dependências e já deixa o comando `consulta-br` disponível dentro do ambiente.

Se você preferir não usar `uv`, dá para instalar com `pip` em modo de desenvolvimento — mas aí as ferramentas de teste e lint não vêm junto, porque elas ficam no grupo `dev` (PEP 735), que o `pip` não lê:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1      # Windows (PowerShell)
source .venv/bin/activate        # Linux / macOS
pip install -e .
```

## Como usar

```bash
# Consultar um CEP (com ou sem máscara)
consulta-br cep 01001000
consulta-br cep 01001-000

# Ajuda
consulta-br --help

# Versão
consulta-br --version
```

Os comandos `cnpj`, `feriados` e a opção `--json` aparecem no [roadmap](#roadmap) e ainda não existem.

## Limitações conhecidas (v0.1.0)

- **Só o caminho feliz.** CEP inexistente (`00000000`) ou falha de rede ainda imprimem o traceback do Python em vez de uma mensagem decente → corrigido na v0.2.
- Sem testes automatizados nem CI → v0.3.
- Saída em texto simples, sem Rich nem `--json` → v0.6.

## Desenvolvimento

Tecnologias usadas:

- [Typer](https://typer.tiangolo.com) para a interface de linha de comando
- [httpx](https://www.python-httpx.org) para as requisições HTTP
- [Rich](https://rich.readthedocs.io) para a formatação no terminal (a partir da v0.6)
- [pytest](https://docs.pytest.org) + [respx](https://lundberg.github.io/respx/) para os testes, com a API simulada (a partir da v0.3)
- [ruff](https://docs.astral.sh/ruff/) como linter e formatador

Organização do pacote:

```
src/consulta_br/
├── __init__.py   # versão, lida do pyproject.toml
├── __main__.py   # permite `python -m consulta_br`
├── cli.py        # Typer: argumentos, mensagens e exit codes
└── api.py        # httpx: só HTTP e JSON, sem nenhum print
```

`api.py` não imprime nada de propósito: a camada de rede pode ser testada sem passar pelo terminal, e a saída pode mudar (Rich, `--json`) sem tocar na chamada HTTP.

Comandos úteis:

```bash
uv run pytest           # testes (a partir da v0.3)
uv run ruff check .     # aponta problemas no código
uv run ruff format .    # formata o código
```

Os testes **não** chamam a BrasilAPI de verdade: as respostas são simuladas com o `respx`. Assim os testes ficam rápidos, funcionam sem internet e não sobrecarregam uma API gratuita.

## Roadmap

- [x] **v0.1**: estrutura do projeto e comando `cep` básico
- [ ] **v0.2**: tratamento de erros (CEP inválido ou inexistente, sem internet, timeout)
- [ ] **v0.3**: testes automatizados e CI com GitHub Actions
- [ ] **v0.4**: comando `cnpj` com validação dos dígitos verificadores
- [ ] **v0.5**: comando `feriados` e opção `--proximo`
- [ ] **v0.6**: saída formatada com Rich e opção `--json`
- [ ] **v0.7**: cache local para os feriados
- [ ] **v1.0**: publicação no PyPI e documentação completa

Ideias para depois da v1.0: consulta de DDD, lista de bancos e código FIPE. Sugestões são bem-vindas nas [issues](https://github.com/pablo-afterlife/consulta-br/issues).

## Contribuindo

Contribuições são muito bem-vindas, principalmente de quem está fazendo a primeira contribuição open source.

1. Veja as [issues abertas](https://github.com/pablo-afterlife/consulta-br/issues). As marcadas com `good first issue` são um bom começo.
2. Comente na issue que quer trabalhar nela.
3. Faça um fork, crie uma branch (`git checkout -b feat/minha-feature`) e faça commits seguindo o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/) (`feat:`, `fix:`, `docs:`, `test:`).
4. Garanta que `uv run pytest` e `uv run ruff check .` passam.
5. Abra um Pull Request descrevendo o que mudou e por quê.

<!-- Quando criar o arquivo CONTRIBUTING.md (v1.0), troque esta seção por um link para ele. -->

## Uso responsável da API

A BrasilAPI é gratuita e mantida pela comunidade. Este projeto:

- faz no máximo uma requisição por comando;
- guarda em cache os dados que mudam pouco, como os feriados (a partir da v0.7);
- nunca chama a API nos testes automatizados.

Se você usar o `consulta-br` em scripts, evite laços com muitas consultas seguidas.

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE).

## Agradecimentos

- À [BrasilAPI](https://github.com/BrasilAPI/BrasilAPI) e à comunidade que a mantém.

---

Feito por [Pablo Vinicius](https://github.com/pablo-afterlife).
