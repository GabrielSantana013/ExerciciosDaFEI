class SaldoInsuficienteError(Exception):
    """Exceção gerada quando o saque ultrapassa o saldo disponível."""
    pass


class CarteiraDigital:
    def __init__(self, saldo_inicial=0, log_path="carteira.log"):
        self.saldo = saldo_inicial
        self.log_path = log_path

    def depositar(self, valor):
        self.saldo = self.saldo + valor

        with open(self.log_path, "a") as arquivo:
            arquivo.write(f"deposito:{valor}\n")

    def sacar(self, valor):
        saldo_atual = self.saldo

        if valor > saldo_atual:
            raise SaldoInsuficienteError("saldo insuficiente")

        self.saldo = saldo_atual - valor


def classificar_transacao(valor):
    """
    Classifica a transação conforme seu valor:
    abaixo de 100: pequena
    de 100 até 999.99...: media
    1000 ou mais: grande
    """
    if valor < 100:
        categoria = "pequena"
    elif valor < 1000:
        categoria = "media"
    else:
        categoria = "grande"

    return categoria


def transferir(origem, destino, valor):
    origem.sacar(valor)
    destino.depositar(valor)
