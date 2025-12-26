# Explorando Banco de Dados Relacionais com Python DB API

Este repositório contém um projeto prático desenvolvido como parte do curso **"Explorando Banco de Dados Relacionais com Python DB API"** da [DIO](https://www.dio.me/). O objetivo é demonstrar como interagir com bancos de dados relacionais utilizando a biblioteca nativa `sqlite3` do Python, seguindo as especificações da Python DB API.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal.
- **SQLite3**: Banco de dados relacional leve e integrado ao Python.
- **Pathlib**: Para manipulação inteligente de caminhos de arquivos no sistema.

## 📁 Estrutura do Projeto

O projeto é dividido em scripts que abordam diferentes conceitos de manipulação de dados:

| Arquivo | Descrição | Conceito Chave |
| :--- | :--- | :--- |
| `conexao.py` | Implementação de operações CRUD completas. | `execute`, `executemany`, `commit`. |
| `transacao.py` | Exemplo de gerenciamento de atomicidade. | `rollback`, `try/except/finally`. |
| `row_factory.py` | Customização da forma como os dados são retornados. | `sqlite3.Row` (Dicionários). |
| `clientes.db` | Arquivo de banco de dados gerado automaticamente. | Persistência local. |

## 🛠️ Funcionalidades Demonstradas

### 1. Operações CRUD
No arquivo `conexao.py`, você encontrará funções para:
- **Criar Tabelas**: Uso de `CREATE TABLE IF NOT EXISTS`.
- **Inserir Registros**: Inserção simples e múltipla (`executemany`).
- **Atualizar e Excluir**: Manipulação de registros existentes via ID.
- **Consultar**: Recuperação de dados com filtros e listagem total.

### 2. Segurança e Boas Práticas
- **Placeholders**: Uso de `?` nas queries SQL para prevenir ataques de **SQL Injection**.
- **Pathlib**: Localização dinâmica do arquivo `.db` baseada no diretório do script, evitando erros de "arquivo não encontrado".

### 3. Gestão de Transações
O script `transacao.py` foca na integridade dos dados. Ele simula uma operação onde, caso ocorra um erro (como uma violação de chave primária), o sistema executa um `rollback`, garantindo que o banco não fique em um estado inconsistente.

### 4. Row Factory
Com o `cursor.row_factory = sqlite3.Row`, transformamos as tuplas de retorno em objetos que se comportam como dicionários. Isso permite acessar os dados pelo nome da coluna:
```python
print(cliente['nome']) # Em vez de cliente[1]
