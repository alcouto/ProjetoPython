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


# @app.route('/usuario/<int:id>', methods=['GET'])
@app.route('/usuario/<id>', methods=['GET'])
def buscar_usuario(id):
    conn = conectar_sql()
    cursor = conn.cursor()

    # Consulta somente a senha do usuário com o Id informado
    cursor.execute("SELECT Id, Senha FROM Usuarios WHERE RTRIM(Id) = ?", id)
    row = cursor.fetchone()

    conn.close()

    # Se não encontrou o usuário
    if not row:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    # Monta o retorno
    usuario = {
        "id": row[0],
        "senha": row[1]
    }

    return jsonify(usuario)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
