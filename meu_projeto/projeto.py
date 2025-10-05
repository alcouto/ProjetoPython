import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import font

from home import home
from dbconfig import get_connection, insert_projeto
from dbtabelas import DB_projeto


def cadastrar(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    frame_cadastro = tk.Frame(
        frame_principal, bg="lightgray", width=300, height=100)

    tk.Label(frame_cadastro, text="Id Projeto novo:").grid(
        row=1, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(frame_cadastro)
    entry_nome.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_cadastro, text="Nome Projeto:").grid(
        row=2, column=0, padx=5, pady=5)
    entry_NomeProjeto = tk.Entry(frame_cadastro, width=30)
    entry_NomeProjeto.grid(row=2, column=1, padx=30, pady=30)

    # Criando o botão para submeter
    botao = tk.Button(frame_cadastro, text="Gravar",
                      command=lambda: gravar_projeto())
    botao.grid(row=5, column=10, padx=30, pady=30)

    botao = tk.Button(frame_cadastro, text="Voltar",
                      command=lambda: home(frame_principal))
    botao.grid(row=5, column=12, padx=30, pady=30)

    frame_cadastro.pack(fill="both", expand=True, padx=0, pady=0)

    def gravar_projeto():
        DB_projeto.DB_idprojeto = entry_nome.get()
        insert_projeto()
