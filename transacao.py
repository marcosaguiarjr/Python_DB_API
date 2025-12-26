import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Digite o ID do cliente que deseja consultar: ")
cursor.execute('SELECT * FROM clientes WHERE id = ?;', (id_cliente,))
clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', ("Ana Paula", "ana.paula@uol.com"))
    conexao.commit()
except Exception as e:
    conexao.rollback()
    print(f"Erro ao inserir cliente: {e}")
finally:
    conexao.close()