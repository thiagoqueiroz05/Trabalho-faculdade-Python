def limpar_janela(janela):
    for widget in janela.winfo_children():
        widget.destroy()
