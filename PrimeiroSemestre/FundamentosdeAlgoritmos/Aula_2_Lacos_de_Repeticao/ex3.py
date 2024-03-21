"""
O Máximo Divisor Comum (MDC) de dois números inteiros positivos,
n e m, é o maior número, d, que divide de forma inteira n e m.
Existem vários algoritmos que podem ser usados para resolver esse problema,
incluindo: 
 
 Inicialize d para ser o menor número entre M e N.

Enquanto d não dividir m e n de forma inteira faça
    diminua o valor de d em 1

relate d como o maior divisor comum de n e m.

 
Utilize o pseudocódigo acima para fazer um programa em Python que
leia dois números inteiros positivos do usuário,
determina e reporta o maior divisor comum entre eles.
"""

n = int(input("Digite n: "))
m = int(input("Digite m: "))

if n > m:
    d = m
else:
    d = n


while(d > 0):
    if (m%d == 0) and (n%d == 0):
        break
    d -=1

print(d)