def retirar_do_estoque(estoque_atual, quantidade):
    if quantidade > estoque_atual:
        raise ValueError("quantidade insuficiente em estoque")
    else:
        return estoque_atual - quantidade
