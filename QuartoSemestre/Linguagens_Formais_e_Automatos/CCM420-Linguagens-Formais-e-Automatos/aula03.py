transicao = {}

estados = list(input().split())
inicial = input()
aceitacao = input()
alfabeto = list(input().split())


for i in range(0,len(estados)):
    linha_transicao = list(input().split())
    transicao.update({linha_transicao[0]:{alfabeto[0]:linha_transicao[1], alfabeto[1]:linha_transicao[2]}})
palavra = list(input().split())
atual = inicial

for p in palavra:
    for c in p:
        if c not in alfabeto:
            atual = None
            break
        atual = transicao[atual][c]
    if atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")
    atual = inicial