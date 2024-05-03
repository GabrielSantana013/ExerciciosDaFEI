"""
Exemplos dicionário:

d = {
    <key1>:<value1>,
    <key2>:<value2>,
    <key2>:<value2>,
}

print (d)

ou

d = {
    <key1>:<value1>,
    <key2>:<value2>,
    <key2>:<value2>,
}

print(d[i]) ou print(d[elemento])

metodo .get()

print(d.get(5)) // acha a chave 5 e retorna o elemento correspondente

para adicionar elementos:

d[chave] = "elemento a ser adicionado"

remover elementos:

del d[chave]

método items:

d = d.items()
d = list(d)
print (d) //vai sair igual uma lista

método .keys() printa todas as chaves

d = d.keys()
d = list(d)
print (d)

método .values() // printa os valores, não as chaves

d = d.values()
d = list(d)
print(d)

iteração:

d = {
    'um':'exemplo',
    'dois':'de',
    'tres':'dicionario',
}

for chave in dicionario:
    print(chave)
print()
for valor in dicionario.values():
    print(valor)
"""

#Exercícios!

"""
Ex 1 -
 Escreva uma função chamada procuraChave que encontre todas as chaves,
em um dicionário, que estão associadas a um valor específico.
A função receberá o dicionário e o valor a procurar como seus únicos
parâmetros.
A função retornará uma lista (possivelmente vazia) de chaves
associadas ao valor fornecido.
Faça um programa principal que mostra o funcionamento da função.
Seu programa principal deve criar um dicionário e mostrar que a
função procuraChave funciona corretamente quando retorna várias
chaves, uma única chave ou nenhuma chave.

"""
'''
def procuraChave(Dicionario, value):
    print(f"Procurando chaves com valor {value}")
    L = []
    for chave in Dicionario:
        if Dicionario[chave] == value:
            L.append(chave)
    return L




Dicionario = {'alpha': 1 , 'bravo': 2, 'charlie': 1, 'delta': 3, 'echo': 1}

n1 = int(input("Digite um número para procurar: "))

print(procuraChave(Dicionario, n1))
'''

"""
Ex 2-
Faça um programa que gere 100 números aleatórios
Gere números no intervalo de 0 à 20
Mostre quantas vezes cada número apareceu
Dica:
Utilize um dicionário para armazenar o número como chave
e a quantidade de vezes em que ele aparece como valor
"""

'''
from random import randint

d = {}

for i in range (100):
    num = randint(0,20)
    if num not in d.keys():
        d[num] = 1 #se n existe, adiciona com val 1
    else:
        d[num] += 1 #se existe soma
print(F"Numero: Quantidade")

for chave in d:
    print(f"{chave}:{d[chave]}")
'''

"""
Ex 3-
Neste exercício, você simulará 1000 lançamentos de dois dados.
Comece escrevendo uma função que simula o lançamento de um par de
dados de seis lados cada.
Sua função não deve aceitar nenhum parâmetro.
Ela retornará a somatória obtida pelos dois dados.
Escreva um programa principal que use sua função para simular 1000
lançamentos de dois dados.
Como acontece em alguns programas, você deve contar o número de vezes
que cada somatória acontece.
Em seguida, a função principal deve exibir uma tabela que resume
esses resultados.
Mostre a frequência para cada resultado como uma porcentagem do
número total de lançamentos.

"""

'''
from random import randint

def lancaDados():
    dado1 = randint(1,6)
    dado2 = randint(1, 6)
    return dado1+dado2

d = {}
for i in range (1000):
    num = lancaDados()
    if num not in d.keys():
        d[num] = int(1)
    else:
        d[num] +=int(1)
print("Lançamentos: ")
print (d)
print()
print("Em 1000 lançamentos tivemos as seguintes porcentagens: ")
for chave in d:
    print("%2d" % chave + " : " + f"{d[chave]/10}%")
'''


"""
4-  Crie uma função que retorna o número de caracteres únicos em uma
string criada pelo usuário.
Por exemplo:
“Hello, World!” tem 10 caracteres únicos
enquanto zzz tem somente 1 caractere único.
Use um dicionário para resolver este problema.

"""

'''
entrada = (input("Digite uma palavra: "))
d = {}

cont = 0

for i in range (len(entrada)):
    if entrada[i] not in d:
        d[entrada[i]] = 1
        cont +=1
print(f"A palavra \"{entrada}\" tem {cont} caracteres unicos")
'''

"""
Ex 5 -
Duas palavras são anagramas se contiverem todas as mesmas letras, mas
em uma ordem diferente.
Por exemplo: estante e setenta são anagramas.
Crie uma função que recebe duas strings do usuário e determina se
elas são ou não anagramas.
Utilize dicionário para resolver o problema.
"""

'''
entrada1 = input("Digite uma palavra: ")
entrada2 = input("Digite outra palavra: ")

d1 = {}
d2 = {}

for i in range (len(entrada1)):
    if entrada1[i] not in d1:
        d1[entrada1[i]] = 1
    else:
        d1[entrada1[i]] +=1

for i in range (len(entrada2)):
    if entrada2[i] not in d2:
        d2[entrada2[i]] = 1
    else:
        d2[entrada2[i]] +=1



#Se precisar sortar:
#d1 = dict(sorted (d1.items()))
#d2 = dict(sorted (d2.items()))



if d1 == d2:
    print("São anagramas")
else:
    print("não anagramas")
    
'''

"""
Ex 6 -
Um cartão de bingo consiste de 5 colunas de 5 números. As colunas
são rotuladas com as letras B, I, N, G e O. Existem 15 números que
podem aparecer na coluna de cada letra. Em particular, os números
que podem aparecer na coluna de B estão no intervalo de 1 a 15, os
números que podem aparecer sob o I variam de 16 a 30 e assim por
diante. Escreva uma função que cria um cartão de Bingo com números
aleatórios e armazena tudo em um dicionário. As chaves serão as
letras B, I, N, G e O. Os valores serão as listas de cinco números
que aparecem em cada letra.
"""
'''

from random import randint



BINGO = {}

def cartela(BINGO):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in range(5):
        n1 = randint(1, 15)
        n2 = randint(16, 30)
        n3 = randint(31, 45)
        n4 = randint(46, 60)
        n5 = randint(61, 75)
        if n1 not in l1:
            l1.append(n1)
        else:
            while n1 in l1:
                n1 = randint(1, 15)
            l1.append(n1)
        if n2 not in l2:
            l2.append(n2)
        else:
            while n2 in l2:
                n2 = randint(16, 30)
            l2.append(n2)
        if n3 not in l3:
            l3.append(n3)
        else:
            while n3 in l3:
                n3 = randint(31, 45)
            l3.append(n3)
        if n4 not in l4:
            l4.append(n4)
        else:
            while n4 in l4:
                n4 = randint(46, 60)
            l4.append(n4)
        if n5 not in l5:
            l5.append(n5)
        else:
            while n5 in l5:
                n5 = randint(61, 75)
            l5.append(n5)

    BINGO['B'] = sorted(l1)
    BINGO['I'] = sorted(l2)
    BINGO['N'] = sorted(l3)
    BINGO['G'] = sorted(l4)
    BINGO['O'] = sorted(l5)

cartela(BINGO)
for i in 'BINGO':
    print(i + " : ", BINGO[i])


'''
"""
Ex 7 -
Escreva uma segunda função que exibe o cartão de Bingo com as colunas
identificadas adequadamente.
Use as funções para escrever um programa que exibe um cartão
aleatório. letra.

"""

'''
from random import randint
nomeCartela = input("Digite o nome da cartela: ")

cartela = {}
a= -14
b = 0
def cartelas(cartela,a,b):
    for i in nomeCartela:
        N = []
        a += 15
        b += 15
        for j in range(5):
            n1 = randint(a, b)
            if n1 not in N:
                N.append(n1)
            else:
                while n1 in N:
                    n1 = randint(a, b)
                N.append(n1)

        cartela[i] = N

cartelas(cartela,a,b)

for i in nomeCartela:
    print(i, ": ", cartela[i])
'''
