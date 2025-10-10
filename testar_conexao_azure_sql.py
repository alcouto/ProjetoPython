import socket
import pyodbc
import ssl
import requests

# ===============================================
# CONFIGURAÇÕES DO SEU SERVIDOR AZURE SQL
# ===============================================
server = "grupo-sigp.database.windows.net"   # Nome completo do servidor
database = "SIGP"                            # Nome do banco de dados
username = "alcouto"                        # Login do SQL (use @servidor)
password = "Irm@2000"                    # Senha do login
driver = "{ODBC Driver 17 for SQL Server}"   # Use sempre o driver mais novo
porta = 1433                                 # Porta padrão do Azure SQL
# ===============================================


def testar_ip_publico():
    """Detecta o IP público atual"""
    print("\n🌐 Testando IP público...")
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text
        print(f"✅ IP público detectado: {ip}")
    except Exception as e:
        print(f"❌ Não foi possível detectar o IP público: {e}")


def testar_dns():
    """Verifica se o nome do servidor resolve para um IP"""
    print(f"\n🔎 Testando resolução DNS para {server}...")
    try:
        ip = socket.gethostbyname(server)
        print(f"✅ DNS OK — {server} resolve para {ip}")
    except Exception as e:
        print(f"❌ Falha na resolução DNS: {e}")


def testar_porta():
    """Testa se a porta 1433 está aberta"""
    print(f"\n🚪 Testando acesso à porta {porta}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((server, porta))
        print(f"✅ Porta {porta} aberta — conexão TCP bem-sucedida!")
    except Exception as e:
        print(f"❌ Porta {porta} bloqueada ou inacessível: {e}")
    finally:
        s.close()


def testar_tls():
    """Verifica suporte a TLS (necessário para Azure SQL)"""
    print("\n🔐 Testando suporte a TLS/SSL...")
    context = ssl.create_default_context()
    try:
        with socket.create_connection((server, porta), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=server) as ssock:
                print(f"✅ TLS OK — versão usada: {ssock.version()}")
    except ssl.SSLError as e:
        print(f"❌ Erro de TLS/SSL: {e}")
    except Exception as e:
        print(f"⚠️ Falha ao testar TLS: {e}")


def testar_conexao_sql():
    """Tenta autenticar e executar uma consulta simples"""
    print("\n🧩 Testando autenticação e conexão com o banco de dados...")

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

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION;")
        versao = cursor.fetchone()[0]
        print("✅ Conexão com o banco bem-sucedida!")
        print(f"🆔 Versão do SQL Server: {versao}")
        cursor.close()
        conn.close()
    except pyodbc.InterfaceError as e:
        print(f"❌ Erro de driver ODBC ou configuração incorreta: {e}")
    except pyodbc.OperationalError as e:
        print(f"❌ Erro operacional (rede, firewall ou login): {e}")
    except Exception as e:
        print(f"⚠️ Outro erro ao conectar: {e}")


if __name__ == "__main__":
    print("=======================================")
    print("🔧 TESTE DE CONEXÃO COM AZURE SQL SERVER")
    print("=======================================")
    testar_ip_publico()
    testar_dns()
    testar_porta()
    testar_tls()
    testar_conexao_sql()
    print("\n🧠 Diagnóstico concluído.")
