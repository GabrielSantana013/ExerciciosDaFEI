import tkinter as tk
from tkinter import messagebox
from tkinter import ttk #basicamente o css do tk
"""

#criando janela
window = tk.Tk()
#definindo o título da janela
window.title("Aula GUI")
#configurando o tamanho da janela
window.geometry('400x400')

#criando um texto
rotulo = tk.Label(window, text="Primeira aplicação gráfica em python!", font=("Arial Bold", 14))
rotulo.place(x=200, y=100, anchor="center")


#ação do botão
def botao_pressionado():
    rotulo.config(text="Botao pressionado")


#criar botão

botao = tk.Button(window, text="Botao1", command=botao_pressionado)
botao.place(x=200, y=200, anchor="center")






#fica chamando a janela em loop
window.mainloop()

"""


"""
EXEMPLO 1 -
Interface gráfica para somar dois números:

"""

'''
def soma():
        try:
            n1 = float(entrada1.get())
            n2 = float(entrada2.get())
            n3 = n1+n2
            entradaResultado.delete(0, tk.END)
            entradaResultado.insert(0, n3)
        except ValueError:
            pass


window = tk.Tk()
window.title("Soma")
window.geometry('400x400')


num1 = tk.Label(window, text="Digite o primeiro número: ", font=("Arial Bold", 14))
num2 = tk.Label(window, text="Digite o segundo número: ", font=("Arial Bold", 14))
resultado = tk.Label(window, text="Resultado:  ", font=("Arial Bold", 14))
botao = tk.Button(window, text="Soma!", command=soma)


entrada1 = tk.Entry(window, width=20)
entrada2 = tk.Entry(window, width=20)
entradaResultado = tk.Entry(window, width=20)


num1.grid(row=0, column=0, padx=5, pady=5)
num2.grid(row=1, column=0, padx=5, pady=5)
entrada1.grid(row=0, column=1, padx=5, pady=5)
entrada2.grid(row=1, column=1, padx=5, pady=5)
resultado.grid(row=2, column=0, padx=5, pady=5)
entradaResultado.grid(row=2, column = 1, padx=5, pady=5)

botao.grid(row=3,column=0)

window.mainloop()

'''

"""
Ex 1 -
Faça uma calculadora para transformar números decimais em: binários, 
hexadecimais ou octais. Cada base numérica deve ter um botão para 
realizar a conversão.

"""
'''
def converter(num):
    try:
        n1 = int(Entrada.get())
        if num == 1:
            Saida.delete(0,tk.END)
            Saida.insert(0, bin(n1))
        elif num == 2:
            Saida.delete(0, tk.END)
            Saida.insert(0, hex(n1))
        else:
            Saida.delete(0, tk.END)
            Saida.insert(0, oct(n1))
    except ValueError:
        Saida.delete(0, tk.END)
        Saida.insert(0, "Entrada inválida!")

window = tk.Tk()
window.title("Conversão Numérica")
window.geometry('400x200')

numeroDecimal = tk.Label(window, text="Número decimal: ", font=("Arial Bold", 14))
Resultado = tk.Label(window, text="Resposta: ", font=("Arial Bold", 14))
Entrada = tk.Entry(window, width=20)
Saida = tk.Entry(window, width=20)
#numero = int(Entrada.get())

b1 = tk.Button(window, text="Binário", command=lambda:converter(1))
b2 = tk.Button(window, text="Hexadecimal", command=lambda:converter(2))
b3 = tk.Button(window, text="Octal", command=lambda:converter(3))

b1.grid(row=1, column=0, padx=5, pady=5)
b2.grid(row=1, column=1, padx=5, pady=5)
b3.grid(row=1, column=2, padx=5, pady=5)


numeroDecimal.grid(row=0, column=0, padx=10, pady=10)
Entrada.grid(row=0, column=1, padx=10, pady=10)
Resultado.grid(row=2, column=0, padx=10, pady=10)
Saida.grid(row=2, column=1 ,padx=5, pady=5)

window.mainloop()

'''

"""
Ex 2-
Crie um programa que lê uma letra do alfabeto por uma caixa de texto. Se 
o usuário digitar a, e, i, o ou u, seu programa deverá exibir uma mensagem 
indicando que a letra inserida é uma vogal (utilize caixas de mensagem - 
messagebox). Se o usuário digitar y, seu programa deve exibir uma 
mensagem indicando que às vezes y é uma vogal (depende da língua, no 
inglês, por exemplo), e às vezes y é uma consoante. Caso contrário, seu 
programa deve exibir uma mensagem indicando que o letra é uma 
consoante
"""
'''
def verificar():
    vogais = ['a', 'e', 'i', 'o', 'u']
    if l1.get() == 'y':
        messagebox.showinfo("Verificação","As vezes pode ser vogal ou consoante, depende do idioma.")
    elif l1.get() in vogais:
        messagebox.showinfo("Verificação", "Vogal.")
    else:
        messagebox.showinfo("Verificação", "Consoante.")


window = tk.Tk()
window.title("Vogal ou Consoante?")
window.geometry("400x100")

entrada = tk.Label(window, text="Digite uma letra: ")
l1 = tk.Entry(window, width=20)
b1 = tk.Button(window, text="Verificar", command=verificar)

entrada.grid(row=0, column=0, padx=5, pady=5)
l1.grid(row=0, column=2, padx=5, pady=5)
b1.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()

'''

"""
Ex 3 -
Faça uma calculadora com as 4 operações básicas, potência, sen, cos, 
tan, log e raiz quadrada.
"""

#INCOMPLETO


n1 = ""
def calcular(entrada):
    global n1
    operacoes = ["C", "sen", "cos", "tan", "log", "/", "^", "√", "=", "+", "-", "x"]
    if entrada not in operacoes:
         n1 += entrada
    else:
        print("Pinto")
    print (n1)

window = tk.Tk()
window.title("Calculadora")
window.geometry("300x400")

display = tk.Entry(window, width=47)
b0 = tk.Button(window, text=("0"), command=lambda:calcular("0"))
b1 = tk.Button(window, text=("1"), command=lambda:calcular("1"))
b2 = tk.Button(window, text=("2"), command=lambda:calcular("2"))
b3 = tk.Button(window, text=("3"), command=lambda:calcular("3"))
b4 = tk.Button(window, text=("4"), command=lambda:calcular("4"))
b5 = tk.Button(window, text=("5"), command=lambda:calcular("5"))
b6 = tk.Button(window, text=("6"), command=lambda:calcular("6"))
b7 = tk.Button(window, text=("7"), command=lambda:calcular("7"))
b8 = tk.Button(window, text=("8"), command=lambda:calcular("8"))
b9 = tk.Button(window, text=("9"), command=lambda:calcular("9"))

bMais = tk.Button(window, text=("+"), command=lambda:calcular("+"))
bMenos = tk.Button(window, text=("-"), command=lambda:calcular("-"))
bMult = tk.Button(window, text=("x"), command=lambda:calcular("x"))
bC = tk.Button(window, text=("C"), command=lambda:calcular("C"))
bSeno = tk.Button(window, text=("sen"), command=lambda:calcular("sen"))
bCos = tk.Button(window, text=("cos"), command=lambda:calcular("cos"))
bTan = tk.Button(window, text=("tan"), command=lambda:calcular("tan"))
bLog = tk.Button(window, text=("log"), command=lambda:calcular("log"))
bIgual = tk.Button(window, text=("="), command=lambda:calcular("="))
bDivisao = tk.Button(window, text=("/"), command=lambda:calcular("/"))
bPotencia = tk.Button(window, text=("^"), command=lambda:calcular("^"))
bRaiz = tk.Button(window, text=("√"), command=lambda:calcular("√"))


display.grid(row=0, column=0,columnspan=6, padx=5, pady=5)

#linha 1
b7.grid(row=1, column=0, padx=1, pady=1, sticky="ew")
b8.grid(row=1, column=1, padx=1, pady=1, sticky="ew")
b9.grid(row=1, column=2, padx=1, pady=1, sticky="ew")
bMais.grid(row=1, column=3, padx=1, pady=1, sticky="ew")
bC.grid(row=1, column = 4, columnspan=2, padx=1, pady=1, sticky="ew")


#linha 2

b4.grid(row=2, column=0, padx=1, pady=1, sticky="ew")
b5.grid(row=2, column=1, padx=1, pady=1, sticky="ew")
b6.grid(row=2, column=2, padx=1, pady=1, sticky="ew")
bMenos.grid(row=2, column=3, padx=1, pady=1, sticky="ew")
bSeno.grid(row=2, column=4, padx=1, pady=1, sticky="ew")
bCos.grid(row=2, column=5, padx=1, pady=1, sticky="ew")

#linha3

b1.grid(row=3, column=0, padx=1, pady=1, sticky="ew")
b2.grid(row=3, column=1, padx=1, pady=1, sticky="ew")
b3.grid(row=3, column=2, padx=1, pady=1, sticky="ew")
bMult.grid(row=3, column=3, padx=1, pady=1, sticky="ew")
bTan.grid(row=3, column=4, padx=1, pady=1, sticky="ew")
bLog.grid(row=3, column=5, padx=1, pady=1, sticky="ew")

#linha4

bIgual.grid(row=4, column=0, padx=1, pady=1, sticky="ew")
b0.grid(row=4, column=1, padx=1, pady=1, sticky="ew")
bDivisao.grid(row=4, column=3, padx=1, pady=1, sticky="ew")
bPotencia.grid(row=4, column=4, padx=1, pady=1, sticky="ew")
bRaiz.grid(row=4, column=5, padx=1, pady=1, sticky="ew")

window.mainloop()