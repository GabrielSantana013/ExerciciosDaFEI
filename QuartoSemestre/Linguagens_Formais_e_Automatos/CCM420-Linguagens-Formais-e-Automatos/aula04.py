transicao = {}
estados = list(input().split())
alfabeto = list(input().split())
inicial = input()
aceitacao = input().split()

# Lendo as transições
for i in range(len(estados)):
    linha_transicao = list(input().split())
    estado = linha_transicao[0]
    
    # Criando dicionário de transições para este estado
    transicoes_estado = {}
    
    # Transições para símbolos do alfabeto
    for j in range(len(alfabeto)):
        simbolo = alfabeto[j]
        destinos = linha_transicao[1+j].split(',') if linha_transicao[1+j] != 'vazio' else []
        transicoes_estado[simbolo] = destinos
    
    # Transição vazia (ε)
    trans_vazia = linha_transicao[-1].split(',') if linha_transicao[-1] != 'vazio' else []
    transicoes_estado['ε'] = trans_vazia
    
    transicao[estado] = transicoes_estado

palavra = input()

# Função para calcular o fecho-ε de uma lista de estados (mantendo duplicatas)
def fecho_epsilon(estados_atual):
    resultado = estados_atual.copy()
    pilha = estados_atual.copy()
    
    while pilha:
        estado = pilha.pop()
        for prox_estado in transicao[estado]['ε']:
            resultado.append(prox_estado)
            pilha.append(prox_estado)
    
    return sorted(resultado)

# Estado inicial com fecho-ε
atual = fecho_epsilon([inicial])
print(atual)

# Processando a palavra
for c in palavra:
    if c not in alfabeto:
        atual = []
        break
    
    print(c)
    
    # Calcular próximo conjunto de estados (sem fecho-ε ainda)
    proximo = []
    for estado in atual:
        for destino in transicao[estado].get(c, []):
            proximo.append(destino)
    
    # Aplicar fecho-ε ao próximo conjunto
    atual = fecho_epsilon(proximo)
    print(atual)

# Verificar aceitação (agora verificamos se algum estado está em aceitacao, mesmo com duplicatas)
aceito = False
for estado in atual:
    if estado in aceitacao:
        aceito = True
        break

if aceito:
    print("aceita")
else:
    print("rejeita")