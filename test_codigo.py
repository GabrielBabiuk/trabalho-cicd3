import pytest
from gerador_codigo import gerar_codigo

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