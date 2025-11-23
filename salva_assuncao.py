from flask import Flask, jsonify, request
import pyodbc
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# 🔥 Libera requisições externas (HTML, Flutter, Postman, ReqBin etc.)
CORS(app)


def conectar_sql():
    server = r"desktop-ndn2tot"
    database = 'Pegasus'
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
#  NOVO ENDPOINT PARA SALVAR Assuncao
# ---------------------------------------------------------
@app.route('/salva_assuncao', methods=['POST'])
def salva_localizacao():
    dados = request.get_json()

    usuario = dados.get("usuario")
    tipo_servico = dados.get("tipo_servico")
    posto = dados.get("posto")
    data_selecionada = dados.get("data")
    hora_selecionada = dados.get("hora")

    if not usuario or tipo_servico is None or posto is None:
        return jsonify({"erro": "Dados incompletos"}), 400

    conn = conectar_sql()
    cursor = conn.cursor()

    cursor.execute("""
       INSERT INTO AssuncaoServico (UsuarioId, TipoServico, Posto, DataSelecionada)
       VALUES (?, ?, ?, GETDATE())
    """, usuario, tipo_servico, posto)

    conn.commit()
    conn.close()

    return jsonify({"status": "OK", "mensagem": "Assunção salva com sucesso"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
