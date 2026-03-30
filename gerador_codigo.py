from db import conectar

def gerar_codigo(grupo, tipo_alimento, pais):
    if not grupo or not tipo_alimento or not pais:
        raise ValueError("Campos não podem ser vazios")

    if len(pais) != 2:
        raise ValueError("Pais deve ter 2 caracteres")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MAX(sec) FROM codigos_sequenciais
        WHERE Grupo=%s AND Tipo_Alimento=%s AND Pais=%s
    """, (grupo, tipo_alimento, pais))

    resultado = cursor.fetchone()[0]
    novo_sec = 1 if resultado is None else resultado + 1

    codigo = f"{pais}{grupo}{str(novo_sec).zfill(4)}{tipo_alimento}"

    cursor.execute("""
        INSERT INTO codigos_sequenciais (codigo, sec, Grupo, Tipo_Alimento, Pais)
        VALUES (%s, %s, %s, %s, %s)
    """, (codigo, novo_sec, grupo, tipo_alimento, pais))

    conn.commit()
    conn.close()

    return codigo, novo_sec