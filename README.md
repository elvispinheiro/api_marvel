# Marvel API

Este projeto tem como objetivo coletar dados da API pública da Marvel e armazená-los em um banco de dados SQLite e em arquivos CSV. Os dados coletados incluem personagens, quadrinhos, criadores, eventos e histórias da Marvel.

## Funcionalidades

- Conecta à API pública da Marvel para buscar dados sobre:
  - Personagens
  - Quadrinhos
  - Criadores
  - Eventos
  - Histórias
- Armazena os dados coletados em um banco de dados SQLite (`marvel_data.db`).
- Armazena os dados coletados em arquivos CSV separados por tipo de dado (exemplo: `marvel_data_characters.csv`).
- Permite a consulta e visualização dos dados diretamente no banco de dados ou nos arquivos CSV.

## Requisitos

Antes de rodar o projeto, certifique-se de que você tem as seguintes dependências instaladas:

- Python 3.x
- Bibliotecas:
  - `requests`
  - `pandas`
  - `python-dotenv`

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

## Configuração

Crie um arquivo .env com suas chaves da API da Marvel:

- PUBLIC_KEY=your_public_key_here
- PRIVATE_KEY=your_private_key_here

## Como Executar 

- Clone o repositório e execute o script.

- Estrutura de Arquivos:

- marvel_data_collector.py: Script principal.
- .env: Arquivo para armazenar suas chaves de API.
- marvel_data.db: Banco de dados SQLite.
- marvel_data_{type_name}.csv: Arquivos CSV com dados coletados.

## Contribuição 

- Fork o repositório.
- Crie uma nova branch (git checkout -b minha-contribuicao).
- Envie um pull request.

## Licença 

- Este projeto está licenciado sob a Licença MIT.

```bash
pip install requests pandas python-dotenv
