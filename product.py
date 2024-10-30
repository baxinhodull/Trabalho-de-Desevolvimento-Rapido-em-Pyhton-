from database import execute_query, fetch_query

def insert_produto(nome, preco, qto, codigo):
    execute_query("INSERT INTO produtos (nome, preco, qto, codigo) VALUES (?, ?, ?, ?)",
                  (nome, preco, qto, codigo))

def mostrar_produtos():
    return fetch_query("SELECT * FROM produtos")

def atualizar_produto(codigo, novo_nome, novo_preco, nova_qto):
    execute_query("UPDATE produtos SET nome = ?, preco = ?, qto = ? WHERE codigo = ?",
                  (novo_nome, novo_preco, nova_qto, codigo))

def deletar_produto(codigo):
    execute_query("DELETE FROM produtos WHERE codigo = ?", (codigo,))

def gerar_relatorio():
    produtos = mostrar_produtos()
    with open("relatorio.txt", "w") as file:
        for produto in produtos:
            file.write(f"Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}, Código: {produto[4]}\n")
