"""
Connects to a SQL database using pyodbc
"""
import pyodbc

# Exemplo: 'localhost' ou o nome do servidor
server = 'DESKTOP-08K13CE\SQLEXPRESS'
database = 'SIGP'  # Nome do banco de dados
username = 'alcouto'  # Seu nome de usuário
password = 'alcouto'  # Sua senha

conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

sql = '''select Projetos.ID_Projeto, Projetos.NomeProjeto, Licitacao.IdLicitacao, Contrato.IdContrato, Projetos.Fase 
               from Projetos
               left join Licitacao on Projetos.ID_Projeto = Licitacao.IdProjeto
               left join Contrato on Projetos.ID_Projeto = Contrato.IdProjeto
               order by Projetos.ID_Projeto'''

cursor.execute(sql)

resultados = cursor.fetchall()

for linha in resultados:
    print(f"ID: {linha[0]}, Nome: {linha[1]}")

# for row in cursor:
#    print(row)


conn.close()
