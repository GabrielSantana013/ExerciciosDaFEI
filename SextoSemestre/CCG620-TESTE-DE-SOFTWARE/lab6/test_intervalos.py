import hypothesis.strategies as st
import pytest
from hypothesis import given

from intervalos import mesclar, mesclar_original


# a) entradas: listas de pares de inteiros de 0 a 50
pares = st.lists(st.tuples(st.integers(0, 50), st.integers(0, 50)))


def normalizar(par):
    """Poe o par na forma (ini, fim) com ini <= fim."""
    a, b = par
    return (a, b) if a <= b else (b, a)


entradas = pares.map(lambda lista: [normalizar(p) for p in lista])


# b) propriedades de mesclar
def prop_idempotencia(f, entrada):
    once = f(entrada)
    assert f(once) == once


def prop_ordem_sem_sobreposicao(f, entrada):
    res = f(entrada)
    for ini, fim in res:
        assert ini <= fim
    for (_, fim1), (ini2, _) in zip(res, res[1:]):
        # fim estritamente menor que o proximo ini: se so se tocassem, seriam unidos
        assert fim1 < ini2


def prop_contencao(f, entrada):
    res = f(entrada)
    for ini, fim in entrada:
        assert any(i <= ini and fim <= j for i, j in res)


PROPRIEDADES = [prop_idempotencia, prop_ordem_sem_sobreposicao, prop_contencao]


def test_normalizar():
    assert normalizar((5, 2)) == (2, 5)
    assert normalizar((2, 5)) == (2, 5)
    assert normalizar((3, 3)) == (3, 3)


# d) funcao corrigida: as tres propriedades valem
@given(entradas)
def test_idempotencia(entrada):
    prop_idempotencia(mesclar, entrada)


@given(entradas)
def test_ordem_sem_sobreposicao(entrada):
    prop_ordem_sem_sobreposicao(mesclar, entrada)


@given(entradas)
def test_contencao(entrada):
    prop_contencao(mesclar, entrada)


def test_exemplo_do_enunciado():
    assert mesclar([(1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]


# c) funcao original: so a contencao falha
@pytest.mark.parametrize("prop", [prop_idempotencia, prop_ordem_sem_sobreposicao])
def test_original_satisfaz(prop):
    @given(entradas)
    def rodar(entrada):
        prop(mesclar_original, entrada)
    rodar()


def test_original_viola_contencao():
    @given(entradas)
    def rodar(entrada):
        prop_contencao(mesclar_original, entrada)
    with pytest.raises(AssertionError):
        rodar()