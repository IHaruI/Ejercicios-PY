import os
import sys

def limpiado_de_pantalla():
        os.system("pause")
        os.system("cls")

def lista_nombres(lista_heroes):
    for i in lista_heroes:
        print(f"Nombre: {i['nombre']}")

def nombre_altura(lista_heroes):
    print("      Nombre               Altura")
    for i in lista_heroes:
        print(f"{i['nombre']:<20} {i['altura']}")

def heroe_mas_alto(lista_heroes):
    maximo = 0

    for i in lista_heroes:
        if float(i["altura"]) > maximo:
            maximo = float(i["altura"])
    
    return maximo

def heroe_mas_bajo(lista_heroes):
    minimo = 0
    bandera = True

    for i in lista_heroes:
        if ((float(i["altura"]) < minimo) or bandera):
            minimo = float(i["altura"])
            bandera = False
    
    return minimo

def promedio(lista_heroes):
    acumulador = 0

    for i in lista_heroes:
        acumulador += float(i["altura"])

    return acumulador / len(lista_heroes)

def nombres_del_mas_alto_y_bajo(lista_heroes):
    maximo = heroe_mas_alto(lista_heroes)
    minimo = heroe_mas_bajo(lista_heroes)

    for i in lista_heroes:
        if maximo == float(i["altura"]):
            nombre_maximo = i["nombre"]
        if minimo == float(i["altura"]):
            nombre_minimo = i["nombre"]

    return f"El heroe mas alto es '{nombre_maximo}' y del mas bajo es '{nombre_minimo}'"

def mas_y_menos_pesado(lista_heroes):
    maximo = 0
    minimo = 0
    bandera = True

    for i in lista_heroes:
        if float(i["peso"]) > maximo:
            maximo = float(i["peso"])
            nombre_mas_pesado = i["nombre"]

        if ((float(i["peso"]) < minimo) or bandera):
            minimo = float(i["peso"])
            nombre_menos_pesado = i["nombre"]
            bandera = False
        
    return f"El heroe mas pesado es '{nombre_mas_pesado}' y el menos pesado es '{nombre_menos_pesado}'"