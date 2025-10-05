import tkinter as tk
from tkinter import ttk
import pyodbc


def carregar_dados():
    # Limpa a tabela
    for item in tree.get_children():
        tree.delete(item)

    # Executa o SELECT no banco
    sql = '''SELECT * FROM Projetos'''
    cursor.execute(sql)
    resultados = cursor.fetchall()

    print(resultados[0][0], resultados[0][1], resultados[0][1])
    print(resultados[1][0], resultados[1][1], resultados[1][1])

    # for linha in resultados:
    #    for campo in linha:
    #        # imprime os campos na mesma linha, separados por tabulação
    #        print(campo, end="\t")
    #        print()  # quebra de linha após cada linha

    # Insere os dados no Treeview
    i = 0
    for linha in resultados:
        tree.insert("", "end", values=(
            resultados[i][0], resultados[i][1], resultados[i][2]))
        i = i+1

    # tree.insert("", "end", values=("1111", "2222", "3333"))


# --- Interface gráfica ---
janela = tk.Tk()
janela.title("Exemplo de Tabela com SELECT")

frame_tabela = tk.Frame(janela)
frame_tabela.pack(padx=10, pady=10)

# Define colunas
colunas = ("ID", "Nome", "Idade")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

# Define os títulos das colunas
for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack()

# --- Banco de dados (Exemplo com SQLite) ---
server = "DESKTOP-08K13CE\SQLEXPRESS"
database = 'SIGP'  # Nome do banco de dados
username = 'alcouto'  # Seu nome de usuário
password = 'alcouto'  # Sua senha

conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

# Carrega os dados do banco para a tabela
carregar_dados()

janela.mainloop()
