from flask import Flask, jsonify, request
import pyodbc
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# 🔥 Libera requisições externas (HTML, Flutter, Postman, ReqBin etc.)
CORS(app)


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
    return pyodbc.connect(conn_str)


# ---------------------------------------------------------
#  NOVO ENDPOINT PARA SALVAR LOCALIZAÇÃO
# ---------------------------------------------------------
@app.route('/salva_localizacao', methods=['POST'])
def salva_localizacao():
    dados = request.get_json()

    usuario = dados.get("usuario")
    latitude = dados.get("latitude")
    longitude = dados.get("longitude")

    if not usuario or latitude is None or longitude is None:
        return jsonify({"erro": "Dados incompletos"}), 400

    conn = conectar_sql()
    cursor = conn.cursor()

    cursor.execute("""
       INSERT INTO Localizacoes (UsuarioId, Latitude, Longitude, DataHora)
       VALUES (?, ?, ?, GETDATE())
    """, usuario, latitude, longitude)

    conn.commit()
    conn.close()

    return jsonify({"status": "OK", "mensagem": "Localização salva com sucesso"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
