import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para gravar o nome no banco de dados


def gravar_nome():
    nome = entry_nome.get()  # Pega o nome digitado

    if nome:
        try:
            # Conectar ao banco de dados (ou criar se não existir)
            conn = sqlite3.connect('nomes.db')
            cursor = conn.cursor()

            # Criar tabela se não existir
            cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT)''')

            # Inserir o nome na tabela
            cursor.execute('INSERT INTO pessoas (nome) VALUES (?)', (nome,))

            # Salvar as mudanças e fechar a conexão
            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Sucesso", f"Nome '{nome}' gravado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gravar o nome: {e}")
    else:
        messagebox.showwarning("Atenção", "Por favor, digite um nome.")


# Criando a janela principal
janela = tk.Tk()
janela.title("Tela de Nome")  # Título da janela

# Criando o rótulo (label) para pedir o nome
label = tk.Label(janela, text="Digite seu nome:")
label.pack(pady=10)

# Criando a caixa de entrada (entry) para digitar o nome
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack(pady=10)

# Criando o botão para submeter o nome
botao = tk.Button(janela, text="Enviar", command=gravar_nome)
botao.pack(pady=10)

# Rodando a aplicação
janela.mainloop()
