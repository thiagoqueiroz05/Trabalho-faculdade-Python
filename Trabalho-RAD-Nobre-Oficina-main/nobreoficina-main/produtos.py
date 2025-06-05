import tkinter as tk
import logging
from datetime import datetime 
from tkinter import messagebox
from database import inserir_produto, listar_produtos, excluir_produto

logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def mostrar_cadastro_produto(app):
    janela = tk.Toplevel(app.root)
    janela.title("Cadastrar Produto")
    janela.geometry("300x250")

    labels = ["Nome", "Descrição", "Preço", "Quantidade"]
    entradas = {}

    for label in labels:
        tk.Label(janela, text=label + ":").pack()
        entrada = tk.Entry(janela)
        entrada.pack()
        entradas[label] = entrada

    def salvar():
        try:
            nome = entradas["Nome"].get()
            descricao = entradas["Descrição"].get()
            preco = float(entradas["Preço"].get())
            quantidade = int(entradas["Quantidade"].get())
            inserir_produto(nome, descricao, preco, quantidade)
            logging.info(f"CRIADO por {app.usuario_logado[1]}: Produto '{nome}'")
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            janela.destroy()
        except:
            messagebox.showerror("Erro", "Verifique os dados inseridos.")

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)

def mostrar_lista_produtos(app):
    import logging

    janela = tk.Toplevel(app.root)
    janela.title("Produtos Cadastrados")
    janela.geometry("400x300")

    produtos = listar_produtos()

    lista = tk.Listbox(janela, width=50)
    lista.pack()

    for prod in produtos:
        texto = f"{prod[0]}. {prod[1]} - {prod[2]} - R${prod[3]:.2f} (x{prod[4]})"
        lista.insert(tk.END, texto)

    def excluir():
        selecao = lista.curselection()
        if selecao:
            id_produto = produtos[selecao[0]][0]
            nome_produto = produtos[selecao[0]][1]

            logging.info(f"EXCLUIDO por {app.usuario_logado[1]}: Produto '{nome_produto}'")

            confirmar = messagebox.askyesno(
                "Confirmar Exclusão",
                f"Tem certeza que deseja excluir o produto '{nome_produto}'?"
            )

            if confirmar:
                excluir_produto(id_produto)
                messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
                janela.destroy()
                mostrar_lista_produtos(app)
        else:
            messagebox.showwarning("Atenção!", "Selecione um produto para excluir.")

    def editar():
        selecao = lista.curselection()
        if selecao:
            id_produto = produtos[selecao[0]][0]
            nome = produtos[selecao[0]][1]
            descricao = produtos[selecao[0]][2]
            preco = produtos[selecao[0]][3]
            quantidade = produtos[selecao[0]][4]

            janela_editar = tk.Toplevel(app.root)
            janela_editar.title("Editar Produto")
            janela_editar.geometry("300x250")

            labels = ["Nome", "Descrição", "Preço", "Quantidade"]
            entradas = {}

            for label in labels:
                tk.Label(janela_editar, text=label + ":").pack()
                entrada = tk.Entry(janela_editar)
                entrada.pack()
                entradas[label] = entrada

            entradas["Nome"].insert(0, nome)
            entradas["Descrição"].insert(0, descricao)
            entradas["Preço"].insert(0, str(preco))
            entradas["Quantidade"].insert(0, str(quantidade))

            def salvar_edicao():
                try:
                    novo_nome = entradas["Nome"].get()
                    nova_descricao = entradas["Descrição"].get()
                    novo_preco = float(entradas["Preço"].get())
                    nova_quantidade = int(entradas["Quantidade"].get())

                    from database import atualizar_produto
                    atualizar_produto(id_produto, novo_nome, nova_descricao, novo_preco, nova_quantidade)
                    messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
                    janela_editar.destroy()
                    janela.destroy()
                    mostrar_lista_produtos(app)
                except:
                    messagebox.showerror("Erro", "Verifique os dados inseridos.")

            tk.Button(janela_editar, text="Salvar Alterações", command=salvar_edicao).pack(pady=10)
        else:
            messagebox.showwarning("Atenção!", "Selecione um produto para editar.")

    tk.Button(janela, text="Excluir Selecionado", command=excluir).pack(pady=5)
    tk.Button(janela, text="Editar Selecionado", command=editar).pack(pady=5)

