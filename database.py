import sqlite3

def initialize_db():
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        senha TEXT
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL,
        qto INTEGER,
        codigo TEXT UNIQUE
    )''')
    conn.commit()
    conn.close()

def execute_query(query, params=()):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result
