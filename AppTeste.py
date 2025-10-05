# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk
# import os
# import sys
# import subprocess

import pyodbc
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import font
from tkinter import filedialog
from tkcalendar import DateEntry

import os
import platform
import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import numpy as np

import yagmail

MAX_ARQUIVOS = 10
# lista com dicionários: {"caminho":..., "tipo":..., "comentario":...}
arquivos = []

TIPOS_ARQUIVO = ["Texto", "Imagem", "Planilha", "PDF", "Outro"]


def Anexos():
    Anexos_window = tk.Toplevel(janela, bg="#E4F0EB")
    Anexos_window.title("Anexos do Projeto")
    Anexos_window.geometry("1000x400+200+200")

    # Anexos_window.attributes("-topmost", True)
    # Anexos_window.lift()

    Anexo1 = tk.Label(Anexos_window, text="Anexos",
                      justify="left", width=20, bg="#E4F0EB")
    Anexo1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    frame_lista = tk.Frame(Anexos_window, borderwidth=2,
                           relief="ridge", padx=5, pady=15, bg="#E4F0EB")
    frame_lista.grid(row=1, column=0, padx=5, pady=15,
                     columnspan=8, sticky="w")
    frame_lista.grid_propagate(False)
    frame_lista.config(width=950, height=300)

    atualizar_lista(frame_lista)

# ------------------------------------------------------------------------------------------
    quadroB = tk.Frame(Anexos_window, borderwidth=2,
                       relief="ridge", padx=5, pady=15, bg="#A6CAEC")
    quadroB.grid(row=10, column=0, padx=5, pady=15, columnspan=8, sticky="w")
    quadroB.grid_propagate(False)
    quadroB.config(width=950, height=50)

    botao3 = tk.Button(quadroB, command=lambda: selecionar_arquivo(frame_lista),
                       text="Adicionar", font=("Helvetica", 7, "bold"), bg="#67958d", fg="black", activebackground="#45a049", activeforeground="white", padx=5, pady=5, borderwidth=2,
                       relief="raised", width=20)
    botao3.grid(row=0, column=0, sticky="w", padx=5, pady=1)

    botao3 = tk.Button(quadroB, command=lambda: Anexos_window.destroy(),
                       text="Salvar", font=("Helvetica", 7, "bold"), bg="#67958d", fg="black", activebackground="#45a049", activeforeground="white", padx=5, pady=5, borderwidth=2,
                       relief="raised", width=20)
    botao3.grid(row=0, column=1, sticky="w", padx=5, pady=1)

    botao3 = tk.Button(quadroB, command=lambda: Anexos_window.destroy(),
                       text="Voltar", font=("Helvetica", 7, "bold"), bg="#67958d", fg="black", activebackground="#45a049", activeforeground="white", padx=5, pady=5, borderwidth=2,
                       relief="raised", width=20)
    botao3.grid(row=0, column=2, sticky="w", padx=5, pady=1)


def selecionar_arquivo(frame_lista):
    if len(arquivos) >= MAX_ARQUIVOS:
        messagebox.showwarning(
            "Limite atingido", f"Você só pode adicionar até {MAX_ARQUIVOS} arquivos.")
        return

    caminho = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=(("Todos os arquivos", "*.*"),
                   ("Arquivos de texto", "*.txt"))
    )
    if caminho:
        arquivos.append({"caminho": caminho, "tipo": tk.StringVar(
            value=TIPOS_ARQUIVO[0]), "comentario": tk.StringVar()})
        atualizar_lista(frame_lista)


def abrir_arquivo(caminho):
    if caminho and os.path.exists(caminho):
        try:
            if sys.platform.startswith("win"):  # Windows
                os.startfile(caminho)
            elif sys.platform.startswith("darwin"):  # macOS
                subprocess.call(["open", caminho])
            else:  # Linux
                subprocess.call(["xdg-open", caminho])
        except Exception as e:
            messagebox.showerror(
                "Erro", f"Não foi possível abrir o arquivo.\n{e}")
    else:
        messagebox.showwarning("Aviso", "Arquivo não encontrado.")


def excluir_arquivo(index):
    if 0 <= index < len(arquivos):
        arquivos.pop(index)
        atualizar_lista()


def atualizar_lista(frame_lista):
    # Frame que vai conter a lista
    # frame_lista.pack(pady=10)

    # Limpa o frame antes de recriar os widgets
    for widget in frame_lista.winfo_children():
        widget.destroy()

    for i, arq in enumerate(arquivos):
        # Caminho do arquivo
        entrada = tk.Entry(frame_lista, width=40)
        entrada.insert(0, arq["caminho"])
        entrada.grid(row=i, column=0, padx=5, pady=3)

        # Botão Abrir
        btn_abrir = tk.Button(frame_lista, text="Abrir",
                              command=lambda c=arq["caminho"]: abrir_arquivo(c))
        btn_abrir.grid(row=i, column=1, padx=5, pady=3)

        # Botão Excluir
        btn_excluir = tk.Button(
            frame_lista, text="Excluir", command=lambda idx=i: excluir_arquivo(idx))
        btn_excluir.grid(row=i, column=2, padx=5, pady=3)

        # Combobox para tipo
        combo_tipo = ttk.Combobox(
            frame_lista, textvariable=arq["tipo"], values=TIPOS_ARQUIVO, state="readonly", width=12)
        combo_tipo.grid(row=i, column=3, padx=5, pady=3)

        # Comentário
        comentario = tk.Entry(
            frame_lista, textvariable=arq["comentario"], width=25)
        comentario.grid(row=i, column=4, padx=5, pady=3)


# ===========================================================================================================
# Criar janela
# janela = tk.Tk()
# janela.title("Gerenciador de Arquivos")
# janela.geometry("950x400")

janela = tk.Tk()
janela.title("SIGP - Sistema de Informações de Gerência de Projetos")
janela.iconbitmap("RM.ICO")
janela.geometry("1125x600+5+5")


btn_anexos = tk.Button(janela, text="Anexos", command=Anexos)
btn_anexos.pack(pady=10)

# Inicia a interface
janela.mainloop()
