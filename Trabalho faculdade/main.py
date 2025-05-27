import tkinter as tk
from tkinter import messagebox, simpledialog
from database import *

class NobreOficinaApp:
    def __init__(self):
        inicializar_banco()
        self.usuario_logado = None

        self.root = tk.Tk()
        self.root.title("Nobre Oficina")
        self.root.geometry("400x300")

        self.mostrar_login()
        self.root.mainloop()

    def mostrar_login(self):
        self.limpar_janela()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="Senha:").pack()
        senha_entry = tk.Entry(self.root, show="*")
        senha_entry.pack()

        def fazer_login():
            email = email_entry.get()
            senha = senha_entry.get()
            usuario = autenticar_usuario(email, senha)
            if usuario:
                self.usuario_logado = usuario
                self.mostrar_menu_principal()
            else:
                messagebox.showerror("Erro", "Credenciais inválidas.")

        tk.Button(self.root, text="Entrar", command=fazer_login).pack(pady=5)
        tk.Button(self.root, text="Cadastrar-se", command=self.mostrar_cadastro).pack()

    def mostrar_cadastro(self):
        self.limpar_janela()
        tk.Label(self.root, text="Cadastro", font=("Arial", 16)).pack(pady=10)

        labels = ["Nome", "Email", "Senha"]
        entradas = {}

        for label in labels:
            tk.Label(self.root, text=label + ":").pack()
            entrada = tk.Entry(self.root, show="*" if label == "Senha" else None)
            entrada.pack()
            entradas[label] = entrada

        def cadastrar():
            nome = entradas["Nome"].get()
            email = entradas["Email"].get()
            senha = entradas["Senha"].get()
            try:
                inserir_usuario(nome, email, senha)
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                self.mostrar_login()
            except:
                messagebox.showerror("Erro", "Email já cadastrado ou erro inesperado.")

        tk.Button(self.root, text="Cadastrar", command=cadastrar).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.mostrar_login).pack()

    def mostrar_menu_principal(self):
        self.limpar_janela()
        tk.Label(self.root, text=f"Bem-vindo(a), {self.usuario_logado[1]}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Cadastrar Produto", command=self.mostrar_cadastro_produto).pack(pady=5)
        tk.Button(self.root, text="Listar Produtos", command=self.mostrar_lista_produtos).pack(pady=5)
        tk.Button(self.root, text="Gerar Relatório", command=self.gerar_relatorio).pack(pady=5)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(pady=10)

    def mostrar_cadastro_produto(self):
        self.limpar_janela()
        tk.Label(self.root, text="Novo Produto", font=("Arial", 14)).pack(pady=10)

        labels = ["Nome", "Descrição", "Preço", "Quantidade"]
        entradas = {}
        for label in labels:
            tk.Label(self.root, text=label + ":").pack()
            entrada = tk.Entry(self.root)
            entrada.pack()
            entradas[label] = entrada

        def salvar():
            try:
                nome = entradas["Nome"].get()
                descricao = entradas["Descrição"].get()
                preco = float(entradas["Preço"].get())
                quantidade = int(entradas["Quantidade"].get())
                inserir_produto(nome, descricao, preco, quantidade)
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                self.mostrar_menu_principal()
            except:
                messagebox.showerror("Erro", "Verifique os dados inseridos.")

        tk.Button(self.root, text="Salvar", command=salvar).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.mostrar_menu_principal).pack()

    def mostrar_lista_produtos(self):
        self.limpar_janela()
        tk.Label(self.root, text="Produtos", font=("Arial", 14)).pack(pady=10)

        lista = tk.Listbox(self.root, width=50)
        lista.pack()

        produtos = listar_produtos()
        for prod in produtos:
            texto = f"{prod[0]}. {prod[1]} - {prod[2]} - R${prod[3]:.2f} (x{prod[4]})"
            lista.insert(tk.END, texto)

        def excluir():
            selecao = lista.curselection()
            if selecao:
                id_produto = produtos[selecao[0]][0]
                excluir_produto(id_produto)
                messagebox.showinfo("Excluído", "Produto removido com sucesso.")
                self.mostrar_lista_produtos()

        tk.Button(self.root, text="Excluir Selecionado", command=excluir).pack(pady=5)
        tk.Button(self.root, text="Voltar", command=self.mostrar_menu_principal).pack()

    def gerar_relatorio(self):
        produtos = listar_produtos()
        total = sum([p[3] * p[4] for p in produtos])
        messagebox.showinfo("Relatório", f"Produtos cadastrados: {len(produtos)}\nValor total em estoque: R$ {total:.2f}")

    def limpar_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    NobreOficinaApp()