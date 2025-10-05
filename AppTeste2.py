import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import subprocess

# Projeto, Licitacao, Contrato, Arquivo, Tipo, Area, Comentario


class DBAnexos:
    Linha = []


class DBUsuarios:
    Linha = []


class DBListaAnexos:
    DBTipoAnexos = ["Aditivo contratuais a processos de aprovação por autoridade competente",
                    "Aditivo contratual",
                    "Adjudicação da licitação em formato PDF",
                    "Análise Técnica das Propostas Recebidas",
                    "Anotação de Responsabilidade Técnica (ART)",
                    "Ata de Reunião do Conselho Deliberativo",
                    "Auditoria interna relacionados ao cumprimento dos indicadores",
                    "Autorização da Autoridade Competente",
                    "Comprovação da inclusão do projeto do Plano de Contratações Anual (PCA)",
                    "Comprovação de pagamento efetuado",
                    "Comprovante de execução de ações corretivas recomendadas pelas auditorias",
                    "Comprovante de publicação",
                    "Contrato Assinado",
                    "Contrato e documentos relacionados à conformidade com a Lei nº 14.133/2021",
                    "Cumprimento de metas",
                    "Declaração de conformidade emitidas pelos órgãos fiscalizadores",
                    "Documentação fotográfica ou vídeo das fiscalizações realizadas",
                    "Documento comprobatório das cotações (Termo de Referência e Planilha para ser Preenchida)",
                    "Documento comprobatório para auditoria (notas fiscais, contratos, etc.)",
                    "Documentos que comprove a realização de ajustes e correções nos indicadores",
                    "Documento que comprove o Cumprimento de Metas",
                    "Encerramento contratual e liberação de garantias",
                    "Extrato do Contrato",
                    "Extrato do Contrato Publicado e Comissao de Fiscalização Publicado",
                    "Justificativa detalhadas para casos de não conformidade",
                    "Justificativa em casos de não conformidade",
                    "Laudo técnico relacionado à fiscalização do projeto",
                    "Orçamento Estimativo",
                    "Parecer de auditoria e relatórios financeiros detalhados",
                    "Parecer técnico e relatório de conformidade",
                    "Parecer técnico sobre a análise de propostas",
                    "Propostas Recebidas",
                    "Prorrogação do contrato",
                    "Questionamento ou recurso apresentado pelas licitantes",
                    "Realização de ajustes e correções nos indicadores",
                    "Relatório de auditoria interna relacionado ao cumprimento dos indicadores",
                    "Relatório de Conformidade",
                    "Relatório de fiscalização e cumprimento de cláusulas contratuais",
                    "Relatório de fiscalização",
                    "Outros"]


def limpar_frame():
    if frame_cadastro_usuario.winfo_ismapped():
        frame_cadastro_usuario.pack_forget()
    if frame_tabela_Usuario.winfo_ismapped():
        frame_tabela_Usuario.pack_forget()


def ordenar(treeview, coluna, reverso):
    # messagebox.showwarning("Ordenar", "ordenar")

    # Pega todos os itens da tabela
    itens = [(treeview.set(k, coluna), k) for k in treeview.get_children('')]

    # Ordena (por padrão string, mas dá para converter para int/float se precisar)
    itens.sort(reverse=reverso)

    # Rearranja as linhas na ordem certa
    for index, (val, k) in enumerate(itens):
        treeview.move(k, '', index)

    # Alterna o sentido da ordenação (crescente/decrescente)
    treeview.heading(coluna, command=lambda: ordenar(
        treeview, coluna, not reverso))

# ======================================================================================================


def Preenche_tabela_Usuario():
    DBUsuarios.Linha = []
    DBUsuarios.Linha.append({"Nome": "Usuario Um", "EMail": "usuarioum@teste.com,br",
                             "Telefone": "+55219998877", "Diretoria": "Dir A", "Setor": "Setor A"})
    DBUsuarios.Linha.append({"Nome": "Usuario Dois", "EMail": "usuariodois@teste.com,br",
                             "Telefone": "+55216660077", "Diretoria": "Dir B", "Setor": "Setor B"})

    tabela_Usuario.delete(*tabela_Usuario.get_children())

    # Reinsere todos
    # for arq in arquivos:
    for arq in DBUsuarios.Linha:
        tabela_Usuario.insert("", "end", values=(
            arq["Nome"], arq["EMail"], arq["Telefone"], arq["Diretoria"], arq["Setor"]))


def usuario_escolhido(Event):
    limpar_frame()

    janela.title(
        "Valueflow         SIGP - Sistema de Informações de Gerência de Projetos         - Cadastro de Usuarios")

    frame_cadastro_usuario.pack(fill="both", expand=True, padx=0, pady=0)


def Usuarios():
    limpar_frame()

    frame_cadastro_usuario.pack_forget()

    frame_tabela_Usuario.pack(fill="both", expand=True, padx=1, pady=1)

    Preenche_tabela_Usuario()

    # Permitir que a tabela mude com a janela
    frame_tabela_Usuario.grid_rowconfigure(1, weight=1)
    frame_tabela_Usuario.grid_columnconfigure(1, weight=1)

# ======================================================================================================


def Anexos(Area):
    MAX_ARQUIVOS = 30

    arquivos = []

    Anexos_window = tk.Toplevel(janela, bg="#E4F0EB")
    Anexos_window.title("Anexos - " + Area)
    Anexos_window.geometry("1020x400+200+200")

    def leitura_anexos():
        DBAnexos.Linha = []

        if Area == "Projeto":
            DBAnexos.Linha.append({"Projeto": "0001", "Licitacao": "0001-01", "Contrato": "000101", "caminho": "G:/Drives compartilhados/valueflow/Clientes e Parceiros/SIGP/SIP - Sistema de Informação de Projetos V3.pptx",
                                   "tipo": "Anotação de Responsabilidade Técnica (ART)", "area": "Contrato", "comentario": "Anotações do dia 01"})
            DBAnexos.Linha.append({"Projeto": "0001", "Licitacao": "0001-02", "Contrato": "000201", "caminho": "G:/Drives compartilhados/valueflow/Clientes e Parceiros/SIGP/SIP - Sistema de Informação de Projetos V3.pptx",
                                   "tipo": "Ata de Reunião do Conselho Deliberativo", "area": "Contrato", "comentario": "Aqrquivo de ata de reunião"})
        if Area == "Licitacao":
            DBAnexos.Linha.append({"Projeto": "0001", "Licitacao": "0001-01", "Contrato": "000101", "caminho": "G:/Drives compartilhados/valueflow/Clientes e Parceiros/SIGP/SIP - Sistema de Informação de Projetos V3.pptx",
                                   "tipo": "Anotação de Responsabilidade Técnica (ART)", "area": "Licitacao", "comentario": "Anotações da Licitação dia 01"})
            DBAnexos.Linha.append({"Projeto": "0001", "Licitacao": "0001-02", "Contrato": "000201", "caminho": "G:/Drives compartilhados/valueflow/Clientes e Parceiros/SIGP/SIP - Sistema de Informação de Projetos V3.pptx",
                                   "tipo": "Ata de Reunião do Conselho Deliberativo", "area": "Licitacao", "comentario": "Arquivo da Licitação"})

    def atualizar_lista():
        # Limpa lista
        for item in tree.get_children():
            tree.delete(item)

        # Reinsere todos
        # for arq in arquivos:
        for arq in DBAnexos.Linha:
            tree.insert("", "end", values=(
                arq["caminho"], arq["tipo"], arq["comentario"]))

    def abrir_arquivo():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um arquivo na lista.")
            return

        item_id = selecionado[0]
        caminho = tree.item(item_id, "values")[0]

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

    def excluir_arquivo():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning(
                "Aviso", "Selecione um arquivo para excluir.")
            return

        item_id = selecionado[0]
        caminho = tree.item(item_id, "values")[0]

        # Remove da lista de arquivos
        # for arq in arquivos:
        for arq in DBAnexos.Linha:
            if arq["caminho"] == caminho:
                # arquivos.remove(arq)
                DBAnexos.Linha.remove(arq)
                break

        atualizar_lista()

    def selecionar_arquivo():
        if len(arquivos) >= MAX_ARQUIVOS:
            messagebox.showwarning(
                "Limite atingido", f"Você só pode adicionar até {MAX_ARQUIVOS} arquivos.")
            return

        caminho = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=(("Todos os arquivos", "*.*"),
                       ("Arquivos de texto", "*.txt"))
        )
        Anexos_window.focus_force()

        if caminho:
            DBAnexos.Linha.append({"Projeto": "0000", "Licitacao": "0000-00", "Contrato": "000000", "caminho": caminho,
                                   "tipo": "", "comentario": ""})

            atualizar_lista()

    def editar_celula(event):
        """Permite edição direta no Treeview com Combobox (Tipo) ou Entry (Comentário)."""
        selecionado = tree.selection()
        if not selecionado:
            return
        item_id = selecionado[0]
        col = tree.identify_column(event.x)  # ex: "#1", "#2", "#3"
        linha = tree.identify_row(event.y)

        if col == "#2":  # Coluna "Tipo"
            x, y, largura, altura = tree.bbox(item_id, column=col)
            valor_atual = tree.set(item_id, "Tipo")
            combo = ttk.Combobox(
                tree, values=DBListaAnexos.DBTipoAnexos, state="readonly")
            combo.place(x=x, y=y, width=largura, height=altura)
            combo.set(valor_atual)
            combo.focus()

            def salvar_tipo(event=None):
                novo_valor = combo.get()
                tree.set(item_id, "Tipo", novo_valor)
                for arq in arquivos:
                    if arq["caminho"] == tree.set(item_id, "Arquivo"):
                        arq["tipo"] = novo_valor
                        break
                combo.destroy()

            combo.bind("<Return>", salvar_tipo)
            combo.bind("<FocusOut>", salvar_tipo)

        elif col == "#3":  # Coluna "Comentário"
            x, y, largura, altura = tree.bbox(item_id, column=col)
            valor_atual = tree.set(item_id, "Comentário")
            entry = tk.Entry(tree)
            entry.place(x=x, y=y, width=largura, height=altura)
            entry.insert(0, valor_atual)
            entry.focus()

            def salvar_comentario(event=None):
                novo_valor = entry.get()
                tree.set(item_id, "Comentário", novo_valor)
                for arq in arquivos:
                    if arq["caminho"] == tree.set(item_id, "Arquivo"):
                        arq["comentario"] = novo_valor
                        break
                entry.destroy()

            entry.bind("<Return>", salvar_comentario)
            entry.bind("<FocusOut>", salvar_comentario)

    quadroB = tk.Frame(Anexos_window, borderwidth=2,
                       relief="ridge", padx=5, pady=15, bg="#A6CAEC")
    quadroB.grid(row=20, column=0, padx=5, pady=15, columnspan=8, sticky="w")
    quadroB.grid_propagate(False)
    quadroB.config(width=1000, height=50)
    quadroB.grid_columnconfigure(0, weight=1)

    frame_tree = tk.Frame(Anexos_window, borderwidth=2, relief="ridge",
                          padx=5, pady=15, bg="#A6CAEC")
    frame_tree.grid(row=2, column=0, padx=5, pady=15, columnspan=8, sticky="w")
    frame_tree.grid_propagate(False)
    frame_tree.config(width=1000, height=300)

# Treeview
# Anexos
# ==============================================================================
    colunas = ("Arquivo", "Tipo", "Comentário")
    tree = ttk.Treeview(frame_tree, columns=colunas, show="headings", height=8)

    tree.heading("Arquivo", text="Arquivo",
                 command=lambda idx=0: ordenar(tree, idx, False))
    tree.heading("Tipo", text="Tipo",
                 command=lambda idx=1: ordenar(tree, idx, False))
    tree.heading("Comentário", text="Comentário",
                 command=lambda idx=2: ordenar(tree, idx, False))

    tree.column("Arquivo", width=150)
    tree.column("Tipo", width=200)
    tree.column("Comentário", width=250)

# Scrollbars
    scroll_y = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)

# Grid para organizar Treeview + Scrollbars
    tree.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")

# Expansão ao redimensionar
    frame_tree.grid_rowconfigure(0, weight=1)
    frame_tree.grid_columnconfigure(0, weight=1)

# Evento de duplo clique para editar
    tree.bind("<Double-1>", editar_celula)

    btn_add = tk.Button(quadroB, command=lambda: selecionar_arquivo(), text="Adicionar Arquivo", font=("Helvetica", 7, "bold"), bg="#A6CAEC", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                        relief="raised", width=20, height=1)
    btn_add.grid(row=16, column=0, padx=5, pady=1, sticky="w")

    btn_open = tk.Button(quadroB, command=lambda: abrir_arquivo(), text="Abrir Selecionado", font=("Helvetica", 7, "bold"), bg="#A6CAEC", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                         relief="raised", width=20, height=1)
    btn_open.grid(row=16, column=1, padx=25, pady=1, sticky="w")

    btn_open = tk.Button(quadroB, command=lambda: excluir_arquivo(), text="Excluir Selecionado", font=("Helvetica", 7, "bold"), bg="#A6CAEC", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                         relief="raised", width=20, height=1)
    btn_open.grid(row=16, column=2, padx=25, pady=1, sticky="w")

    btn_open = tk.Button(quadroB, command=lambda: Anexos_window.destroy(), text="Volta", font=("Helvetica", 7, "bold"), bg="#67958d", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                         relief="raised", width=20, height=1)
    btn_open.grid(row=16, column=3, padx=25, pady=1, sticky="w")

    btn_open = tk.Button(quadroB, command=lambda: Anexos_window.destroy(), text="Salva", font=("Helvetica", 7, "bold"), bg="#67958d", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                         relief="raised", width=20, height=1)
    btn_open.grid(row=16, column=4, padx=25, pady=1, sticky="w")

    leitura_anexos()

    atualizar_lista()
# ======================================================================================================
# ======================================================================================================


# =====================================================================================================
# Criar janela
janela = tk.Tk()
janela.title(
    "SIGP - Sistema de Informações de Gerência de Projetos")
janela.iconbitmap("RM.ICO")
janela.geometry("1125x600+5+5")

# Área principal
# ---------------------------------------------------------------------------------------------
frame_principal = tk.Frame(janela, bg="#CDE4F0", width=50, height=50)

frame_principal.pack(side="right", fill="both", expand=True)

# Frames
# ---------------------------------------------------------------------------------------------
frame_tabela_Usuario = tk.Frame(frame_principal, height=1, bg="#A6CAEC")

# frame_cadastro_usuario
# ----------------------------------------------------------------------------
frame_cadastro_usuario = tk.Frame(frame_principal, height=1, bg="#FFFFFF")

quadroU = tk.Frame(frame_cadastro_usuario, borderwidth=2,
                   relief="ridge", padx=5, pady=5, bg="#CDE4F0")
quadroU.grid(row=0, column=0, padx=5, pady=5, columnspan=8, sticky="w")
quadroU.grid_propagate(False)
quadroU.config(width=1050, height=50)

IdProjetof = tk.Label(quadroU, text="Projeto:", bg="#CDE4F0")
IdProjetof.grid(row=0, column=0, padx=5, pady=10, sticky="w")
entry_IdProjetof = tk.Entry(quadroU, width=30)
entry_IdProjetof.grid(row=0, column=1, padx=5, pady=10, sticky="w")

# -----------------------------------
quadroB = tk.Frame(frame_cadastro_usuario, borderwidth=2,
                   relief="ridge", padx=5, pady=15, bg="#A6CAEC")
quadroB.grid(row=20, column=0, padx=5, pady=15, columnspan=8, sticky="w")
quadroB.grid_propagate(False)
quadroB.config(width=1050, height=50)

botao30 = tk.Button(quadroB, command=lambda: Usuarios(), text="Voltar", font=("Helvetica", 7, "bold"), bg="#09ACD0", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                    relief="raised", width=20, height=1)
botao30.grid(row=16, column=0, padx=5, pady=1, sticky="w")

botao30 = tk.Button(quadroB, command=lambda: Usuarios(), text="Excluir", font=("Helvetica", 7, "bold"), bg="#09ACD0", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                    relief="raised", width=20, height=1)
botao30.grid(row=16, column=1, padx=25, pady=1, sticky="w")

botao30 = tk.Button(quadroB, command=lambda: Usuarios(), text="Salvar", font=("Helvetica", 7, "bold"), bg="#09ACD0", fg="black", activebackground="#45a049", activeforeground="white", padx=10, pady=5, borderwidth=2,
                    relief="raised", width=20, height=1)
botao30.grid(row=16, column=1, padx=25, pady=1, sticky="w")

# Tabela para mostrar dados
# ===================================================================================================
# Criando um estilo para a Treeview
# ---------------------------------------------------------------------------------------------------
sort_order = {}

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


# Tabelas
# ---------------------------------------------------------------------------------------------------
frame_tabela_Usuario.grid_columnconfigure(0, weight=1)

# Scrollbar vertical
scrollbar = tk.Scrollbar(frame_tabela_Usuario)
scrollbar.grid(row=0, column=2, sticky="ns")

# Tabela (Treeview)
columns = ["Nome", "EMail", "Telefone", "Diretoria", "Setor"]
tabela_Usuario = ttk.Treeview(frame_tabela_Usuario, columns=columns,
                              show="headings", yscrollcommand=scrollbar.set, height=20)
tabela_Usuario.grid(row=0, column=0, columnspan=2,
                    sticky="nsew", padx=1, pady=1)

scrollbar.config(command=tabela_Usuario.yview)

# Cabeçalhos
tabela_Usuario.heading("Nome", text="Nome",
                       command=lambda idx=0: ordenar(tabela_Usuario, idx, False))
tabela_Usuario.heading("EMail", text="EMail",
                       command=lambda idx=1: ordenar(tabela_Usuario, idx, False))
tabela_Usuario.heading("Telefone", text="Telefone",
                       command=lambda idx=2: ordenar(tabela_Usuario, idx, False))
tabela_Usuario.heading("Diretoria", text="Diretoria",
                       command=lambda idx=3: ordenar(tabela_Usuario, idx, False))
tabela_Usuario.heading("Setor", text="Setor",
                       command=lambda idx=4: ordenar(tabela_Usuario, idx, False))

tabela_Usuario.column("Nome", width=200)
tabela_Usuario.column("EMail", width=40)
tabela_Usuario.column("Telefone", width=40)
tabela_Usuario.column("Diretoria", width=40)
tabela_Usuario.column("Setor", width=40)

tabela_Usuario.bind("<<TreeviewSelect>>", usuario_escolhido)

# ===========================================================================

menu_lateral = tk.Frame(janela, bg="#FFFFFF", width=50)
menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)

botao = tk.Button(menu_lateral, command=lambda: Anexos(
    "Projeto"), text="Anexos Projeto", bg="#FFFFFF", font=("Arial", 6), compound="top")
botao.pack(side="top", pady=12)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(menu_lateral, command=lambda: Anexos(
    "Licitacao"), text="Anexos Licitacao", bg="#FFFFFF", font=("Arial", 6), compound="top")
botao.pack(side="top", pady=12)  # Pode usar: side="left", "right", "bottom"

botao = tk.Button(menu_lateral, command=lambda: Usuarios(
), text="Usuarios", bg="#FFFFFF", font=("Arial", 6), compound="top")
botao.pack(side="top", pady=12)  # Pode usar: side="left", "right", "bottom"

janela.mainloop()
