import sqlite3

def inicializar_banco():
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT UNIQUE,
        senha TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        descricao TEXT,
        preco REAL,
        quantidade INTEGER)''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, senha):
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
    conn.commit()
    conn.close()

def autenticar_usuario(email, senha):
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    user = c.fetchone()
    conn.close()
    return user

def inserir_produto(nome, descricao, preco, quantidade):
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute("INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
              (nome, descricao, preco, quantidade))
    conn.commit()
    conn.close()

def atualizar_produto(id_produto, nome, descricao, preco, quantidade):
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute("""
        UPDATE produtos
        SET nome = ?, descricao = ?, preco = ?, quantidade = ?
        WHERE id = ?
    """, (nome, descricao, preco, quantidade, id_produto))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute("SELECT * FROM produtos")
    produtos = c.fetchall()
    conn.close()
    return produtos

def excluir_produto(produto_id):
    conn = sqlite3.connect('nobre.db')
    c = conn.cursor()
    c.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conn.commit()
    conn.close()