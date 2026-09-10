import pytest
from src import classificar_estoque


def test_classificar_estoque_limite_100():
    assert classificar_estoque(100) == "Alto"
    assert classificar_estoque(101) == "Alto"
    assert classificar_estoque(99) == "Normal"


def test_classificar_estoque_limite_20():
    assert classificar_estoque(20) == "Normal"
    assert classificar_estoque(21) == "Normal"
    assert classificar_estoque(19) == "Baixo"


@pytest.mark.parametrize("quantidade, esperado", [
    # (valor, resultado_esperado)
    (100, "Alto"),
    (101, "Alto"),
    (99, "Normal"),
    (20, "Normal"),
    (21, "Normal"),
    (19, "Baixo")
])
def test_classificar_estoque_parametrizado(quantidade, esperado):
    assert classificar_estoque(quantidade) == esperado