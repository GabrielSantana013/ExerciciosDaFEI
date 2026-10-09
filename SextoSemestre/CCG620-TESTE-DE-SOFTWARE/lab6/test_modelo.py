# test_modelo.py
from itertools import product
from modelo import PARAMS, casos, pares_de

def test_quantidade():
    assert len(list(product(*PARAMS))) == 54
    assert len(casos) >= 9

def test_conjunto_cobre_todos_os_pares():
    assert pares_de(casos) == pares_de(product(*PARAMS))

def test_verificador_aponta_descobertos():
    descobertos = pares_de(product(*PARAMS)) - pares_de(casos[:3])
    assert len(descobertos) > 0