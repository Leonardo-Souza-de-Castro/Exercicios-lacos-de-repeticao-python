from math import sqrt


while(True):

    x1 = input("valor de X para P0: ")

    if x1 == "sair":
        break

    y1 = input("valor de Y para P0: ")

    if y1 == "sair":
        break

    x2 = input("valor de X para P1: ")

    if x2 == "sair":
        break

    y2 = input("valor de Y para P1: ")

    if y2 == "sair":
        break

    distancia = sqrt((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2)
    
    print(f"Distância de {distancia}")


