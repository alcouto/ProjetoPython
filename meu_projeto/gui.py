import tkinter as tk
from tkinter import ttk, messagebox
from clientes import add_cliente, get_clientes, update_cliente, delete_cliente
# from diretorias import add_diretoria, get_diretorias, update_diretoria, delete_diretoria

# editado por binho no VS e no guit


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Clientes e Diretorias (SQL Server)")

        # Abas
        self.tab_control = ttk.Notebook(root)

        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_diretorias = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.add(self.tab_diretorias, text="Diretorias")
        self.tab_control.pack(expand=1, fill="both")

        self.setup_clientes_tab()
        self.setup_diretorias_tab()

    # ====================== CLIENTES ======================
    def setup_clientes_tab(self):
        frame = ttk.Frame(self.tab_clientes)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview
        self.tree_clientes = ttk.Treeview(
            frame, columns=("codigo", "nome", "diretoria"), show="headings"
        )
        self.tree_clientes.heading("codigo", text="Código")
        self.tree_clientes.heading("nome", text="Nome")
        self.tree_clientes.heading("diretoria", text="Diretoria")
        self.tree_clientes.pack(fill="both", expand=True)

        # Botões
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=5)

        ttk.Button(btn_frame, text="Adicionar", command=self.add_cliente_form).grid(
            row=0, column=0, padx=5
        )
        ttk.Button(btn_frame, text="Editar", command=self.edit_cliente_form).grid(
            row=0, column=1, padx=5
        )
        ttk.Button(btn_frame, text="Excluir", command=self.delete_cliente_action).grid(
            row=0, column=2, padx=5
        )

        self.refresh_clientes()

    def refresh_clientes(self):
        for i in self.tree_clientes.get_children():
            self.tree_clientes.delete(i)
        for row in get_clientes():
            self.tree_clientes.insert("", "end", values=row)

    def add_cliente_form(self):
        form = tk.Toplevel(self.root)
        form.title("Adicionar Cliente")

        tk.Label(form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        entry_nome = tk.Entry(form)
        entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Diretoria:").grid(row=1, column=0, padx=5, pady=5)
        diretorias = get_diretorias()
        cb_diretoria = ttk.Combobox(
            form, values=[f"{d[0]} - {d[1]}" for d in diretorias])
        cb_diretoria.grid(row=1, column=1, padx=5, pady=5)

        def salvar():
            nome = entry_nome.get()
            if not nome:
                messagebox.showwarning("Atenção", "Nome não pode ser vazio!")
                return
            diretoria_id = None
            if cb_diretoria.get():
                diretoria_id = int(cb_diretoria.get().split(" - ")[0])
            add_cliente(nome, diretoria_id)
            self.refresh_clientes()
            form.destroy()

        ttk.Button(form, text="Salvar", command=salvar).grid(
            row=2, column=0, columnspan=2, pady=10
        )

    def edit_cliente_form(self):
        selected = self.tree_clientes.selection()
        if not selected:
            messagebox.showwarning(
                "Atenção", "Selecione um cliente para editar")
            return
        values = self.tree_clientes.item(selected[0], "values")
        codigo, nome, diretoria = values

        form = tk.Toplevel(self.root)
        form.title("Editar Cliente")

        tk.Label(form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        entry_nome = tk.Entry(form)
        entry_nome.insert(0, nome)
        entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Diretoria:").grid(row=1, column=0, padx=5, pady=5)
        diretorias = get_diretorias()
        cb_diretoria = ttk.Combobox(
            form, values=[f"{d[0]} - {d[1]}" for d in diretorias])
        if diretoria:
            cb_diretoria.set(diretoria)
        cb_diretoria.grid(row=1, column=1, padx=5, pady=5)

        def salvar():
            novo_nome = entry_nome.get()
            diretoria_id = None
            if cb_diretoria.get():
                diretoria_id = int(cb_diretoria.get().split(" - ")[0])
            update_cliente(codigo, novo_nome, diretoria_id)
            self.refresh_clientes()
            form.destroy()

        ttk.Button(form, text="Salvar", command=salvar).grid(
            row=2, column=0, columnspan=2, pady=10
        )

    def delete_cliente_action(self):
        selected = self.tree_clientes.selection()
        if not selected:
            messagebox.showwarning(
                "Atenção", "Selecione um cliente para excluir")
            return
        values = self.tree_clientes.item(selected[0], "values")
        codigo = values[0]
        if messagebox.askyesno("Confirmação", "Deseja excluir este cliente?"):
            delete_cliente(codigo)
            self.refresh_clientes()

    # ====================== DIRETORIAS ======================
    def setup_diretorias_tab(self):
        frame = ttk.Frame(self.tab_diretorias)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree_diretorias = ttk.Treeview(
            frame, columns=("codigo", "descricao"), show="headings"
        )
        self.tree_diretorias.heading("codigo", text="Código")
        self.tree_diretorias.heading("descricao", text="Descrição")
        self.tree_diretorias.pack(fill="both", expand=True)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=5)

        ttk.Button(btn_frame, text="Adicionar", command=self.add_diretoria_form).grid(
            row=0, column=0, padx=5
        )
        ttk.Button(btn_frame, text="Editar", command=self.edit_diretoria_form).grid(
            row=0, column=1, padx=5
        )
        ttk.Button(btn_frame, text="Excluir", command=self.delete_diretoria_action).grid(
            row=0, column=2, padx=5
        )

        self.refresh_diretorias()

    def refresh_diretorias(self):
        for i in self.tree_diretorias.get_children():
            self.tree_diretorias.delete(i)
        for row in get_diretorias():
            self.tree_diretorias.insert("", "end", values=row)

    def add_diretoria_form(self):
        form = tk.Toplevel(self.root)
        form.title("Adicionar Diretoria")

        tk.Label(form, text="Descrição:").grid(row=0, column=0, padx=5, pady=5)
        entry_desc = tk.Entry(form)
        entry_desc.grid(row=0, column=1, padx=5, pady=5)

        def salvar():
            descricao = entry_desc.get()
            if not descricao:
                messagebox.showwarning(
                    "Atenção", "Descrição não pode ser vazia!")
                return
            add_diretoria(descricao)
            self.refresh_diretorias()
            form.destroy()

        ttk.Button(form, text="Salvar", command=salvar).grid(
            row=1, column=0, columnspan=2, pady=10
        )

    def edit_diretoria_form(self):
        selected = self.tree_diretorias.selection()
        if not selected:
            messagebox.showwarning(
                "Atenção", "Selecione uma diretoria para editar")
            return
        values = self.tree_diretorias.item(selected[0], "values")
        codigo, descricao = values

        form = tk.Toplevel(self.root)
        form.title("Editar Diretoria")

        tk.Label(form, text="Descrição:").grid(row=0, column=0, padx=5, pady=5)
        entry_desc = tk.Entry(form)
        entry_desc.insert(0, descricao)
        entry_desc.grid(row=0, column=1, padx=5, pady=5)

        def salvar():
            nova_desc = entry_desc.get()
            update_diretoria(codigo, nova_desc)
            self.refresh_diretorias()
            form.destroy()

        ttk.Button(form, text="Salvar", command=salvar).grid(
            row=1, column=0, columnspan=2, pady=10
        )

    def delete_diretoria_action(self):
        selected = self.tree_diretorias.selection()
        if not selected:
            messagebox.showwarning(
                "Atenção", "Selecione uma diretoria para excluir")
            return
        values = self.tree_diretorias.item(selected[0], "values")
        codigo = values[0]
        if messagebox.askyesno("Confirmação", "Deseja excluir esta diretoria?"):
            delete_diretoria(codigo)
            self.refresh_diretorias()
