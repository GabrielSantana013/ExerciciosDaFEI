"""
Newton descobriu um método para aproximar os valores das raízes de uma equação numérica.
Esse método é bastante simples e é conhecido como método de Newton.
Escreva um programa que implemente o método de Newton para calcular e exibir a raiz quadrada de um número x digitado pelo usuário.
O algoritmo (pseudocódigo) para o método de Newton é o seguinte:

"""

x = int(input("Digite o número desejado: "))
palpite = x/2
erro = abs((palpite*palpite) - x)
while(erro > 1/10 ** 12):
        palpite = (palpite+(x/palpite))/2
        erro = (palpite*palpite - x)
print (f"{palpite:.3f}")
### ou print("%.3f" % palpite)
