from random import randint

'''
Crie uma matriz M[12][12] com números inteiros aleatórios (de 0 até 10: randint(0,10)); Então, leia um caractere maiúsculo (S ou M), que indica uma operação que deve ser realizada na matriz. Em seguida, calcule e mostre a soma (S) ou a média (M) considerando somente aqueles elementos que estão abaixo da diagonal secundária da matriz, conforme ilustrado abaixo (área verde). Exiba a matriz criada e o resultado da operação.

Para imprimir os elementos da matriz utilize "%3d" para dar espaço de 3 caracteres.

Utilize somente número inteiros (inclusive no cálculo da média).
'''

"""

operacao = input()
matriz = []
contador = 0
res = 0

for i in range (12):
    matriz.append([])
    for j in range (12):
        matriz[i].append(randint(0,10))
        if(i+j) > 11:
            res += matriz[i][j]
            contador +=1

print("Matriz criada:")

for i in range (12):
    for j in range(12):
        print("%3d" % matriz[i][j], end=" ")
    print()

if operacao == "M":
    res = res/contador
print("Resultado da conta: %d " %res)
"""


'''

Crie uma matriz M[12][12] com números inteiros aleatórios (de 0 até 10: randint(0,10)); Então, leia um caractere maiúsculo (S ou M), que indica uma operação que deve ser realizada na matriz. Em seguida, calcule e mostre a soma (S) ou a média (M) considerando somente aqueles elementos que estão acima da diagonal secundária da matriz, conforme ilustrado abaixo (área verde). Exiba a matriz criada e o resultado da operação.

Para imprimir os elementos da matriz utilize "%3d" para dar espaço de 3 caracteres.

Utilize somente número inteiros (inclusive no cálculo da média).

'''

"""

operacao = input()

matriz = []
cont = 0
res = 0

for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(randint(0,10))
        if (i+j) < 11:
            res += matriz[i][j]
            cont +=1

print("Matriz criada:")

for i in range (12):
    for j in range (12):
        print("%3d" % matriz[i][j], end =" ")
    print()

if operacao == "M":
    res = res/cont
print("Resultado da conta: %d" %res)
"""

'''
Crie uma matriz M[12][12] com números inteiros aleatórios (de 0 até 10: randint(0,10)); Então, leia um caractere maiúsculo (S ou M), que indica uma operação que deve ser realizada na matriz. Em seguida, calcule e mostre a soma (S) ou a média (M) considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde). Exiba a matriz criada e o resultado da operação.

Para imprimir os elementos da matriz utilize "%3d" para dar espaço de 3 caracteres.

Utilize somente número inteiros (inclusive no cálculo da média).
'''
'''

operacao = input()
matriz  = []
cont = 0
res = 0

for i in range (12):
    matriz.append([])
    for j in range (12):
        matriz[i].append(randint(0,10))
        if j+i < 11 and j>i:
            cont +=1
            res += matriz[i][j]

print("Matriz criada: ")
for i in range(12):
    for j in range(12):
        print("%3d" %matriz[i][j], end=" ")
    print()

if operacao == 'M':
    res = res/cont

print("Resultado da conta: %d" %res)
'''


'''
Construa um programa em Python que deve receber duas strings e combiná-las, alternando uma letra de cada string em uma palavra resultante (que será diretamente exibida na tela, não é salva em uma variável). Considere que uma string pode ser maior que a outra na entrada; nesse caso, as letras que sobrarem (não utilizadas durante a alternância) devem ser adicionadas ao fim da palavra resultante.

Exemplo 1: entradas com o mesmo tamanho
palavra1 = prova
palavra2 = exito
saída: perxoivtao

Exemplo 2: entradas com tamanhos diferentes
palavra1 = prova
palavra2 = algoritmos
saída: parlogvoaritmos
'''

"""

str1 = input()
str2 = input()
tam1 = len(str1)
tam2 = len(str2)
maior = 0


if tam1>= tam2:
    maior = tam1
else:
    maior = tam2

for i in range (maior):
    if i < tam1:
        print(str1[i], end="")
    if i < tam2:
        print(str2[i], end="")
print()
"""

'''
Dois carros (X e Y) partem em uma mesma direção. 
O carro X sai com velocidade constante de 60 km/h e o carro Y sai com velocidade constante de 90 km/h. 
Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, 
consegue se afastar um quilômetro a cada 2 minutos. 
Leia a distância (em km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.
'''

'''
distancia = int(input("Digite a distância: "))
minutos = (distancia*2)
print(f"\n{minutos} minutos")
'''

"""
Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que: 

a) Esse funcionário foi contratado em 2005, com salário inicial de R$ 5.000,00; 

b) Em 2006 ele recebeu aumento de 1,5% sobre o salário inicial; 

c) A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior. 

Faça um programa que recebe um ano (ano > 2007) e determina o salário atual do funcionário.
"""

'''
ANO_INICIAL = 2005
SALARIO_INICIAL = 5000.00
BONUS_INICIAL = (1.5/100)
ano_Atual = int(input("Digite o ano desejado: "))


for i in range(ano_Atual-ANO_INICIAL):
    SALARIO_INICIAL += BONUS_INICIAL*SALARIO_INICIAL
    BONUS_INICIAL *=2

print(f"Salário de {ano_Atual}: R$ {SALARIO_INICIAL:.2f}")

'''

"""

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas.
"""

'''
distancia = int(input("digite a distância percorrida: "))
preco = 0

if distancia > 200:
    preco = distancia*0.45
else:
    preco = distancia*0.5
print(f"{preco:.2f}")
'''

"""

Faça um programa que calcula
2n
, onde
n
deve ser digitado pelo usuário. Então, seu programa deve realizar a soma de cada digito do
 resultado obtido e exibir a resposta. 

"""
'''
potencia = int(input("Digite a potência: "))
resultado = 2**potencia
strPot = str(resultado)
listaNums = []

print(f"2^{potencia} = {resultado}")

for i in strPot:
    listaNums.append(i)

res = 0

for i in listaNums:
    res += int(i)

soma_String = ' + '.join(listaNums)

print(f"{soma_String} = {res}")
'''

"""
Um reservatório vazio deve ser abastecido por uma bomba. Faça um programa em Python para calcular o tempo (em segundos) necessário para que o reservatório fique completamente cheio. A vazão da bomba (em litros 
por segundo) e a capacidade do reservatório (em litros) serão digitadas pelo usuário.
"""

'''
capacidade = float(input("Digite a capacidade do reservatório: \n"))
vazao = float(input("Digite a vazão da bomba: \n"))
print(f"Tempo necessário para encher o reservatório: {capacidade/vazao} segundos")
'''

'''
num = 1
res = 0
while num != 0:
    num = int(input())
    res +=num
print(f"Resultado: {res}")
'''

"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo (todos números inteiros). A seguir calcule a duração do jogo.

O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
"""

hI = int(input("Digite a hora inicial: \n"))
mI = int(input("Digite o minuto inicial: \n"))
hF = int(input("Digite a hora final: \n"))
mF = int(input("Digite o minuto final: \n"))

totalMinutosInicio = hI * 60 + mI
totalMinutosFinal = hF*60 + mF
duracaoTotal = 0

if totalMinutosFinal > totalMinutosInicio:
    duracaoTotal = totalMinutosFinal - totalMinutosInicio
else:
    duracaoTotal = (24*60 - totalMinutosInicio) + totalMinutosFinal
duracaoHoras = duracaoTotal // 60
duracaoMinutos = duracaoTotal % 60
print(f"O jogo durou {duracaoHoras} hora(s) e {duracaoMinutos} minutos(s)")
