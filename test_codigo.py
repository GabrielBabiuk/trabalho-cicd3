import pytest
from gerador_codigo import gerar_codigo
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="seu_banco"
    )

def test_tabela():
    conn = conectar()
    cursor = conn.cursor()

    print("\n===== ANTES =====")
    cursor.execute("SELECT * FROM alimentos")
    antes = cursor.fetchall()
    for linha in antes:
        print(linha)

    codigo, sec = gerar_codigo("A", "B", "BR")
    print(f"\nGerado: {codigo} | Sec: {sec}")

    print("\n===== DEPOIS =====")
    cursor.execute("SELECT * FROM alimentos")
    depois = cursor.fetchall()
    for linha in depois:
        print(linha)

    cursor.close()
    conn.close()

    assert True
