"""

Ex 1 - Escreva uma função que tenha os comprimentos dos dois lados mais curtos de um triângulo retângulo como seus parâmetros.
Retorne a hipotenusa do triângulo, calculada usando o teorema de Pitágoras, como o resultado da função.
Inclua um programa principal que lê os comprimentos dos lados mais curtos de um triângulo retângulo do usuário e use sua
 função para calcular o comprimento da hipotenusa. Exiba o resultado.

"""

'''
from math import pow
from math import sqrt

n1 = int(input("Digite o primeiro lado do triângulo: "))
n2 = int(input("Digite o segundo lado do triângulo: "))

def hipotenusa(n1, n2):
    h = pow(n1,2)+pow(n2,2)
    return sqrt(h)

print(f"Hipotenusa: {float(hipotenusa(n1,n2)):.2f}")

'''

"""

Ex 2 - Crie uma função para calcular e retornar o peso de uma pessoa nos outros planetas do Sistema Solar. 
A função deve ter dois parâmetros: o planeta desejado e o peso em Kg da pessoa na Terra. 
O programa principal deve receber o peso da pessoa na Terra (em Kg) e o planeta desejado.

Relação de pesos: 1 Kg na Terra equivale a: 0.37 Kg em Mercúrio; 0.88 Kg em Vênus; 0.38 Kg em Marte;
 2.64 Kg em Júpiter; 1.15 Kg em Saturno; 1.17 Kg em Urano; e 1.18 Kg em Netuno.  

"""
'''
nome = input("Digite o o nome do planeta desejado: ")
peso = float(input("Digite o peso da pessoa na Terra em kg: "))

def pesoPlanetas(nome, peso):
    if nome == "Vênus":
        peso = peso * 0.88
        print(f"Peso em {nome}: {peso:.2f}")
    elif nome == "Mercúrio":
        peso = peso*0.37
        print(f"Peso em {nome}: {peso:.2f}")
    elif nome == "Marte":
        peso = peso*0.38
        print(f"Peso em {nome}: {peso:.2f}")
    elif nome == "Júpiter":
        peso =  peso*2.64
        print(f"Peso em {nome}: {peso:.2f}")
    elif nome == "Saturno":
        peso = peso*1.15
        print(f"Peso em {nome}: {peso:.2f}")
    elif nome == "Urano":
        peso = peso*1.17
        print(f"Peso em {nome}: {peso:.2f}")
    elif nome == "Netuno":
        peso = peso*1.18
        print(f"Peso em {nome}: {peso:.2f}")


pesoPlanetas(nome,peso)
'''

"""
Ex 3 - Escreva uma função, test_prime() que recebe um número e verifica se ele é primo ou não.
 A função retorna True ou False. Não é necessário desenvolver o programa principal.

"""
'''
def test_prime(n1):
    contaPrimo = 0
    index = 1

    while index <= n1:
        if n1 % index == 0:
            contaPrimo = contaPrimo+1
            index = index + 1
        else:
            index = index + 1

    if contaPrimo == 2:
        return True
    else:
        return False

test_prime(11)

'''

"""
Ex 4 - Crie uma função chamada produtorio que realize o cálculo do produtório, conforme equação abaixo:

Sua função deverá receber entre 3 e 6 parâmetros e retornar o valor do produtório. Não é necessário fazer o programa principal.

Produtório é a multiplicação de uma sequência de objetos matemáticos (números, funções, vetores, matrizes, etc.).

"""

'''
def produtorio(n1,n2,n3,n4 = 1, n5 = 1, n6 = 1):
    resultado = n1 * n2 * n3 * n4 * n5 * n6
    return resultado
'''

"""
Ex 5 -Em uma determinada jurisdição, as tarifas de táxi consistem em uma tarifa básica de R$ 10.00, mais R$ 0.50 para cada 125 metros percorridos. 
Escreva uma função que considere a distância percorrida (em quilômetros inteiros) como seu único parâmetro e retorne a tarifa total como seu único resultado. 
Escreva um programa principal em que a quantidade de km será digitada e onde a função será chamada.

"""

'''
km = int(input("Digite a quantidade de quilômetros: "))

def tarifa(km):
    mts = (km*1000)/125
    resultado = 10 + (0.5*mts)
    return resultado
print(f"Tarifa {tarifa(km):.2f}")

'''


