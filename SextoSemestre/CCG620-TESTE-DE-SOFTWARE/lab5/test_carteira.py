
import os
import pytest

from carteira import (
    CarteiraDigital,
    SaldoInsuficienteError,
    classificar_transacao,
    transferir,
)

# ---------------------------------------------------------------------------
# 1) Verificação do saldo inicial, adição e retirada de valores
# ---------------------------------------------------------------------------

def test_carteira_inicia_sem_saldo():
    conta = CarteiraDigital()

    assert conta.saldo == 0


def test_carteira_inicia_com_valor_personalizado():
    valor_inicial = 150

    conta = CarteiraDigital(saldo_inicial=valor_inicial)

    assert conta.saldo == 150


def test_adicao_de_dinheiro_atualiza_saldo(tmp_path):
    arquivo_log = tmp_path / "registro.log"
    conta = CarteiraDigital(
        saldo_inicial=100,
        log_path=str(arquivo_log)
    )

    conta.depositar(50)

    assert conta.saldo == 150


def test_retirada_de_dinheiro_reduz_saldo(tmp_path):
    arquivo_log = tmp_path / "registro.log"
    conta = CarteiraDigital(
        saldo_inicial=200,
        log_path=str(arquivo_log)
    )

    conta.sacar(80)

    assert conta.saldo == 120


# ---------------------------------------------------------------------------
# 2) Verificação da exceção SaldoInsuficienteError
# ---------------------------------------------------------------------------

def test_retirada_acima_do_saldo_gera_erro(tmp_path):
    arquivo_log = tmp_path / "registro.log"
    conta = CarteiraDigital(
        saldo_inicial=50,
        log_path=str(arquivo_log)
    )

    with pytest.raises(SaldoInsuficienteError) as informacoes_erro:
        conta.sacar(100)

    assert informacoes_erro.type is SaldoInsuficienteError
    assert str(informacoes_erro.value) == "saldo insuficiente"


def test_saldo_permanece_igual_apos_retirada_invalida(tmp_path):
    arquivo_log = tmp_path / "registro.log"
    conta = CarteiraDigital(
        saldo_inicial=50,
        log_path=str(arquivo_log)
    )

    with pytest.raises(SaldoInsuficienteError):
        conta.sacar(100)

    assert conta.saldo == 50


# ---------------------------------------------------------------------------
# 3) Fixture para preparar e limpar o arquivo de registro
# ---------------------------------------------------------------------------

CAMINHO_LOG = "carteira.log"


@pytest.fixture
def conta_com_registro():
    # Preparação: remove o arquivo de uma execução anterior, se existir
    if os.path.exists(CAMINHO_LOG):
        os.remove(CAMINHO_LOG)

    conta = CarteiraDigital(saldo_inicial=0)

    yield conta

    # Limpeza: remove o arquivo ao finalizar o teste
    if os.path.exists(CAMINHO_LOG):
        os.remove(CAMINHO_LOG)


def test_deposito_registra_operacao_no_arquivo(conta_com_registro):
    conta = conta_com_registro

    conta.depositar(75)

    with open(CAMINHO_LOG, "r") as arquivo:
        registro = arquivo.read()

    assert registro == "deposito:75\n"


# ---------------------------------------------------------------------------
# 4) Teste parametrizado da classificação de valores
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "quantia, classificacao_esperada",
    [
        (0, "pequena"),
        (99, "pequena"),
        (100, "media"),
        (500, "media"),
        (999, "media"),
        (1000, "grande"),
        (1500, "grande"),
    ],
    ids=[
        "zero_classificado_como_pequeno",
        "noventa_e_nove_classificado_como_pequeno",
        "cem_classificado_como_medio",
        "valor_intermediario_classificado_como_medio",
        "novecentos_e_noventa_e_nove_classificado_como_medio",
        "mil_classificado_como_grande",
        "valor_elevado_classificado_como_grande",
    ],
)
def test_categoria_de_uma_quantia(quantia, classificacao_esperada):
    categoria_obtida = classificar_transacao(quantia)

    assert categoria_obtida == classificacao_esperada


# ---------------------------------------------------------------------------
# 5) Testes da operação de transferência entre carteiras
# ---------------------------------------------------------------------------

@pytest.fixture
def contas_para_transferencia(tmp_path):
    """Monta duas carteiras: uma com dinheiro e outra sem saldo."""
    registro_saida = tmp_path / "saida.log"
    registro_entrada = tmp_path / "entrada.log"

    conta_origem = CarteiraDigital(
        saldo_inicial=500,
        log_path=str(registro_saida)
    )

    conta_destino = CarteiraDigital(
        saldo_inicial=0,
        log_path=str(registro_entrada)
    )

    return conta_origem, conta_destino


@pytest.mark.parametrize(
    "quantia_enviada",
    [50, 200, 500],
    ids=[
        "envio_de_quantia_baixa",
        "envio_de_quantia_intermediaria",
        "envio_do_saldo_completo",
    ],
)
def test_envio_de_dinheiro_entre_contas(
    contas_para_transferencia,
    quantia_enviada
):
    conta_origem, conta_destino = contas_para_transferencia

    saldo_inicial_origem = conta_origem.saldo
    saldo_inicial_destino = conta_destino.saldo

    transferir(conta_origem, conta_destino, quantia_enviada)

    assert conta_origem.saldo == saldo_inicial_origem - quantia_enviada
    assert conta_destino.saldo == saldo_inicial_destino + quantia_enviada


def test_transferencia_acima_do_saldo_preserva_as_contas(
    contas_para_transferencia
):
    conta_origem, conta_destino = contas_para_transferencia

    saldo_inicial_origem = conta_origem.saldo
    saldo_inicial_destino = conta_destino.saldo

    quantia_excedente = saldo_inicial_origem + 1000

    with pytest.raises(SaldoInsuficienteError):
        transferir(conta_origem, conta_destino, quantia_excedente)

    assert conta_origem.saldo == saldo_inicial_origem
    assert conta_destino.saldo == saldo_inicial_destino
