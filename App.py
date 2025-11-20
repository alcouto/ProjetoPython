"""
Connects to a SQL database using pyodbc
"""
import pyodbc

# Servidor no Azure --------------------------------------------------------------------
# server = 'grupo-sigp.database.windows.net'
# database = 'SISPC'
# username = 'alcouto'
# password = 'Irm@2000'  # use a senha que definiu
# driver = '{ODBC Driver 17 for SQL Server}'

# conn_str = (
#    f'DRIVER={driver};'
#    f'SERVER={server},1433;'
#    f'DATABASE={database};'
#    f'UID={username};'
#    f'PWD={password};'
#    'Encrypt=yes;'
#    'TrustServerCertificate=no;'
#    'Connection Timeout=30;'
# )

# Servidor Interno --------------------------------------------------------------------
# server = r"DESKTOP-08K13CE\SQLEXPRESS"
server = r"desktop-ndn2tot"
database = 'DBDoBinho'
username = 'alcouto'
password = 'alcouto'
driver = '{ODBC Driver 17 for SQL Server}'

conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server},1433;'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
    'Connection Timeout=30;'
)

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()
sql = '''select * from clientes'''
cursor.execute(sql)
resultados = cursor.fetchall()

for linha in resultados:
    print(f"ID: {linha[0]}, Nome: {linha[1]}")

conn.close()
