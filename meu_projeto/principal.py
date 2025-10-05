# -------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import font

from projeto import cadastrar
from home import home

# Janela principal
# -----------------------------------------------------------------------------------------
janela = tk.Tk()
janela.title("Valueflow         SIP - TESTE DE FRAMES")
janela.geometry("900x500")

# Barra Menu de cima
# ------------------------------------------------------------------------------------------
barra_menu = tk.Menu(janela)

menu_espaço = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="               ", menu=menu_espaço)

# Frame do menu lateral
# -----------------------------------------------------------------------------------------------
frame_lateral = tk.Frame(janela, bg="#A6CAEC", width=50)
frame_lateral.pack(side="left", fill="y")
frame_lateral.pack_propagate(False)

botao = tk.Button(frame_lateral, command=lambda: home(
    frame_principal), bg="white", text="Home")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(frame_lateral, command=lambda: cadastrar(
    frame_principal), bg="white", text="Cadastrar")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(frame_lateral, command=janela.quit, bg="white", text="Sair")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

# Frame principal
# ---------------------------------------------------------------------------------------------
frame_principal = tk.Frame(janela, bg="#E4F0EB", width=100, height=100)
frame_principal.pack(side="right", fill="both", expand=True)

home(frame_principal)

# Iniciando a interface
janela.mainloop()
