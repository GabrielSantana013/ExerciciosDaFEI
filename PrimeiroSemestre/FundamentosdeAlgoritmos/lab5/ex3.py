"""

Faça um programa que receba um número inteiro maior que 1 e 
verifique se o número fornecido é primo ou não. 
Mostre uma mensagem de número primo ou de número não primo. 
Um número é primo quando é divisível apenas pelo número um e por ele mesmo.

"""
contaPrimo = 0

x = 1
while x==1:
    N = int(input("Digite o número desejado: "))
    if N > 1:
        x = 2
    if x!=1:
        break


for i in range (1,N+1):
    if(N%i ==0):
        contaPrimo +=1

if contaPrimo ==2:
    print("Número primo")
else:
    print("Número não primo")