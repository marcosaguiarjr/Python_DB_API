import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                   'nome VARCHAR(100), '
                   'email VARCHAR(150) UNIQUE NOT NULL)')


def inserir_registro(conexao, cursor, dados):
    cursor.execute('INSERT OR IGNORE INTO clientes (nome, email) VALUES (?, ?)', dados)
    conexao.commit()

def inserir_multi_registro(conexao, cursor, dados):
    cursor.executemany('INSERT OR IGNORE INTO clientes (nome, email) VALUES (?, ?)', dados)
    conexao.commit()

def atualizar_registro(conexao, cursor, dados):
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', dados)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    cursor.execute('DELETE FROM clientes WHERE id = ?;', (id,))
    conexao.commit()

data = ("Maria Silva", "maria.silva@uol.com", 2)
data2 = [
    ("João Souza", "joao.souza@uol.com"),
    ("Carlos Oliveira", "carlos.oliveira@uol.com")
]

#inserir_multi_registro(conexao, cursor, data2)

#atualizar_registro(conexao, cursor, data)

#excluir_registro(conexao, cursor, 1)


def consultar_registros(cursor):
    cursor.execute('SELECT * FROM clientes;')
    for linha in cursor.fetchall():
        print(dict(linha))

def consultar_registro_por_id(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?;', (id,))
    print(dict(cursor.fetchone()))

consultar_registro_por_id(cursor, 2)
consultar_registros(cursor)
conexao.close()