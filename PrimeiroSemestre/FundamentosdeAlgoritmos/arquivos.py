"""
Sintaxe:

arquivo = open("nomeDoArquivo.txt", "w")

w = write
r = read
a = append (preserva o conteúdo existente)
+ = (combinação entre w e r)


arquivo.close()

se usar: with open("arquivo.txt", "w") as arquivo:
NÃO PRECISA USAR O arquivo.close()

txt.replace("string que ja existe","string que vai trocar")
.split("caracter de separação") transforma numa lista

EX: gabriel,santana,dias
.split()
["gabriel", "santana", "dias"]

.strip() tira o /n do final

"""

"""
EXEMPLO 1 -Gerar e gravar números pares e ímpares em arquivos separados:
Números de 0 a 999.
Números pares no arquivo pares.txt
Números ímpares no arquivo impares.txt

"""
'''
with open("pares.txt", "w") as pares, open("impares.txt", "w") as impares:
    for i in range (1000):
        if i % 2 == 0:
            pares.write("%d\n" % i)
        else:
            impares.write("%d\n"% i)
'''

"""
EXEMPLO 2 - Utilize o arquivo “pares.txt” gerado no último exemplo:
Vamos criar outro arquivo que deve conter somente os números
múltiplos de 4

"""
'''
with open ("pares.txt", "r") as pares:
    for i in pares:
        if int(i) % 4 == 0:
            with open("multD4.txt", "a") as multD4:
                multD4.write("%d\n" % int(i))
'''

"""
EXEMPLO 3 -Ler da entrada padrão o nome e o telefone de um usuário e gravar no
arquivo: “contatos.txt”, em uma mesma linha;
Parar quando nome for vazio;
Abrir o arquivo gerado;
Ler os registros e mostrar os dados na saída padrão.
"""

'''
while True:
    nome = input("Digite seu nome: ")
    if nome == "":
        with open("contatos.txt", "r") as contatos:
            for linha in contatos.readlines():
                print(linha)
            break
    telefone = int(input("Digite seu telefone: "))
    with open("contatos.txt", "a") as contatos:
        contatos.write("%s %d\n" %(nome,telefone))
'''

"""
Ex 1 -Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
A primeira linha deve conter o maior número e a última linha o menor.
Salve o resultado em outro arquivo (invertido.txt).

"""

'''
with open("pares.txt","r") as pares:
    num = pares.readlines()
    num.reverse()

with open("invertidos.txt", "w") as invertidos:
    for i in num:
        invertidos.write("%d\n" %int(i))
'''

"""
Ex 2 - Crie um arquivo: “numeros.txt” que contenha 100 números aleatórios;
Todos os números do arquivo estão na mesma e única linha, separados
por espaço;
Escreva uma função em Python para retornar a somatória de todos os
números que estão armazenados no arquivo “numeros.txt”.

"""
'''
from random import randint

with open("numeros.txt", "w") as numeros:
    for i in range (100):
        numeros.write(str(randint(1,100)))
        numeros.write(" ")

with open("numeros.txt", "r") as numeros:
    num = numeros.readline().split()
print(num)

resultado = 0
for i in num:
    resultado += int(i)
print(resultado)
'''

"""
Ex 3 - Crie um arquivo: “numeros.txt” que contenha 100 números aleatórios;
Escreva uma função que leia uma sequência numérica do arquivo
“numeros.txt” e salva os números na lista num.
Escreva outra função que recebe a lista num como parâmetro e retorna
uma nova lista num_unicos, sem os elementos repetidos.
Escreva uma terceira função que recebe a lista num_unicos e grava os
números no arquivo “numeros_unicos.txt”.

"""
'''
def salvaEmLista():
    with open("numeros.txt", "r") as numeros:
        num = numeros.readline().split()
    return num
def achaUnicos(num):
    unicos = set(num)
    listaUnicos = list(unicos)
    return listaUnicos

def gravaUnicos(num):
    with open("numeros_unicos.txt", "w") as numUnicos:
        for i in range (len(num)):
            numUnicos.write("%s\n" % num[i])

from random import randint

with open("numeros.txt", "w") as numeros:
    for i in range (100):
        numeros.write(str(randint(1,100)))
        numeros.write(" ")
num = salvaEmLista()
gravaUnicos(achaUnicos(num))
'''

"""
Ex 4 - Crie uma agenda de telefones que salva os dados de maneira
permanente.
A agenda deve funcionar em loop infinito, até que o usuário decida
sair. Os dados armazenados são: nome, sobrenome, telefone e e-mail.
A agenda deve apresentar o seguinte menu para o usuário:
▶ 1 - Novo contato (create)
▶ 2 - Procura (pelo nome) (read)
▶ 3 - Atualiza contato (update)
▶ 4 - Apaga contato (delete)
▶ 0 - Sair

"""
'''
def novoContato():
    with open("agenda.txt", "a") as agenda:
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        telefone = int(input("Digite o telefone: "))
        email = input("Digite o email: ")
        agenda.write("%s %s %d %s\n" %(nome, sobrenome, telefone, email))

def procuraContato():
    nome = input("Digite o nome para procurar na agenda: ")
    with open("agenda.txt", "r") as agenda:
        for linha in agenda:
            partes = linha.strip().split()
            if partes[0] == nome:
                print("Nome: ", partes[0])
                print("Sobrenome: ", partes[1])
                print("Telefone: ", partes[2])
                print("Email: ", partes[3])
def atualizaContato():
    nome = input("Digite o nome para atualizar o contato: ")
    contatosAtualizados = []
    with open("agenda.txt", "r") as agenda:
        for linha in agenda:
            partes = linha.strip().split()
            if partes[0] == nome:
                novo_Nome = input("Digite o novo nome: ")
                novo_SobreNome = input("Digite o novo sobrenome: ")
                novo_Telefone = input("Digite o novo telefone: ")
                novo_Email = input("Digite o novo email: ")
                contatoAtualizado = f"{novo_Nome} {novo_SobreNome} {novo_Telefone} {novo_Email}\n"
                contatosAtualizados.append(contatoAtualizado)
            else:
                contatosAtualizados.append(linha)
    with open("agenda.txt", "w") as agenda:
        for linha in contatosAtualizados:
            agenda.write(linha)

def apagaContato():
    nome = input("Digite o nome para apagar o contato: ")
    contatosAtualizados = []
    with open("agenda.txt", "r") as agenda:
        for linha in agenda:
            partes = linha.strip().split()
            if partes[0] == nome:
                continue
            else:
                contatosAtualizados.append(linha)
    with open("agenda.txt", "w") as agenda:
        for linha in contatosAtualizados:
            agenda.write(linha)
while True:
    print("▶ 1 - Novo contato ")
    print("▶ 2 - Procura (pelo nome) ")
    print("▶ 3 - Atualiza contato ")
    print("▶ 4 - Apaga contato (delete) ")
    print("▶ 0 - Sair ")
    escolha = input("")

    if escolha == '1':
        novoContato()
    elif escolha == '2':
        procuraContato()
    elif escolha == '3':
        atualizaContato()
    elif escolha == '4':
        apagaContato()
    elif escolha == '0':
        break

'''