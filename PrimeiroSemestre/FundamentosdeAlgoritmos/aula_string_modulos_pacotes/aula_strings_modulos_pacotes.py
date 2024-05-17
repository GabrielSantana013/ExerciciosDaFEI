"""
Para imprimir os caracteres da tabela ASCII:
for i in range(0,255):
    print("%c" % i, end=" ")

Para imprimir os caracteres da tabela UTF (Unicode):
print(u’\u00ae’)
print(u’\u0061’)
print(u’\u00c7’)

"""


"""
Ex 1 -
Faça um programa que peça uma string para o usuário;
Imprima uma nova string substituindo as vogais minúsculas por vogais.
maiúsculas.
"""

'''
entrada = input("Digite uma string: ")

for x in entrada:
    if x == 'a' or x =='e' or x =='i' or x =='o' or x =='u':
        print(x.upper(), end="")
    else:
        print(x, end="")
'''


"""
Ex 2 -
Peça ao usuário uma string1;
Imprima se essa string é um palíndromo ou não.
Palíndromo é uma palavra ou frase (normalmente, ignorando-se os
espaços em branco) que se pode ler, indiferentemente, da esquerda
para a direita ou vice-versa.
Exemplos: “ovo”, “a grama é amarga” maiúsculas.

"""

'''
entrada = input("Digite uma string: ")

"""
for x in range (len(entrada) -1, -1, -1):
    print(entrada[x])
"""

nova_entrada = ""

for i in entrada:
    if i != ' ':
        nova_entrada += i
entrada_reversa = nova_entrada[::-1]

if nova_entrada == entrada_reversa:
    print("Palindromo!")
else:
    print("Não é Palindromo!")
'''

"""
Ex 3 -
Neste exercício, você criará um programa em Python que identifica
a(s) palavras(s) mais longa(s) em um arquivo.
Seu programa deve exibir uma mensagem que inclua o tamanho da palavra
mais longa, juntamente com todas as palavras desse comprimento que
ocorreram no arquivo. Desconsidere sinais de pontuação.

"""

'''
with open("teste.txt", "r") as teste:
    texto_arquivo = teste.read()
    texto_arquivo = texto_arquivo.split()
    tamanho = 0
    for i in texto_arquivo:
        if i.isalpha():
            if len(i) > tamanho:
                tamanho = len(i)
                palavras = []
                palavras.append(i)
            elif len(i) == tamanho:
                palavras.append(i)
print(palavras)

'''

"""
Ex 4 -
Escreva um programa que exiba a(s) palavra(s) que ocorrera(m) com
mais frequência em um arquivo e quantas vezes a(s) palavra(s)
aparece(m).
Seu programa deve começar lendo o nome do arquivo do usuário.
Em seguida, ele deve encontrar a(s) palavra(s) mais frequente(s),
ignorando letras maiúsculas ou minúsculas e a pontuação.
Desta forma, por exemplo, as palavras apple, apple!, Apple, APPLE e
ApPlE devem todas ser contadas como uma única palavra.

"""

'''
def trataPalavras(i):
    palavra = ""
    for letra in i:
        if letra >= 'A' and letra <='Z' or letra >='a' and letra <='z' or letra>='0' and letra <='9':
            palavra += letra.upper()
    return palavra


with open("repetidas.txt", "r") as teste:
    texto_arquivo = teste.read()
    texto_arquivo = texto_arquivo.split()
    palavras_repetidas = {}
    for i in texto_arquivo:
        i = trataPalavras(i)
        if i in palavras_repetidas:
            palavras_repetidas[i] +=1
        else:
            palavras_repetidas[i] = 1

    maximo = max(palavras_repetidas.values())#values pega o valor da chave, get pega a chave e items pega tudo
    #print(maximo)
    L = []
    for i in palavras_repetidas:
        if palavras_repetidas[i] == maximo:
            L.append(i)
print(L)

'''

"""
Ex 5-
Pig Latin é uma língua construída pela transformação de palavras da
língua inglesa.
Regras usadas para traduzir do inglês para o Pig Latin:
1) Se a palavra começar com consoante (incluindo y), todas as letras no
início da palavra, até a primeira vogal (excluindo y), serão removidas e
adicionadas ao final da palavra, seguidas de ay.
Por exemplo:
computer se torna omputercay e think se torna inkthay.
2) Se a palavra começar com uma vogal (não incluindo y), então way é
adicionado ao final da palavra.
Por exemplo:
o algorithm se torna algorithmway e office se torna officeway. Escreva
um programa que leia uma linha de texto do usuário.
Seu programa deve traduzir a linha para Pig Latin e exibir o
resultado.
Trate letras maiúsculas, minúsculas e pontuação.

"""
'''
def trataPalavras(i):
    palavra = ""
    for letra in i:
        if letra >= 'A' and letra <='Z' or letra >='a' and letra <='z':
            palavra += letra.lower()
    return palavra

entrada = input("Digite sua palavra: ")
entrada = trataPalavras(entrada)

vogais = ['a', 'e', 'i', 'o', 'u']

status = True
letras = ""

for i in entrada:
    if entrada[0] in vogais and status:
        entrada = entrada + "way"
        break
    else:
        status = False
        if i not in vogais:
            letras += i
            entrada = entrada[1:] #tira o primeiro da palavra
        else:
            entrada = entrada + letras + "ay"
            break
print(entrada)

'''

"""
Ex 6 -
Neste exercício, você deve programar um módulo composto por 4 funções
que, juntas, servirão para determinar se uma senha é boa ou não. Uma
boa senha deve ter:
▶ Pelo menos 8 caracteres (1ª função)
▶ Pelo menos uma letra maiúscula (2ª função)
▶ Pelo menos uma letra minúscula (3ª função)
▶ Pelo menos um número (4ª função)
Cada função deve retornar True ou False para a senha recebida.
Faça também um programa principal que leia uma senha do usuário,
chame cada função de verificação e relate se a senha é boa ou não.

"""

'''
import modulos

senha = input("Digite sua senha: ")

if modulos.numCaracteres(senha) and modulos.procuraMaiuscula(senha) and modulos.procuraMinuscula(senha) and modulos.procuraNum(senha):
    print("Senha segura.")
else:
    print("Senha fraca")
'''

"""
Ex 8 -
Muitas pessoas não usam letras maiúsculas corretamente, especialmente
ao digitar em pequenos dispositivos como smartphones.
Neste exercício, você escreverá um módulo composto por uma função que
capitaliza os caracteres apropriados em uma string.
O primeiro caractere da string deve ser sempre capitalizado, assim
como o primeiro caractere após “.”, “!” ou “?”.
Por exemplo, se a função for fornecida com a string:
“que horas tenho que estar lá? qual é o endereço?”
Então deve retornar a string:
“Que horas tenho que estar lá? Qual é o endereço?”
"""
import modulos

entrada = input("Digite seu texto: ")
entrada = modulos.capitalizar(entrada)
print(entrada)
