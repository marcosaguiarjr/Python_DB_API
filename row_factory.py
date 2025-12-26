import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def recuperar_cliente(cursor):  
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchone()


cliente = recuperar_cliente(cursor)

print(dict(cliente))
print(cliente['nome'])

conexao.close()