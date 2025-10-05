# Configurações do SQL Server
import pyodbc
from tkinter import simpledialog, messagebox

from dbtabelas import DB_projeto

# Configurações do SQL Server
server = r"DESKTOP-08K13CE\SQLEXPRESS"
database = "DBDoBinho"
username = "alcouto"
password = "alcouto"


def get_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    return conn


def insert_projeto():
    print("DB id projeto")
    print(DB_projeto.DB_idprojeto)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projetos (idprojeto, nomeprojeto) VALUES (?, ?)", (DB_projeto.DB_idprojeto, DB_projeto.DB_nomeprojeto))
    conn.commit()
    conn.close()

    messagebox.showwarning("Gravar", "Gravação OK")
