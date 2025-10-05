import tkinter as tk
from tkinter import messagebox


def abrir_janela_login():
    # Cria uma nova janela (janela de login)
    login_window = tk.Toplevel(janela)
    login_window.title("Login")
    login_window.geometry("300x180")

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
            messagebox.showinfo("Login", "Login bem-sucedido!")
            login_window.destroy()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    # Botão Entrar
    btn_entrar = tk.Button(login_window, text="Entrar",
                           command=autenticar, bg="green", fg="white", width=15)
    btn_entrar.grid(row=2, column=0, columnspan=2, pady=15)


# Janela principal
janela = tk.Tk()
janela.title("Sistema Principal")
janela.geometry("400x200")

# Botão que abre a janela de login
btn_login = tk.Button(janela, text="Fazer Login",
                      command=abrir_janela_login, width=20)
btn_login.pack(pady=60)

janela.mainloop()
