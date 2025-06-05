import tkinter as tk
from tkinter import messagebox
from util import limpar_janela
from produtos import mostrar_cadastro_produto, mostrar_lista_produtos

def mostrar_menu_principal(app):
    limpar_janela(app.root)

    menubar = tk.Menu(app.root)

    menu_arquivo = tk.Menu(menubar, tearoff=0)
    menu_arquivo.add_command(label="Sair", command=app.root.quit)
    menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

    menu_registro = tk.Menu(menubar, tearoff=0)
    menu_registro.add_command(label="Cadastrar Produto", command=lambda: mostrar_cadastro_produto(app))
    menu_registro.add_command(label="Listar Produtos", command=lambda: mostrar_lista_produtos(app))
    menubar.add_cascade(label="Produtos", menu=menu_registro)

    menu_relatorio = tk.Menu(menubar, tearoff=0)
    menu_relatorio.add_command(label="Gerar Relatório", command=lambda: gerar_relatorio(app))
    menubar.add_cascade(label="Relatório", menu=menu_relatorio)

    menu_ajuda = tk.Menu(menubar, tearoff=0)
    menu_ajuda.add_command(label="Sobre", command=sobre)
    menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

    app.root.config(menu=menubar)
    tk.Label(app.root, text=f"Bem-vindo(a) à Nobre Oficina", font=("Arial", 14)).pack(pady=20)

def gerar_relatorio(app):
    from database import listar_produtos
    produtos = listar_produtos()
    total = sum([p[3] * p[4] for p in produtos])
    messagebox.showinfo("Relatório", f"Produtos cadastrados: {len(produtos)}\nValor total em estoque: R$ {total:.2f}")

def sobre():
    messagebox.showinfo("Sobre", "Sistema de Cadastro - Nobre Oficina\nDesenvolvido em Python com Tkinter e banco de dados.")
