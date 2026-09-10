from src import calcular_valor_total


def test_calcular_valor_total():
    assert calcular_valor_total(10, 5) == 50
    assert calcular_valor_total(0, 5) == 0
    assert calcular_valor_total(10, 0) == 0
    assert calcular_valor_total(10, -5) == -50
    assert calcular_valor_total(-10, 5) == -50