import tkinter as tk
from tkinter import messagebox
from database import autenticar_usuario, inserir_usuario
from util import limpar_janela
from menu import mostrar_menu_principal

def mostrar_login(app):
    limpar_janela(app.root)
    tk.Label(app.root, text="Login", font=("Arial", 16)).pack(pady=10)

    tk.Label(app.root, text="Email:").pack()
    email_entry = tk.Entry(app.root)
    email_entry.pack()

    tk.Label(app.root, text="Senha:").pack()
    senha_entry = tk.Entry(app.root, show="*")
    senha_entry.pack()

    def fazer_login():
        email = email_entry.get()
        senha = senha_entry.get()
        usuario = autenticar_usuario(email, senha)
        if usuario:
            app.usuario_logado = usuario
            mostrar_menu_principal(app)
        else:
            messagebox.showerror("Erro", "Usuário não cadastrado.")

    tk.Button(app.root, text="Entrar", command=fazer_login).pack(pady=5)
    tk.Button(app.root, text="Cadastrar-se", command=lambda: mostrar_cadastro(app)).pack()

def mostrar_cadastro(app):
    limpar_janela(app.root)
    tk.Label(app.root, text="Cadastro de Usuário", font=("Arial", 16)).pack(pady=10)

    labels = ["Nome", "Email", "Senha"]
    entradas = {}

    for label in labels:
        tk.Label(app.root, text=label + ":").pack()
        entrada = tk.Entry(app.root, show="*" if label == "Senha" else None)
        entrada.pack()
        entradas[label] = entrada

    def cadastrar():
        try:
            nome = entradas["Nome"].get()
            email = entradas["Email"].get()
            senha = entradas["Senha"].get()
            inserir_usuario(nome, email, senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            mostrar_login(app)
        except:
            messagebox.showerror("Erro", "Email já cadastrado ou erro inesperado.")

    tk.Button(app.root, text="Cadastrar", command=cadastrar).pack(pady=5)
    tk.Button(app.root, text="Voltar", command=lambda: mostrar_login(app)).pack()
