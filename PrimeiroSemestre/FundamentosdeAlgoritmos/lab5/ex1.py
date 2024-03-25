"""

Escreva um programa que leia um valor inteiro n, onde n
 é a quantidade de linhas de saída que serão apresentadas na execução do programa.

A saída do programa deve ser feita seguindo o padrão dos exemplos fornecidos.

1 1 1
2 4 8
3 9 27


"""
n = int(input("Digite a quantidade de linhas: "))
from math import pow

for i in range (1,n+1):
    for j in range (1,4):
        print(f"{int(pow(i,j))} ", end="")
    print(" ")

    '''
    1
    1 2 3
    2
    1 2 3
    3
    1 2 3 
    
    
    '''