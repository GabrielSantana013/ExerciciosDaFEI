"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor de E, conforme a fórmula a seguir: 

E = 1 + 1/1 + 1/2 + 1/3 + ... + 1/N

"""

N = int(input("Digite o número desejado: "))
E = 1

for i in range(1,N+1):
    E += 1/i

print(f"{E:.3f}")
