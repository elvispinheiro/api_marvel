import os
from dotenv import load_dotenv
import requests
import hashlib
import time
import sqlite3
import pandas as pd


load_dotenv()

PUBLIC_KEY = os.getenv("PUBLIC_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# URL base da API da Marvel
BASE_URL = "http://gateway.marvel.com/v1/public"

# Conectar ao banco de dados
conn = sqlite3.connect('marvel_data.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS marvel_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    name TEXT,
    description TEXT
)
''')
conn.commit()

# Função dados da API da Marvel
def get_marvel_data(endpoint, params=None):
    if params is None:
        params = {}

    # Timestamp gera o hash
    ts = str(time.time())
    to_hash = ts + PRIVATE_KEY + PUBLIC_KEY
    hash_md5 = hashlib.md5(to_hash.encode()).hexdigest()

    # Adicionar parâmetros
    params.update({
        'ts': ts,
        'apikey': PUBLIC_KEY,
        'hash': hash_md5,
    })

    # Requisição
    response = requests.get(f"{BASE_URL}/{endpoint}", params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar o endpoint {endpoint}: {response.status_code}")
        print(response.json())
        return None

# Função para salvar dados no banco
def save_to_db(data, type_name):
    for item in data:
        name = item.get('name', item.get('title', 'Sem Nome'))
        description = item.get('description', 'Nenhuma descrição disponível.')

        cursor.execute('''
        INSERT INTO marvel_data (type, name, description)
        VALUES (?, ?, ?)
        ''', (type_name, name, description))
    conn.commit()

# Função para salvar dados em um arquivo CSV
def save_to_csv(data, type_name):
    # Criar um DataFrame com os dados
    df = pd.DataFrame(data, columns=['name', 'description'])
    
    # Adicionar uma coluna para o tipo de dado
    df['type'] = type_name

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(f"marvel_data_{type_name}.csv", index=False, mode='a', header=not pd.io.common.file_exists(f"marvel_data_{type_name}.csv"))
    print(f"Dados de {type_name} salvos em marvel_data_{type_name}.csv")

# Função para exibir e salvar no banco de dados e CSV
def fetch_and_display(endpoint, limit=10):
    data = get_marvel_data(endpoint, {"limit": limit})
    if data:
        results = data['data']['results']
        print(f"\nResultados do endpoint: {endpoint}\n")
        
        # Salvar dados no banco de dados
        save_to_db(results, endpoint)
        
        # Salvar dados em um arquivo CSV
        save_to_csv(results, endpoint)
        
        for item in results:
            print(f"Nome: {item.get('name', item.get('title', 'Sem Nome'))}")
            print(f"Descrição: {item.get('description', 'Nenhuma descrição disponível.')}")
            print("-" * 50)

if __name__ == "__main__":
    print("Buscando...\n")

    # personagens
    fetch_and_display("characters", limit=5)

    # quadrinhos
    fetch_and_display("comics", limit=5)

    # criadores
    fetch_and_display("creators", limit=5)

    # eventos
    fetch_and_display("events", limit=5)

    # histórias
    fetch_and_display("stories", limit=5)

    
    conn.close()
