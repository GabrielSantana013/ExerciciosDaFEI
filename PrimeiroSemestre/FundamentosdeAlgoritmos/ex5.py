"""
Faça um programa que receba valores do teclado até o usuário digitar zero
e imprima a soma de todos os valores digitados.

"""
acumulado = 0
n = int(input())
while(n != 0):
    acumulado += n
    n = int(input())

print(f"Resultado: {acumulado}")