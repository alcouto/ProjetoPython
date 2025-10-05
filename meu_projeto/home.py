import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import font


def home(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()

    frame_campos = tk.Frame(frame_principal, height=1, bg="#E4F0EB")
    frame_campos.pack(fill="both", expand=True, padx=0, pady=0)

    Imagem = Image.open("imagens/contratos.jpg")
    Imagem = Imagem.resize((250, 80))
    ImagemIRM_tk = ImageTk.PhotoImage(Imagem)

    labelIRM = tk.Label(frame_campos)
    labelIRM.grid(row=0, column=0, padx=220, pady=20, sticky="e")
    labelIRM.config(image=ImagemIRM_tk)
    labelIRM.image = ImagemIRM_tk

    label = tk.Label(frame_campos, text=f"Teste no laboratório",
                     justify="left", anchor="w", font=("Helvetica", 10, "bold"), fg="#000FFF")
    label.grid(row=2, column=0, sticky="w", padx=1, pady=1)

    label = tk.Label(frame_campos, text=f"Versão 1.0",
                     font=("Helvetica", 8, "bold"), fg="#000FFF")
    label.grid(row=3, column=0, sticky="w", padx=1, pady=1)
