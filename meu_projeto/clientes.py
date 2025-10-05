from dbconfig import get_connection


def add_cliente(nome, diretoria_codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (nome, diretoria_codigo) VALUES (?, ?)", (nome, diretoria_codigo))
    conn.commit()
    conn.close()


def get_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT c.codigo, c.nome, d.descricao 
    FROM clientes c LEFT JOIN diretorias d
    ON c.diretoria_codigo = d.codigo
    """)
    result = cursor.fetchall()
    conn.close()
    return result


def update_cliente(codigo, nome, diretoria_codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome=?, diretoria_codigo=? WHERE codigo=?",
                   (nome, diretoria_codigo, codigo))
    conn.commit()
    conn.close()


def delete_cliente(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE codigo=?", (codigo,))
    conn.commit()
    conn.close()
