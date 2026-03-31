import pytest
from gerador_codigo import gerar_codigo
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="alimentos"
    )

def test_geracao_codigo_existente():
    codigo, sec = gerar_codigo("C", "A", "BR")
    assert codigo.startswith("BRC")
    assert len(codigo) == 8

def test_primeiro_codigo_grupo_novo():
    codigo, sec = gerar_codigo("Z", "X", "BR")
    assert sec == 1
    assert codigo == "BRZ0001X"

def test_incremento_sec():
    _, sec1 = gerar_codigo("Y", "A", "BR")
    _, sec2 = gerar_codigo("Y", "A", "BR")
    assert sec2 == sec1 + 1

def test_zerofill():
    codigo, _ = gerar_codigo("T", "A", "BR")
    assert codigo[3:7].isdigit()
    assert len(codigo[3:7]) == 4

def test_entrada_invalida():
    with pytest.raises(ValueError):
        gerar_codigo("", "A", "BR")

def test_pais_invalido():
    with pytest.raises(ValueError):
        gerar_codigo("A", "B", "BRA")

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
