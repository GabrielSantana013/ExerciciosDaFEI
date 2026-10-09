"""Frete: esperado, funcao original (com defeitos), funcao corrigida e testes."""
from itertools import product

import pytest
from allpairspy import AllPairs

PARAMS = [
    ["leve", "medio", "pesado"],      # peso
    ["normal", "expressa"],           # urgencia
    [False, True],                    # seguro
    ["sul", "sudeste", "norte"],      # regiao
]


def frete_original(peso, urgencia, seguro, regiao):
    """Versao escrita por outra pessoa (com defeitos), mantida para comparacao."""
    base = {"leve": 10, "medio": 20, "pesado": 40}[peso]
    if regiao == "norte" and peso != "leve":
        base += 8
    if urgencia == "expressa":
        base = base * 1.5
    if base > 60:
        base = 60
    if seguro:
        base += 5
    return round(base, 2)


def frete(peso, urgencia, seguro, regiao):
    """Versao corrigida."""
    base = {"leve": 10, "medio": 20, "pesado": 40}[peso]
    if regiao == "norte":
        base += 8
    if urgencia == "expressa":
        base = base * 1.5
    if seguro:
        base += 5
    return round(base, 2)


def esperado(peso, urgencia, seguro, regiao):
    valor = {"leve": 10, "medio": 20, "pesado": 40}[peso]
    if regiao == "norte":
        valor += 8
    if urgencia == "expressa":
        valor *= 1.5
    if seguro:
        valor += 5
    return round(valor, 2)


PAIRWISE = [tuple(c) for c in AllPairs(PARAMS)]
COMPLETO = list(product(*PARAMS))


@pytest.mark.parametrize("caso", PAIRWISE, ids=str)
def test_frete_pairwise(caso):
    assert frete(*caso) == esperado(*caso)


@pytest.mark.parametrize("caso", COMPLETO, ids=str)
def test_frete_completo(caso):
    assert frete(*caso) == esperado(*caso)


def test_original_falhas_no_pairwise():
    falhas = [c for c in PAIRWISE if frete_original(*c) != esperado(*c)]
    assert len(falhas) == 1
    assert all(c[0] == "leve" and c[3] == "norte" for c in falhas)


def test_original_falhas_no_completo():
    falhas = [c for c in COMPLETO if frete_original(*c) != esperado(*c)]
    assert len(falhas) == 6
    # o defeito do teto (grau 3) so aparece no produto completo
    assert any(c[0] == "pesado" and c[1] == "expressa" and c[3] == "norte" for c in falhas)