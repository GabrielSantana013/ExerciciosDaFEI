# listas e tuplas!!

"""
L = [] //é uma lista vazia (no caso, L é um ponteiro que aponta pra lista)

L= [4, 'b', 3.2, True] lista preenchida (pode ser homo ou hetero)

pode mudar pelo índice:

L= [2,3,4]
L[0]= 8
L= [8,3,4]

usar o .append adiciona um elemento no fim da lista, ex:

L= [2,3,4]
L.append(8)
L= [2,3,4,8]

ou usar o .insert(indice) para adicionar de acordo com o índice

L= [2,3,4]
L.insert(1,8)
L= [2,8,3,4]

também podemos usar o .pop(indice) para remover um elemento da lista.

L= [2,3,4]
L.pop(1)
L= [2,3,4]

tambem podemos usar o .remove para remover um elemento específico da lista.

L= [2,3,4]
L.remove(3)
L= [2,4]

podemos usar o len(lista) para descobrir o tamanho da lista.

L= [2,3,4]
len(L)

3


podemos procurar um elemento com um for ou while:


z = ['a','b','c']

for elemento in z:
    if elemento == c:
        print("Encontrado")
        break
else:
    print("Não encontrado")
------------------------------
também pode ser assim:

z = ['a','b','c']
    if 'c' in z:
        print("encontrado")
    else:
        print("n encontrado")
------------------------------

para saber o índice daquele elemento:

z = ['a','b','c']
for indice in range(len(z)):
    if z[indice] == 'c':
        print("Encontrado no indice %d" %indice)
        break
else:
    print("elemento n encontrado")
--------------------------------------------------

Também da pra fazer slicing, pegas só os elementos da lista em um intervalo:

p = [42,13,82,63,80,90]
print(p[0:5]) = 42,13,82,80

pode usar tbm
p[:4]
p[-1] (isso inverte a lista, pega o ultimo elemento)


pra copiar lista:

z1 = z[:]

tuplas é igual lista, só muda que tem o () e são imutáveis


"""

#Exercícios!


"""
Ex 1 - Faça um programa que:

▶ Leia 5 valores do usuário e armazene-os em uma lista
▶ Imprima a lista completa
▶ Imprima o primeiro e o último elemento da lista
"""

'''
L = []

for i in range (1,6):
    a = input("Digite um elemento para a lista: ")
    L.append(a)
print(L)
print(L[0],L[4])
'''

"""
Ex 2 - Faça um programa que:
▶ Mostre o menor valor dentro da lista T = [11, 7, 2, 4]

"""
'''
menor = 0

T = [11, 7, 2, 4]
for i in range(len(T)):
    if i == 0:
        menor = T[i]
        
    if T[i] <= menor:
         menor = T[i]
        
print(menor)

'''

"""
Ex 3 - Faça um programa que:
▶ Peça 10 números reais do usuário.
▶ Armazene-os em uma lista e diga qual o índice do maior e seu
valor
"""

'''
indiceMaior = 0

L = []

for i in range (10):
    n1 = (float(input("Digite um numero real: ")))
    L.append(n1)
    if i == 0:
        indiceMaior = i
    if L[i] > L[indiceMaior]:
        indiceMaior = i
print(f"Numeros: {L}")
print(f"Maior numero: {L[indiceMaior]}")
print(f"Indice do maior numero: {indiceMaior}")
'''


"""
Ex 4-Faça um programa para criar uma lista de 10 elementos do
usuário e aprsente:
▶ a soma dos elementos pares
▶ a soma dos elementos de índice par
"""

'''
L = []
somaPar = 0
somaIndice = 0

for i in range (10):
    L.append(int(input("Digite um numero: ")))
    if L[i]%2 == 0:
        somaPar += L[i]
    if i%2 ==0:
        somaIndice += L[i]

print(f"Numeros: {L}")
print(f"Soma dos elementos pares: {somaPar}")
print(f"Soma dos indices pares: {somaIndice}")
'''

"""
Ex 5- Faça um programa que:
▶ Imprime uma sequência de n números em ordem inversa à da leitura
▶ Utilize uma lista para isso.
"""
'''
L = []
qtd = 0

qtd = int(input("Digite a qtde de numeros: "))

for i in range (qtd):
    L.append(int(input("Digite um número: ")))
print(L)
print("Inverso:")
for i in range ((qtd-1),-1,-1):
    print(L[i])
'''

"""
Ex 6- Faça um programa para criar uma lista de 10 elementos inteiros
▶ Mostre todos os elementos que forem maiores que a soma de dois
de seus antecessores
"""

'''
L = []
for i in range(10):
    L.append(int(input("Digite um numero: ")))
print(L)
for i in range(10):
    if i>=2 and L[i-2] + L[i-1] < L[i]:
        print(L[i])
'''

"""
Ex 7 - As temperaturas de uma cidade foram armazenadas na lista
temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprime a menor e a maior temperatura
E imprima também a média das temperaturas
Exemplo de execução
"""
'''
menorTemp = 0
maiorTemp = 0
tempTotal = 0
L = [-10, -8, 0, 1, 2, 5, -2, -4]
for i in range(len(L)):
    if L[i] > maiorTemp:
        maiorTemp = L[i]
    if L[i] < menorTemp:
        menorTemp = L[i]
    tempTotal += L[i]
print(f"Maior: {maiorTemp}")
print(f"Menor: {menorTemp}")
print(f"Média: {tempTotal/len(L)}")
'''

"""

Ex 8 - Neste exercício, você criará um programa que lê palavras do
usuário até que o usuário entre com uma linha em branco.
Após o usuário digitar uma linha em branco, seu programa deve
exibir cada palavra digitada pelo usuário exatamente uma vez.
As palavras devem ser exibidas na mesma ordem em que foram
inseridas.
"""
'''
L = []
frase = ""
while True:
    frase = (input("Digite uma palavra: "))

    if frase == "":
        break
    elif frase not in L:
        L.append(frase)

print("Palavras digitadas: ")
for i in range(len(L)):
    print(L[i])
'''