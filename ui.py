import tkinter as tk
from tkinter import messagebox, ttk
from user import cadastrar, fazer_login
from product import insert_produto, mostrar_produtos, atualizar_produto, deletar_produto
import os

def tela_de_login():
    root = tk.Tk()
    root.title("Tela de Login")
    root.geometry("300x200")

    tk.Label(root, text="Email").pack()
    entry_email = tk.Entry(root)
    entry_email.pack()

    tk.Label(root, text="Senha").pack()
    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    tk.Button(root, text="Cadastrar", command=lambda: messagebox.showinfo("Info", cadastrar(entry_email.get(), entry_senha.get()))).pack(pady=5)
    tk.Button(root, text="Fazer Login", command=lambda: fazer_login_handler(entry_email.get(), entry_senha.get())).pack(pady=5)

    root.mainloop()

def fazer_login_handler(email, senha):
    if fazer_login(email, senha):
        menuPrincipal()
    else:
        messagebox.showerror("Erro", "Email ou senha incorretos.")

def menuPrincipal():
    root = tk.Tk()
    root.title("Tela Principal")
    root.geometry("400x600")

    tk.Button(root, text="Cadastrar Produto", command=tela_de_cadastro).pack(pady=10)
    tk.Button(root, text="Atualizar Produto", command=tela_de_update).pack(pady=10)
    tk.Button(root, text="Mostrar Produtos", command=tela_de_mostrar).pack(pady=10)
    tk.Button(root, text="Deletar Produto", command=tela_de_deletar).pack(pady=10)
    tk.Button(root, text="Gerar Relatório", command=gerar_relatorio).pack(pady=10)

    root.mainloop()

def tela_de_cadastro():
    root = tk.Tk()
    root.title("Tela de Cadastro de Produto")
    root.geometry("300x300")

    tk.Label(root, text="Nome do Produto").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    tk.Label(root, text="Preço do Produto").pack()
    entry_preco = tk.Entry(root)
    entry_preco.pack()

    tk.Label(root, text="Quantidade no Estoque").pack()
    entry_qto = tk.Entry(root)
    entry_qto.pack()

    tk.Label(root, text="Código de Barras").pack()
    entry_codigo = tk.Entry(root)
    entry_codigo.pack()

    tk.Button(root, text="Cadastrar", command=lambda: insert_produto(entry_nome.get(), float(entry_preco.get()), int(entry_qto.get()), entry_codigo.get())).pack(pady=10)

    root.mainloop()

def tela_de_update():
    root = tk.Tk()
    root.title("Tela de Atualização de Produto")
    root.geometry("300x300")

    tk.Label(root, text="Código do Produto").pack()
    entry_codigo = tk.Entry(root)
    entry_codigo.pack()

    tk.Label(root, text="Novo Nome").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    tk.Label(root, text="Novo Preço").pack()
    entry_preco = tk.Entry(root)
    entry_preco.pack()

    tk.Label(root, text="Nova Quantidade").pack()
    entry_qto = tk.Entry(root)
    entry_qto.pack()

    tk.Button(root, text="Atualizar", command=lambda: atualizar_produto(entry_codigo.get(), entry_nome.get(), float(entry_preco.get()), int(entry_qto.get()))).pack(pady=10)

    root.mainloop()

def tela_de_deletar():
    root = tk.Tk()
    root.title("Tela de Deletar Produto")
    root.geometry("300x200")

    tk.Label(root, text="Código do Produto").pack()
    entry_codigo = tk.Entry(root)
    entry_codigo.pack()

    tk.Button(root, text="Deletar", command=lambda: deletar_produto(entry_codigo.get())).pack(pady=10)

    root.mainloop()

def tela_de_mostrar():
    root = tk.Tk()
    root.title("Mostrar Produtos")
    root.geometry("400x400")

    tv = ttk.Treeview(root, columns=('nome', 'preco', 'qtd', 'codigo'), show='headings')
    for col in tv['columns']:
        tv.heading(col, text=col.upper())
        tv.column(col, minwidth=0, width=100)
    tv.pack()

    for linha in mostrar_produtos():
        tv.insert("", tk.END, values=linha)

    root.mainloop()

def gerar_relatorio():
    caminho_principal = os.path.dirname(os.path.abspath(__file__))
    caminho_relatorio = os.path.join(caminho_principal, "relatorio.txt")

    produtos = mostrar_produtos()

    with open(caminho_relatorio, "w") as arquivo:
        arquivo.write("Relatório de Produtos\n")
        arquivo.write("=====================\n")
        for produto in produtos:
            nome, preco, quantidade, codigo = produto
            arquivo.write(f"Produto: {nome}\n")
            arquivo.write(f"Preço: R${preco:.2f}\n")
            arquivo.write(f"Quantidade: {quantidade}\n")
            arquivo.write(f"Código de Barras: {codigo}\n")
            arquivo.write("---------------------\n")
    
    messagebox.showinfo("Sucesso", "Relatório gerado com sucesso em relatorio.txt!")
    print(f"Relatório gerado com sucesso em: {caminho_relatorio}")


tela_de_login()
