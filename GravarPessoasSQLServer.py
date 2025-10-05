import tkinter as tk
from tkinter import messagebox
import pyodbc

# Função para gravar o nome no banco de dados SQL Server


def gravar_nome():
    nome = entry_nome.get()  # Pega o nome digitado

    if nome:
        try:
            # Conexão com o banco de dados SQL Server
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=SEU_SERVIDOR;'
                'DATABASE=SEU_BANCO_DE_DADOS;'
                'UID=SEU_USUARIO;'
                'PWD=SEU_PASSWORD'
            )
            cursor = conn.cursor()

            # Criar a tabela (se não existir)
            cursor.execute('''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='pessoas' AND xtype='U')
                CREATE TABLE pessoas (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    nome NVARCHAR(100)
                )
            ''')
            conn.commit()

            # Inserir o nome na tabela
            cursor.execute('INSERT INTO pessoas (nome) VALUES (?)', (nome,))
            conn.commit()

            # Fechar a conexão
            conn.close()

            # Exibir mensagem de sucesso
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
