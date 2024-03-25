"""

Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, 
inclusive N, se for o caso.

Entrada
A entrada contém um valor inteiro N (5 < N < 2000).

Saída
Imprima o quadrado de cada um dos valores pares, de 1 até N, 
conforme o exemplo abaixo.

Input: 6

Result: 2^2=4
        4^2=16
        6^2=36

"""

N = int(input())

for i in range(1,N+1):
    if i%2 ==0:
        print(f"{i}^2 = {i*i}")