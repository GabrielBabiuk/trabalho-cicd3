import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="alimentos"
    )

def gerar_codigo(grupo, subgrupo, pais):
    if not grupo or not subgrupo:
        raise ValueError("Grupo e subgrupo são obrigatórios")

    if len(pais) != 2:
        raise ValueError("País deve ter 2 caracteres")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT MAX(sec) FROM alimentos WHERE grupo = %s",
        (grupo,)
    )
    resultado = cursor.fetchone()

    if resultado[0] is None:
        sec = 1
    else:
        sec = resultado[0] + 1

    codigo = f"{pais}{grupo}{str(sec).zfill(4)}{subgrupo}"

    cursor.execute(
        "INSERT INTO alimentos (codigo, grupo, subgrupo, sec) VALUES (%s, %s, %s, %s)",
        (codigo, grupo, subgrupo, sec)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return codigo, sec
