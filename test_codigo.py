def test_tabela():
    conn = conectar()
    cursor = conn.cursor()

    print("\n===== ANTES =====")
    cursor.execute("SELECT * FROM codigos_sequenciais")
    antes = cursor.fetchall()
    for linha in antes:
        print(linha)

    codigo, sec = gerar_codigo("A", "B", "BR")
    print(f"\nGerado: {codigo} | Sec: {sec}")

    print("\n===== DEPOIS =====")
    cursor.execute("SELECT * FROM codigos_sequenciais")
    depois = cursor.fetchall()
    for linha in depois:
        print(linha)

    cursor.close()
    conn.close()

    assert True
