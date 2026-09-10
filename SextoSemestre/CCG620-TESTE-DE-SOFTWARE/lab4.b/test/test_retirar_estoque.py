from src import retirar_do_estoque
import pytest

def test_retirar_do_estoque_sucesso(estoque_inicial):
    estoque_atual = retirar_do_estoque(estoque_inicial, 5)
    assert estoque_atual == estoque_inicial - 5


def test_retirar_do_estoque_insuficiente():
    with pytest.raises(ValueError) as e:
        retirar_do_estoque(10, 20)
    assert str(e.value) == "quantidade insuficiente em estoque"
    
    