"""
Ex-1
Crie uma função que calcule a média de dois números
▶ Sua função deve receber dois números como parâmetros de entrada
▶ Deve imprimir o resultado da média

"""

'''
def media(n1, n2):
    resultado = (n1+n2)/2
    print(resultado)

n1 = int(input("Digite o N1: "))
n2 = int(input("Digite o N2: "))
media(n1, n2)

'''

"""
Ex-2
Adapte a função para calcular a média criada anteriormente.
▶ Faça com que ela retorne o resultado da média para o chamador da
função.

"""
'''
def media(n1, n2):
    resultado = (n1+n2)/2
    return resultado


n1 = int(input("Digite o N1: "))
n2 = int(input("Digite o N2: "))
retorno = media(n1, n2)
print(retorno)
'''

"""
Ex-3
Escreva uma função com parâmetros que retorne o maior de dois
números.
▶ A função deve se chamar maximo(x, y)

"""
'''
def maximo (x, y):
    return x if x>y else y

retorno = maximo(3,2)
print(retorno)
'''

"""
Ex-4
Escreva uma função com parâmetros chamada multiplo(x, y).
▶ Esta função deve receber dois números
▶ Retornar True se o primeiro for múltiplo do segundo número;
▶ Retornar False caso contrário.

"""
'''
def multiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False


n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))

print(multiplo(n1,n2))
'''

"""
Ex-5
Escreva uma função com parâmetros que:
▶ Receba a base e a altura de um triângulo e retorne sua área

"""
'''
def area(b, h):
    return (b*h)/2


n1 = int(input("Digite a base do triângulo: "))
n2 = int(input("Digite a altura do triângulo: "))
print(area(n1,n2))
'''

"""
Ex 6-Faça um programa que:
▶ Leia três números e apresente o resultado do seguinte cálculo:

raiz(n1)+raiz(n2)+raiz(n3)+raiz(n1+n2)/2+raiz(n2+n3)/2+raiz(n1+n3)/2
"""

'''
from math import sqrt

def calculo(n1, n2, n3):
    return sqrt(n1)+sqrt(n2)+sqrt(n3)+(sqrt(n1+n2)/2)+(sqrt(n2+n3)/2)+(sqrt(n1+n3)/2)

n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
n3 = int(input("Digite o terceir número"))

print(f"{calculo(n1,n2,n3):.2f}")
'''

"""
Ex 7- Existem restrições para que uma pessoa possa doar sangue. Uma
delas é relativa ao peso. Mulheres tem que pesar no mínimo
50kg e homens no mínimo 60kg. Faça uma função para informar
se uma pessoa está ou não apta a doar sangue sabendo seu sexo
e seu peso.

O programa principal deve ler as entradas, acionar a função e
exibir a resposta.

"""
'''
def doador(sexo, peso):

    if sexo == 'M' and peso >= 60:
        return "apto"
    elif sexo == 'M' and peso <60:
        return "não apto"

    elif sexo == 'F' and peso >= 50:
        return "apto"
    else:
        return "não apto"

sexo = input("Digite o sexo (M) ou (F): ")
peso = int(input("Digite seu peso: "))

print(doador(sexo, peso))

'''

"""
Ex 8- 
Uma data é considerada mágica quando o dia multiplicado pelo
mês é igual ao ano de dois dígitos.

Por exemplo, 10 de junho de 1960 é uma data mágica porque
junho é o sexto mês e 6 vezes 10 é 60, o que equivale ao ano
de dois dígitos.

Escreva uma função que determine se uma data é ou não uma data
mágica.

"""
'''
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

def anoMagico(dia, mes, ano):
    if ano%100 == dia*mes:
        print(f"Data Mágica {dia}/{mes}/{ano}")
    else:
        print("Não é uma data mágica.")

anoMagico(dia,mes,ano)
'''

"""
Ex 10 -
Use a função criada no exercício anterior
Exiba todas as datas mágicas do século XX.
Ou seja, do ano 1901 à 2000
"""

'''
def anoMagico(dia, mes, ano):
    if ano%100 == dia*mes:
        print(f"Data Mágica {dia}/{mes}/{ano}")

for k in range (1901,2001):
    for i in range (1,13):
        for j in range(1,31):
            anoMagico(j,i,k)
'''

"""
Ex 10 -

Refaça os exercícios 3, 4, e 5 utilizando função lambda

No Python, podemos criar funções simples em somente uma linha
Estas funções, ou expressões, são chamadas de lambda
Sintaxe:
<nome_da_função> = lambda <parâmetros> : <expressão>
"""
'''

maximo = lambda x,y: x>y
print(maximo(3,2))

multiplo = lambda x,y: x%y == 0
print(multiplo(10,2))

area = lambda b,h: (b*h)/2
print(area(10,5))
'''

"""
Ex 11-
Faça uma função que receba quatro valores: I, A, B e C.
Destes valores, I é um valor inteiro valendo 1, 2 ou 3. A, B
e C são valores reais. Escreva os números A, B e C obedecendo
à tabela a seguir, dependendo do valor de I
"""
'''
def ordem(i, a, b, c):
    if i == 1:
        if a > b:
            a = a ^ b
            b = a ^ b
            a = a ^ b
        else:
            b = a ^ b
            a = a ^ b
            b = a ^ b
        if b > c:
            b = b ^ c
            c = b ^ c
            b = b ^ c
        else:
            c = b ^ c
            b = b ^ c
            c = b ^ c

    elif i == 2:
        if a<b:
            a = a^b
            b = a^b
            a = a^b
        if b<c:
            c = c^b
            b = c^b
            c = c^b

    elif i == 3:
        if a > b:
            b = a ^ b
            a = a ^ b
            b = a ^ b

        if c > b:
            b = c ^ b
            c = c ^ b
            b = c ^ b


    print(a, b, c)

ordem(3,10,2,5)
'''

"""
Ex 12 - 
Escreva uma função que calcula o quociente e o resto da
divisão inteira entre dois números. Utilize apenas as
operações de soma e subtração para calcular o resultado.
Dica: utilize uma estrutura de repetição para isso.
Faça um programa principal que recebe o dividendo e o divisor
do usuário e, depois de chamar a função, exibe o quociente e o
resto.

"""
'''
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

def calculo(dividendo, divisor):
    quociente = 0
    resto = dividendo
    while True:
        resto -= divisor
        quociente += 1
        if resto <= divisor: break
    print(quociente, resto)
calculo(dividendo,divisor)

'''

"""
Ex 13 - Escreva uma função chamada exponencial que recebe um valor n
como parâmetro. Sua função deve encontrar e retornar b e k tal
que b
k = n e b seja o menor possível.

"""
'''

from math import pow

n = int(input("Digite o valor de n: "))

def exponencial(n):
    k = 1
    b = 2
    while True:
        if pow(b,k) < n:
            k+=1

        elif pow(b,k) > n:
            k = 0
            b +=1
        else:
            return b, k

print(exponencial(n))
'''