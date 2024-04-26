from random import randint, random
"""
Ex 1-
Crie 3 listas:
▶ Inteiros: a primeira lista com 10 números inteiros gerados
aleatoriamente
▶ Reais: a segunda lista com 5 números reais gerados aleatoriamente
▶ Strings: A terceira lista com 7 strings criadas por você.
Então adicione as 3 listas a uma lista única, chamada completa.
Apague todas as 3 listas originais.
Acesse e mostre todos os elementos da lista completa.
Use:
from random import randint, random
print(randint(0, 10))
print(random() * 10)

"""
'''
from random import randint, random

l1= []
l2 = []
l3 = ["python", "c", "c++", "gcc", "beecrowd", "java", "javascript", "html", "css", "node"]
lCompleta = []
lCompleta2 = []

for i in range (10):
    x = randint(1,10)
    l1.append(x)
    y = random()*10
    l2.append(y)

lCompleta.append(l1+l2+l3) #cria uma lista dentro da lista
lCompleta2.extend(l1+l2+l3)#deixa uma lista só
l1 = []
l2 = []
l3 = []


print(lCompleta)
print(lCompleta2)
'''

"""
Ex 2 -
Faça um programa que cria uma matriz M 10 X 15, sendo que cada
elemento é um inteiro gerado aleatoriamente.
Então, exiba a matriz completa e, na sequência, somente os elementos
da primeira coluna da matriz.
"""
'''
M = []

for linha in range (10):
    linha=[]
    for coluna in range(15):
        linha.append(randint(1,10))
    M.append(linha)
print("Matriz completa: \n")

for linha in range(len(M)):
    for coluna in range (len(M[linha])):
        print("%4d" % M[linha][coluna], end=" ")
    print()

print("\nPrimeira coluna da matriz: \n")

for linha in range(len(M)):
    for coluna in range (len(M[linha])):
        if coluna == 0:
            print(M[linha][coluna])
'''


"""
Ex 3 -
Faça um programa para receber uma matriz 3 X 3 (solicitar ao usuário)
Apresentar a soma dos elementos da diagonal principal
Exemplo de execução:

"""
'''
M=[]
soma = 0

for linha in range(3):
    linha = []
    for coluna in range(3):
        linha.append(int(input("Digite um numero")))
    M.append(linha)

print("\nMatriz: \n")

for linha in range (len(M)):
    for coluna in range(len(M[linha])):
        if linha == coluna:
            soma += M[linha][coluna]
        print(M[linha][coluna], end=" ")
    print()

print(f"\nSoma da diagonal: {soma}")
'''

"""
Ex 4 -
Solicitar dados de uma matriz 4 X 4
Montar uma lista de 4 elementos com a soma dos elementos ímpares de
cada linha da matriz
Exemplo de execução:
"""
'''
M = []
lImpares = []
imparTotal = 0

for linha in range(4):
    linha = []
    for coluna in range(4):
        linha.append(int(input("Digite um numero: ")))
    M.append(linha)

print("Matriz:")
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if M[linha][coluna] % 2 !=0:
            imparTotal += M[linha][coluna]
        print(f"{M[linha][coluna]}", end = " ")
    lImpares.append(imparTotal)
    imparTotal = 0
    print()

print(f"Lista: {lImpares}")

'''

"""
Ex 5 -
Faça um programa que cria um matriz A 10 X 5 com números inteiros
aleatórios e, então, exiba a matriz transposta de A(At
)
Determinar a transposta de uma matriz é reescrevê-la de forma que
suas linhas e colunas troquem de posições ordenadamente, isto é, a
primeira linha é reescrita como a primeira coluna, a segunda linha é
reescrita como a segunda coluna e assim por diante, até que se
termine de reescrever todas as linhas na forma de coluna.
Exemplo de execução:

"""

'''
M = []
mTransposta = []

for i in range(10):
    i = []
    for j in range(5):
        i.append(randint(1,10))
    M.append(i)

for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end = " ")
    print()

for i in range(5):
    linha = []
    for j in range(10):
        linha.append(M[j][i])
    mTransposta.append(linha)

for i in range(len(mTransposta)):
    for j in range(len(mTransposta[i])):
        print(mTransposta[i][j], end = " ")
    print()
'''

"""
Ex 6-

Cria uma matriz m[12][12] com números inteiros aleatórios.
Em seguida, calcule e mostre a soma ou a média considerando somente
aqueles elementos que estão abaixo da diagonal principal da matriz,
conforme ilustrado abaixo (área verde).
A entrada do programa deve ser um único caractere maiúsculo ’S’ ou
’M’, indicando a operação (Soma ou Média) que deverá ser realizada
com os elementos da matriz.
"""
'''
M = []
somaT = 0
qttNums = 0

for i in range(12):
    i = []
    for j in range(12):
        i.append(randint(1,10))
    M.append(i)

for i in range(len(M)):
    for j in range(len(M[i])):
        if i<j:
            somaT +=M[i][j]
            qttNums+=1
        print(f"{M[i][j]:2d}", end=" ")
    print()

entrada = input("")

if entrada == 's' or entrada == 'S':
    print(f"Soma: {somaT}")
elif entrada == 'm' or entrada == 'M':
    print(f"Media: {somaT/qttNums}")

'''


"""

Ex 7-
Faça um programa que preencha uma matriz 10 X 3 com as notas de 10
alunos com 3 provas (valores gerados de forma aleatória entre 0 e
10).
O programa deverá mostrar:
▶ A matriz com todas as notas de cada aluno.
▶ Um relatório com o número do aluno (número da linha), a prova em que cada
aluno obteve a menor nota (número da coluna) e o valor da menor nota.
▶ O relatório deverá mostrar também qual foi a menor nota obtida em cada
prova e a quantidade de alunos que obtiveram essa menor nota na
respectiva prova.

"""

M = []
menorNota = 0
idx = 0

menorNotaProva = 0
qttAlunos = 0


for i in range(10):
    i = []
    for j in range(3):
        i.append(randint(1,10))
    M.append(i)

for i in range(len(M)):
    for j in range(len(M[i])):
        print(f"{M[i][j]:2d}", end=" ")
    print()

for i in range(len(M)):
    menorNota = M[i][j]
    for j in range(len(M[i])):
        if menorNota > M[i][j]:
            menorNota = M[i][j]
            idx = j
    print(f"Aluno {i} : menor nota: {menorNota}, idx: {idx}\n")

for i in range(3):
    menorNotaProva = M[j][i]
    for j in range(10):
        if menorNotaProva> M[j][i]:
            menorNotaProva = M[j][i]
            qttAlunos = 1
        elif menorNotaProva == M[j][i]:
            qttAlunos+=1


print(f"Menor nota da prova {i} - {menorNotaProva} com essa nota: {qttAlunos}")
