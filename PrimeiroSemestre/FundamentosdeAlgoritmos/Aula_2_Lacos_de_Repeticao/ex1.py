"""
Considerando que a distância entre os pontos p0 e p1
pode ser calculada usando
distancia = sqrt(( p0_x - p1_x)^2 + (p0_y - p1_y)^2 ),
faça um programa que leia os valores x e y de dois pontos
e exiba a distância entre eles.
O programa deve parar quando a primeira entrada for a string "sair"
"""


from math import sqrt

while True:
    x0 = (input("valor de X para P0: "))
    if x0 == 'sair':
        break
    x0 = float(x0)
    y0 = float((input("valor de Y para P0: ")))
    x1 = float((input("valor de X para P1: ")))
    y1 = float((input("valor de Y para P1: ")))

    distancia = sqrt(( x1 - x0)**2 + (y1 - y0)**2)

    print(f"Distância de {distancia}")



###sqrt(( p0_x - p1_x)^2 + (p0_y - p1_y)^2 