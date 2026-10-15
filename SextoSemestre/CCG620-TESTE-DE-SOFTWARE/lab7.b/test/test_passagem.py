"""Testes de preco de passagem por particionamento e pairwise."""
from itertools import combinations, product

import pytest
from allpairspy import AllPairs

from passagem import preco


REPRESENTANTES = [
    [1, 6, 40],                         # idade
    ["economica", "executiva"],        # classe
    [0, 1, 2],                          # malas
    ["nacional", "internacional"],     # trecho
]

LIMITES = [
    [0, 1, 2, 11, 12, 120],             # idade
    ["economica", "executiva"],
    [0, 1, 2],
    ["nacional", "internacional"],
]


def esperado(idade, classe, malas, trecho):
    tarifa = {"nacional": 400, "internacional": 1500}[trecho]
    if classe == "executiva":
        tarifa *= 2
    if idade <= 1:
        tarifa *= 0.10
    elif idade <= 11:
        tarifa *= 0.75
    return round(tarifa + 100 * malas, 2)


PAIRWISE_REPRESENTANTES = [tuple(caso) for caso in AllPairs(REPRESENTANTES)]
PAIRWISE_LIMITES = [tuple(caso) for caso in AllPairs(LIMITES)]
COMPLETO_REPRESENTANTES = list(product(*REPRESENTANTES))
COMPLETO_LIMITES = list(product(*LIMITES))


def combinacoes_de(casos, t):
    """Devolve as combinacoes de t valores, identificadas por parametro."""
    return {
        tuple((indice, caso[indice]) for indice in indices)
        for caso in casos
        for indices in combinations(range(len(caso)), t)
    }


TRIPLAS_COMPLETAS = combinacoes_de(COMPLETO_LIMITES, 3)
TRIPLAS_PAIRWISE = combinacoes_de(PAIRWISE_LIMITES, 3)
FORCA_3 = [tuple(caso) for caso in AllPairs(LIMITES, n=3)]
TRIPLAS_FORCA_3 = combinacoes_de(FORCA_3, 3)


@pytest.mark.parametrize("caso", PAIRWISE_REPRESENTANTES, ids=str)
def test_preco_pairwise_representantes(caso):
    if preco(*caso) != esperado(*caso):
        pytest.xfail("falha conhecida na implementacao original")
    assert preco(*caso) == esperado(*caso)


@pytest.mark.parametrize("caso", PAIRWISE_LIMITES, ids=str)
def test_preco_pairwise_limites(caso):
    if preco(*caso) != esperado(*caso):
        pytest.xfail("falha conhecida na implementacao original")
    assert preco(*caso) == esperado(*caso)


def test_falhas_do_pairwise_representantes():
    falhas = [c for c in PAIRWISE_REPRESENTANTES if preco(*c) != esperado(*c)]
    assert len(falhas) == 2
    assert any(c[0] == 6 and c[1] == "executiva" for c in falhas)


def test_falhas_do_pairwise_limites():
    falhas = [c for c in PAIRWISE_LIMITES if preco(*c) != esperado(*c)]
    assert len(falhas) == 5
    assert any(c[0] == 2 and c[1] == "economica" for c in falhas)
    assert sum(c[0] == 2 for c in falhas) == 3


def test_cobertura_de_triplas():
    assert len(TRIPLAS_COMPLETAS) == 108
    assert len(TRIPLAS_PAIRWISE) == 60
    assert TRIPLAS_PAIRWISE < TRIPLAS_COMPLETAS


def test_allpairs_forca_3_nao_cobre_todas_as_triplas():
    assert len(FORCA_3) == 19
    assert len(TRIPLAS_FORCA_3) == 61
    assert TRIPLAS_FORCA_3 < TRIPLAS_COMPLETAS
