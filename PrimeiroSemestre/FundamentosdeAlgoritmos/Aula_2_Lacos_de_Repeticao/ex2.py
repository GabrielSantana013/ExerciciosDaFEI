"""
Faça um programa que leia um valor N inteiro e positivo,
calcule e mostre o valor de E, conforme a fórmula a seguir: 

E = 1 + 1/1 + 1/2 + 1/3 + ... + 1/N

"""

n = int(input("Digite o número desejado: "))

i = 1
E = 1

while(i <= n):

    E += 1/i
    i +=1

print(f"{E:.3f}")