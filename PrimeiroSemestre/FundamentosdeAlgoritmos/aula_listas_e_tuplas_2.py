"""

concatenação de listas:

l1 = [1,2,3]
l2 = [4,5]
l3 = l1+l2
print(l3) #saida: [1,2,3,4,5]

concatenação de listas vazias:

l1 = ["Olá", "Mundo"]
novaLista = l1+ []
print(novaLista) #saida: ["Olá", "Mundo"]

concatenação de varias listas:

l1 = [1,2,3]
l2 = [4,5]
l3 = [6,7]
l4 = l1+l2+l3
print(l3) #saida: [1,2,3,4,5,6,7]

concatenar usando o .extend()

l1 = [1,2]
l2 = [3,4]

l1.extend(l2)
print(l1) #saida: [1,2,3,4]

repetição de listas:

l1 = ["maca","banana"]
l2 = l1*3
print(l2) #saida: ["maca","banana","maca","banana","maca","banana"]

map(): aplica uma fução à todos os elementos da lista

def quadrado(num):
    return num*num

numeros = [1,2,3,4]
quadrado_numeros = map(quadrado,numeros)
print(list(quadrado_numeros)) #saida = [1,4,9,16]

filter(); Filra os elementos de uma lista com base em uma condição

def eh_par(num):
    return num % 2 == 0
numeros = [1,2,3,4,5,6]
numeros_pares = filter(eh_par, numeros)
print(list(numeros_pares)) # saida: [2,4,6]

 Filtrando palavras longas:
 palavras = ["maçã", "banana", "abacaxi", "uva"]
 def is_long_word(word):
 return len(word) > 6

 palavras_longas = filter(is_long_word, palavras)
 print(list(palavras_longas)) # Saída: ["pineapple"]


"""

"""
ex 1 - Faça um programa que leia uma quantidade indeterminada de números
positivos e conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá
terminar quando for lido um número negativo.
"""

'''
contador025 = 0
contador2650 = 0
contador5175 = 0
contador76100 = 0

l1 = []
l2 = []
l3 = []
l4 = []

x = 1
while x > 0:
    x = int(input("Digite um número: "))
    if x > 0 and x<=25:
        contador025 +=1
        l1.append(x)
    elif x > 25 and x<=50:
        contador2650 +=1
        l2.append(x)
    elif x > 50 and x<=75:
        contador5175 +=1
        l3.append(x)
    elif x > 75 and x<=100:
        contador76100 +=1
        l4.append(x)
print(l1,contador025)
print(l2,contador2650)
print(l3,contador5175)
print(l4,contador76100)
'''

"""
2- Uma empresa de pesquisas precisa tabular os resultados da seguinte
enquete feita a um grande quantidade de organizações: "Qual o melhor
Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado
da enquete e informe ao final o resultado da mesma. O programa
deverá ler os valores até ser informado o valor 0, que encerra a
entrada dos dados. Não deverão ser aceitos valores além dos válidos
para o programa (0 a 6). Os valores referentes a cada uma das opções
devem ser armazenados num vetor. Após os dados terem sido
completamente informados, o programa deverá calcular a percentual de
cada um dos concorrentes e informar o vencedor da enquete. O formato
da saída foi dado pela empresa, e é o seguinte:

"""

'''
x = 1
l = [0,0,0,0,0,0]
ws = 0
unix = 0
linux = 0
netware = 0
macos = 0
outro = 0



while x != 0:
    x = int(input(""))

    if x == 1:
        l[0] +=1
    elif x == 2:
        l[1] +=1
    elif x == 3:
        l[2] += 1
    elif x == 4:
        l[3] += 1
    elif x == 5:
        l[4] += 1
    elif x == 6:
        l[5] += 1

total = 0
for i in l:
    total +=i

print(total)

print("Sistema Operacional          Votos     %")
print("-------------------          -----     ---")
print(f"Windows Server                {l[0]}          {int((l[0]/total*100))}%")
print(f"Unix                          {l[1]}          {int(l[1]/total*100)}%")
print(f"Linux                         {l[2]}          {int(l[2]/total*100)}%")
print(f"Netware                       {l[3]}          {int(l[3]/total*100)}%")
print(f"Mac Os                        {l[4]}          {int(l[4]/total*100)}%")
print(f"Outro                         {l[5]}          {int(l[5]/total*100)}%")

print(f"Total                         {total}")

'''

"""
Ex 3 - Usando funções Lambda:
Pegue duas listas, digamos, por exemplo, estas duas:
1 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
2 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e escreva um programa que retorne uma lista que contenha apenas os
elementos comuns entre as listas. Certifique-se de que seu programa
funcione em duas listas de tamanhos diferentes. Escreva isso em uma
linha de Python usando pelo menos uma compreensão de lista.

"""

'''
a = []
b = []

print("digite os elementos da lista A, e digite 'x' pra sair:")

x = input("")
while x != 'x':
    a.append(int(x))
    x = input("")

print("digite os elementos da lista B, e digite 'x' pra sair:")

x = input("")
while x != 'x':
    b.append(int(x))
    x = input("")

palavrasComuns = filter(lambda z: z in b, a)

print(list(palavrasComuns))
'''

"""
Ex 4- Faça um jogo em que o jogador deva adivinhar a palavra “EVAPARAR”.
Para este exercício, escreva a lógica que pede ao jogador para
adivinhar uma letra e exibe as letras da palavra-chave que foram
adivinhadas corretamente. Por enquanto, deixe o jogador adivinhar um
número infinito de vezes até obter a palavra inteira. Como bônus,
acompanhe as letras que o jogador adivinhou e exiba uma mensagem
diferente se o jogador tentar adivinhar a letra novamente. Lembre-se
de parar o jogo quando todas as letras forem adivinhadas
corretamente!

Um exemplo de interação pode ser assim:
1 _ _ _ _ _ _ _ _ _
2 >>> Adivinhe sua letra: S
3 Incorreta!
4 >>> Adivinhe sua letra: E
5 E _ _ _ _ _ _ _ E
6 ...
E assim por diante, até que o jogador receba a palavra.


"""

'''
palavra = ["E","V","A","P","O","R","A","R"]
letrasAdivinhadas = ['_']*len(palavra)

while letrasAdivinhadas != palavra:
    print("Adivinhe sua letra: ")
    letra = input("")
    for i in range(len(palavra)):
        if letra == palavra[i]:
            letrasAdivinhadas[i] = letra
    print(*letrasAdivinhadas) # o * tira o apóstrofe e as vírgulas
'''

"""
Ex 5 -
Problema: Contagem de Elementos Únicos
Você deve escrever uma função em Python chamada count_unique_elements
que recebe uma lista de inteiros e retorna o número de elementos
únicos nessa lista.
Detalhes:
A função deve lidar com listas de qualquer tamanho, incluindo listas
vazias. Elementos únicos são aqueles que aparecem exatamente uma vez
na lista. Exemplo:

 Entrada: [1, 2, 2, 3, 4, 4, 5]

 Saída: 3 (Os elementos únicos são 1, 3 e 5.)

"""
'''
def cout_unique_elements(l):
    listaUnicos = []
    for i in range (len(l)):
        if l[i] in listaUnicos:
            listaUnicos.pop()
        else:
            listaUnicos.append(l[i])
    return listaUnicos

l = []


print("Digite os elementos da lista. 'x' para.")
x = input("")
while x !='x':
    l.append(x)
    x = input("")

print(len(cout_unique_elements(l)))

'''

"""
6 - Escreva uma função Python para encontrar o segundo maior elemento em
uma lista.

"""
'''
def maiorNum(l):
    maior = 0
    maior2 = 0
    for i in range(len(l)):
        if i == 0:
            maior = l[i]
        elif maior < l[i]:
            maior2 = maior
            maior = l[i]
    return maior2

l = []
print("Digite os elmentos da lista. 'x' para.")
x = input("")
while x != 'x':
    l.append(int(x))
    x = input("")
print(maiorNum(l))
'''