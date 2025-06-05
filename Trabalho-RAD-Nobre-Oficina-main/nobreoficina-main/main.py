import tkinter as tk
from database import inicializar_banco
from auth import mostrar_login

class NobreOficinaApp:
    def __init__(self):
        inicializar_banco()
        self.root = tk.Tk()
        self.root.title("Nobre Oficina")
        self.root.geometry("500x400")
        self.root.config(bg="white")

        self.usuario_logado = None
        mostrar_login(self)  # Chama a tela de login
        self.root.mainloop()

if __name__ == "__main__":
    NobreOficinaApp()
