import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import font
from tkinter import filedialog

# Limpar frames


def limpar_frame():
    if frame_campos.winfo_ismapped():
        frame_campos.pack_forget()

    if frame_cadastro.winfo_ismapped():
        frame_cadastro.pack_forget()

    if frame_Consulta.winfo_ismapped():
        frame_Consulta.pack_forget()

    if frame_tabela.winfo_ismapped():
        frame_tabela.pack_forget()

    if frame_alterar.winfo_ismapped():
        frame_alterar.pack_forget()


def Home():
    limpar_frame()

    frame_campos.pack(fill="both", expand=True, padx=0, pady=0)

    label = tk.Label(frame_campos, text=f"SIP - Sistema de Informação de Projetos",
                     justify="left", anchor="w", font=("Helvetica", 10, "bold"), fg="#000FFF")
    label.grid(row=1, column=0, sticky="w", padx=1, pady=1)

    label = tk.Label(frame_campos, text=f"Versão 1.0",
                     font=("Helvetica", 8, "bold"), fg="#000FFF")
    label.grid(row=2, column=0, sticky="w", padx=1, pady=1)

# Label para exibir a imagem de Capa dentro do frame
    label = tk.Label(frame_campos)

    Imagem = Image.open("Contratos.jpg")
    Imagem = Imagem.resize((300, 200))  # redimensiona se quiser
    Imagem_tk = ImageTk.PhotoImage(Imagem)

    label.grid(row=0, column=0, padx=1, pady=1)
    label.config(image=Imagem_tk)
    label.image = Imagem_tk

    label = tk.Label(frame_campos, text=f"Informações para Usuários:",
                     font=("Helvetica", 9, "bold"), fg="#000FFF", bg="#E4F0EB")
    label.grid(row=1, column=2, sticky="w", padx=1, pady=1)

    texto_longo = (
        "09/04/2025 – O sistema recebeu uma nova facilidade para acessar os projetos por numero da Licitação – acesse o Manual do Usuário")
    label = tk.Label(frame_campos, text=texto_longo,
                     font=("Arial", 9), fg="#000FFF", wraplength=450, bg="#E4F0EB")
    label.grid(row=2, column=2, sticky="w", padx=1, pady=1)

    texto_longo = (
        "06/04/2025 – Foram atualizadas todas as contas de usuários novos no sistema")
    label = tk.Label(frame_campos, text=texto_longo,
                     font=("Arial", 9), fg="#000FFF", wraplength=450, bg="#E4F0EB")
    label.grid(row=3, column=2, sticky="w", padx=1, pady=1)

    texto_longo = (
        "Previsão de sistema fora de uso para manutenção em 04/04/2025 das 23:00 até 24:00")
    label = tk.Label(frame_campos, text=texto_longo,
                     font=("Arial", 9), fg="#000FFF", wraplength=450, bg="#E4F0EB")
    label.grid(row=4, column=2, sticky="w", padx=1, pady=1)


def gravar():
    messagebox.showwarning("Gravar", "Gravação OK")


def verificar_login():
    messagebox.showwarning("Login", "Login OK")


def Logar():
    # Cria uma nova janela (janela de login)
    login_window = tk.Toplevel(janela)
    login_window.title("Login")
    login_window.geometry("300x180+500+200")

    # Usuário
    tk.Label(login_window, text="Usuário:").grid(
        row=0, column=0, padx=10, pady=10, sticky="e")
    entry_usuario = tk.Entry(login_window)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)

    # Senha
    tk.Label(login_window, text="Senha:").grid(
        row=1, column=0, padx=10, pady=10, sticky="e")
    entry_senha = tk.Entry(login_window, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=10)

    # Função de autenticação dentro da janela
    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario == "admin" and senha == "1234":
            login_window.destroy()
            Home()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    # Botão Entrar
    btn_entrar = tk.Button(login_window, text="Entrar",
                           command=autenticar, bg="#000FFF", fg="white", width=15)
    btn_entrar.grid(row=2, column=0, columnspan=2, pady=15)


def consulta():
    limpar_frame()

    frame_Consulta.pack(fill="both", expand=True, padx=0, pady=0)

    IdProjeto = tk.Label(frame_Consulta, text="Id Projeto:", justify="left")
    IdProjeto.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_IdProjeto = tk.Entry(frame_Consulta, width=30)
    entry_IdProjeto.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    NomeProjeto = tk.Label(
        frame_Consulta, text="Nome Projeto:", justify="left")
    NomeProjeto.grid(row=1, column=2, padx=10, pady=10, sticky="e")
    entry_NomeProjeto = tk.Entry(frame_Consulta, width=30)
    entry_NomeProjeto.grid(row=1, column=3, padx=1, pady=0, sticky="w")

    botao3 = tk.Button(frame_Consulta, command=lambda: Mostrar_Tabela(),
                       text="Confirma", font=("Helvetica", 9, "bold"), bg="#000FFF", fg="white", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                       relief="raised")
    botao3.grid(row=10, column=10)


def cadastrar():
    limpar_frame()

    frame_Consulta.pack(fill="both", expand=True, padx=0, pady=0)

    IdProjeto = tk.Label(frame_Consulta, text="Id Projeto:", justify="left")
    IdProjeto.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_IdProjeto = tk.Entry(frame_Consulta, width=30)
    entry_IdProjeto.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    NomeProjeto = tk.Label(
        frame_Consulta, text="Nome Projeto:", justify="left")
    NomeProjeto.grid(row=1, column=2, padx=10, pady=10, sticky="e")
    entry_NomeProjeto = tk.Entry(frame_Consulta, width=30)
    entry_NomeProjeto.grid(row=1, column=3, padx=1, pady=0, sticky="w")

    botao3 = tk.Button(frame_Consulta, command=lambda: altera(entry_IdProjeto.get(), entry_NomeProjeto.get()),
                       text="Confirma", font=("Helvetica", 9, "bold"), bg="#000FFF", fg="white", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                       relief="raised")
    botao3.grid(row=10, column=10)


def altera(valores0, valores1):
    limpar_frame()

    frame_alterar.pack(fill="both", expand=True, padx=0, pady=0)

    C1 = tk.Label(frame_alterar, text="C1", justify="left", bg="#E4F0EB")
    C1.grid(padx=10, pady=10, sticky="w")
    entry_C1 = tk.Entry(frame_alterar, width=30)
    entry_C1.grid(padx=1, pady=0, sticky="ew")

    C2 = tk.Label(frame_alterar, text="C2", justify="left", bg="#E4F0EB")
    C2.grid(padx=10, pady=10, sticky="w")
    entry_C2 = tk.Entry(frame_alterar, width=30)
    entry_C2.grid(padx=1, pady=0, sticky="ew")

    Linha = tk.Label(frame_alterar, text="",
                     justify="left", width=10, bg="#E4F0EB")
    Linha.grid(row=21, column=0, padx=10, pady=10, sticky="w")

    botao3 = tk.Button(frame_alterar, command=lambda: consulta(),
                       text="Salvar", font=("Helvetica", 9, "bold"), bg="#000FFF", fg="white", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                       relief="raised")
    botao3.grid(row=22, column=6)


def selecionar_arquivo(entry_arquivo):
    caminho = filedialog.askopenfilename(title="Selecione um arquivo")
    if caminho:
        entry_arquivo.delete(0, tk.END)
        entry_arquivo.insert(0, caminho)


def Mostrar_Tabela():
    limpar_frame()

    frame_tabela.pack(fill="both", expand=True, padx=1, pady=1)

    # Inserindo dados fictícios
    for i in range(40):
        tabela.insert("", "end", values=(
            f"Pessoa {i}", 20 + i % 10, f"Cidade {i % 5}"))

    # Permitir que a tabela mude com a janela
    frame_tabela.grid_rowconfigure(1, weight=1)
    frame_tabela.grid_columnconfigure(1, weight=1)


def item_escolhido(event):
    limpar_frame()

    selecionado = tabela.focus()
    valores = tabela.item(selecionado, "values")

    altera(valores[0], valores[1])


# Janela principal
# -----------------------------------------------------------------------------------------
janela = tk.Tk()
janela.title("Valueflow         SIP - Sistema de Informação de Projetos")
janela.iconbitmap("RM.ICO")
janela.geometry("1000x600+100+100")

# Barra Menu de cima
# ------------------------------------------------------------------------------------------
barra_menu = tk.Menu(janela)

menu_espaço = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="               ", menu=menu_espaço)

menu_cadastro = tk.Menu(barra_menu, tearoff=0)
menu_cadastro.add_command(label="Consulta", command=consulta)
menu_cadastro.add_command(label="Cadastramento", command=cadastrar)

barra_menu.add_cascade(label="Projeto", menu=menu_cadastro)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Projeto", command=consulta)
barra_menu.add_cascade(label="Consulta", menu=menu_editar)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Dashboard", command=consulta)
menu_editar.add_command(label="Planos Setoriais", command=consulta)
barra_menu.add_cascade(label="Monitoramento", menu=menu_editar)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Indicadores", command=consulta)
barra_menu.add_cascade(label="Indicadores", menu=menu_editar)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Diretorias", command=consulta)
menu_editar.add_command(label="Municípios", command=consulta)
menu_editar.add_command(label="Funções Públicas", command=consulta)
menu_editar.add_command(label="Eixos Temáticos", command=consulta)
menu_editar.add_command(label="Ações dos Eixos Temáticos", command=consulta)
menu_editar.add_command(label="Eixos Setoriais", command=consulta)
barra_menu.add_cascade(label="Cadastros", menu=menu_editar)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Cadastro de Usuários", command=consulta)
menu_editar.add_command(label="Troca de Senha", command=consulta)
menu_editar.add_command(label="Acessos", command=consulta)
menu_editar.add_command(label="Consulta LOG", command=consulta)
barra_menu.add_cascade(label="Controle de Acesso", menu=menu_editar)

menu_espaço = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(
    label="                                                                               ", menu=menu_espaço)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Entrar", command=Logar)
barra_menu.add_cascade(label="Entrar", menu=menu_editar)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Sair", command=janela.quit)
barra_menu.add_cascade(label="Sair", menu=menu_editar, command=janela.quit)

janela.config(menu=barra_menu)

# Frame do menu lateral
# -----------------------------------------------------------------------------------------------
imPesquisa = Image.open("Pesquisa.jpg")  # substitua pelo seu arquivo
imPesquisa = imPesquisa.resize((30, 30))  # redimensiona se quiser
iPesquisa = ImageTk.PhotoImage(imPesquisa)

imagemHome = Image.open("Home.jpg")  # substitua pelo seu arquivo
imagemHome = imagemHome.resize((30, 30))  # redimensiona se quiser
iconeHome = ImageTk.PhotoImage(imagemHome)

imagemEntrar = Image.open("Entrar.jpg")  # substitua pelo seu arquivo
imagemEntrar = imagemEntrar.resize((30, 30))  # redimensiona se quiser
iconeEntrar = ImageTk.PhotoImage(imagemEntrar)

imagemDashboard = Image.open("Dashboard.jpg")  # substitua pelo seu arquivo
imagemDashboard = imagemDashboard.resize((30, 30))  # redimensiona se quiser
iconeDashboard = ImageTk.PhotoImage(imagemDashboard)

imagemSair = Image.open("Sair.jpg")  # substitua pelo seu arquivo
imagemSair = imagemSair.resize((30, 30))  # redimensiona se quiser
iconeSair = ImageTk.PhotoImage(imagemSair)

menu_lateral = tk.Frame(janela, bg="#A6CAEC", width=50)
menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)

botao = tk.Button(menu_lateral, image=iconeHome,
                  command=Home, bg="white", text="Home")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(menu_lateral, image=iconeEntrar,
                  command=Logar, bg="white", text="Entrar")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(menu_lateral, image=iPesquisa,
                  command=consulta, bg="white", text="Consulta")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(menu_lateral, image=iconeDashboard,
                  command=consulta, bg="white", text="Dashboard")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(menu_lateral, image=iconeSair,
                  command=janela.quit, bg="white", text="Sair")
botao.pack(side="top", pady=20)  # Pode usar: side="left", "right", "bottom"

# Área principal
# ---------------------------------------------------------------------------------------------
frame_principal = tk.Frame(janela, bg="#E4F0EB", width=100, height=100)
frame_principal.pack(side="right", fill="both", expand=True)

# Frames
# ---------------------------------------------------------------------------------------------
frame_cadastro = tk.Frame(
    frame_principal, bg="lightgray", width=300, height=100)

frame_campos = tk.Frame(frame_principal, height=1, bg="#E4F0EB")
frame_Consulta = tk.Frame(frame_principal, height=1, bg="#E4F0EB")
frame_tabela = tk.Frame(frame_principal, height=1, bg="#E4F0EB")
frame_alterar = tk.Frame(frame_principal, height=1, bg="#E4F0EB")

# Tabela para mostrar dados
# -------------------------------------------------------------------------------------------
# Criando um estilo para a Treeview
style = ttk.Style()
style.theme_use("default")

# Mudando a cor de fundo e outras cores
style.configure("Treeview",
                background="#E4F0EB",
                foreground="black",
                rowheight=20,
                fieldbackground="#f0f0f0")

# Cor do item selecionado (opcional)
style.map("Treeview", background=[('selected', '#3399ff')])

frame_tabela.grid_columnconfigure(0, weight=1)

# Scrollbar vertical
scrollbar = tk.Scrollbar(frame_tabela)
scrollbar.grid(row=0, column=2, sticky="ns")

# Tabela (Treeview)
tabela = ttk.Treeview(frame_tabela, columns=("SEI", "Nome", "Diretoria", "Municipio", "Natureza", "Entrada", "Fase"),
                      show="headings", yscrollcommand=scrollbar.set, height=20)
tabela.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)

scrollbar.config(command=tabela.yview)

# Cabeçalhos
tabela.heading("SEI", text="SEI")
tabela.heading("Nome", text="Nome")
tabela.heading("Diretoria", text="Diretoria")
tabela.heading("Municipio", text="Município")
tabela.heading("Natureza", text="Natureza")
tabela.heading("Entrada", text="Entrada")
tabela.heading("Fase", text="Fase")

tabela.column("SEI", width=150)
tabela.column("Nome", width=150)
tabela.column("Diretoria", width=100)
tabela.column("Municipio", width=100)
tabela.column("Natureza", width=80)
tabela.column("Entrada", width=50)
tabela.column("Fase", width=10)

tabela.bind("<<TreeviewSelect>>", item_escolhido)

# Iniciando a interface
janela.mainloop()
