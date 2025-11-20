from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)


def conectar_sql():
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

    return conn


@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = conectar_sql()

    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nome FROM clientes")
    rows = cursor.fetchall()

    conn.close()

    clientes = [{"codigo": r[0], "nome": r[1]} for r in rows]

    return jsonify(clientes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
