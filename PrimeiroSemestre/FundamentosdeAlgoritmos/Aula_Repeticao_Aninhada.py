'''
EX - 1
Faça um programa que permita imprimir apenas as bordas de um
retângulo. O programa recebe dois números inteiros L > 0 e
C > 0 que representam o número de linhas e número de colunas do
retângulo.

'''

'''

k = 1

while k == 1:
    linhas = int(input("Digite o Numero de Linhas: "))
    colunas = int(input("Digite o Numero de colunas: "))
    if linhas > 0 and colunas > 0:
        k = 2

    for i in range(linhas):
        for j in range(colunas):
            if i == 0 or i == linhas-1 or j == 0 or j == colunas-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
'''
"""
EX - 2

Faça um programa que permita imprimir uma representação de um
tabuleiro quadrado de xadrez.

"""

'''

k = 1

while k == 1:
    tamanho = int(input("Digite o tamanho do tabuleiro: "))
    if tamanho > 0:
        k = 2

    #suponha que tamanho valha 4
    for i in range(tamanho):
        for j in range(tamanho):
            if i %2==0:
                if j%2 ==0:
                    print("*", end="")
                else:
                    print("o", end="")
            else:
                if j%2 ==0:
                    print("o", end="")
                else:
                    print("*", end="")

        print()



'''
"""
EX - 3
Faça um programa que permita imprimir uma representação de uma
tabela quadrada com o seguinte padrão:

@@@@
$@@@
$$@@
$$$@

"""
'''
k = 1

while k == 1:
    tamanho = int(input("Digite o tamanho do tabuleiro: "))
    if tamanho > 0:
        k = 2

    #suponha que tamanho valha 5
    for i in range(tamanho):
        for j in range(tamanho):
            if j<i:
                print("@", end="")
            else:
                print("$", end="")
        print()

'''
""" 
EX - 4
Faça um programa que permita imprimir uma representação de uma
tabela quadrada com o seguinte padrão:

$&$&
%#%#
$&$&
%#%#

"""

'''

k = 1

while k == 1:
    tamanho = int(input("Digite o tamanho da tabela: "))
    if tamanho > 0:
        k = 2

for i in range(tamanho):
    for j in range(tamanho):
        if i%2==0:
            if j%2==0:
                print("$ ", end="")
            else:
                print("& ", end="")
        else:
            if j%2==0:
                print("% ", end="")
            else:
                print("# ", end="")
    print()

'''
"""
EX - 5
Crie um programa que leia um número natural positivo N e
determine quantos dígitos este número possui.
Entrada:
O programa recebe um número inteiro, N, maior que zero.
Saída:
O programa deve imprimir o número de dígitos de N.

"""
'''
k = 0
digitos = 0

while k ==0:
    N = int(input("Digite um numero:"))
    if N>0:
        k = 1

#10


while N != 0:
    digitos +=1
    N = N//10

print(digitos)
'''

"""
EX 6-
Crie um programa que permita verificar se um número pertence à
sequência de Fibonacci.

Entrada:
O programa recebe um número inteiro maior ou igual a zero.

Saída:
O programa deve imprimir “Verdadeiro” (sem aspas) se o número
dado como entrada pertence à sequência de Fibonacci, caso
contrário deve imprimir “Falso” (sem aspas).

Exemplos:
Entrada Saída
55 Verdadeiro
4000 Falso
4181 Verdadeiro
0 Verdadeiro
20 Falso

"""

