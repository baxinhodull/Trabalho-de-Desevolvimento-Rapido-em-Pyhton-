import sqlite3
from database import execute_query, fetch_query

def cadastrar(email, senha):
    if '@yahoo.com' in email or '@gmail.com' in email:
        if len(senha) >= 6:
            try:
                execute_query("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
                return "Cadastro realizado com sucesso!"
            except sqlite3.IntegrityError:
                return "Email já cadastrado."
        else:
            return "Senha muito curta."
    else:
        return "Email inválido."

def fazer_login(email, senha):
    resultado = fetch_query("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    return resultado is not None
