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

    # Insere os dados no Treeview
    i = 0
    for linha in resultados:
        tree.insert("", "end", values=(
            resultados[i][0], resultados[i][1], resultados[i][2]))
        i = i+1


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


# --- Banco de dados Azure ---
server = 'grupo-sigp.database.windows.net'
database = 'SIGP'
username = 'alcouto'
password = 'Irm@2000'  # use a senha que definiu
driver = '{ODBC Driver 17 for SQL Server}'

conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server},1433;'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=30;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# --- Banco de dados Local ---
# server = "DESKTOP-08K13CE\SQLEXPRESS"
# server = "192.168.0.25,1433"
# database = 'SIGP'  # Nome do banco de dados
# username = 'alcouto'  # Seu nome de usuário
# password = 'alcouto'  # Sua senha
# conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()

# Carrega os dados do banco para a tabela
carregar_dados()

janela.mainloop()
