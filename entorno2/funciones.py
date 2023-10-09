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

def nombres_masculinos_y_femeninos(lista_heroes, genero):
    
    print(f"         Nombres")
    print(f"    -----------------")
    
    for i in lista_heroes:
        if i["genero"] == genero:
            print(f"     {i['nombre']}")

def heroe_mas_alto_y_bajo_masculino_y_femenino(lista_heroes, genero, altura):
    
    if genero == "M":
        return nombre_MyF_mas_alto_y_bajo(lista_heroes, genero, altura)
    
    elif genero == "F":
        return nombre_MyF_mas_alto_y_bajo(lista_heroes, genero, altura)

def nombre_MyF_mas_alto_y_bajo(lista_heroes, genero, altura):
    maximo = 0
    minimo = 0
    bandera = True
    
    if altura == "Alto":
        for i in lista_heroes:
                if (i["genero"] == genero) and (float(i["altura"]) > maximo):
                    maximo = float(i["altura"])
                    nombre = i["nombre"]

    elif altura == "Bajo":
        for i in lista_heroes:
                if (i["genero"] == genero) and ((float(i["altura"]) < minimo) or bandera):
                    maximo = float(i["altura"])
                    nombre = i["nombre"]
                    bandera = False

    return nombre

def altura_promedio_masculino_y_femenino(lista_heroes, genero):

    if genero == "M":
        return promedio_masc_y_femen(lista_heroes, genero)

    elif genero == "F":
        return promedio_masc_y_femen(lista_heroes, genero)

def promedio_masc_y_femen(lista_heroes, genero):
    acumulador = 0
    contador = 0

    for i in lista_heroes:
        if i["genero"] == genero:
            acumulador += float(i["altura"])
            contador += 1
    
    return acumulador / contador

def tipos_de_ojos_y_pelos_de_heroes(lista_heroes, tipo):
    lista = {}
    contador = 0

    for i in lista_heroes:
        if not(i[tipo] in lista):
            if i[tipo] == "":
                contador += 1
                lista["No tiene"] = contador
            else:
                lista[(i[tipo])] = 1
        else:
            for valor in lista.values():
                if lista[(i[tipo])] == valor:
                    lista[(i[tipo])] = valor + 1
                    break
    
    print("    Tipos                Cantidad de usuarios")
    print("    --------------------------------------------")
    for clave, valor in lista.items():
        print(f"    {clave:<30} {valor}")
    lista.clear()

def tipos_de_heroes_por_pelos_ojos__y_inteligencia(lista_heroes, tipo):
    lista1 = {}
    auxiliar = True

    for i in lista_heroes:
        if not(i[tipo] in lista1):
            if i[tipo] == "":
                nombre = i["nombre"]
                if auxiliar:
                    lista1["No tiene"] = nombre
                    auxiliar = False
                else:
                    for clave, valor in lista1.items():
                        if clave == "No tiene":
                            lista1["No tiene"] = f"{valor}, {i['nombre']}"
                            break
            else:
                lista1[(i[tipo])] = i["nombre"]
        else:
            for valor in lista1.values():
                if lista1[(i[tipo])] == valor:
                    bandera = f"{valor}, {i['nombre']}"
                    lista1[(i[tipo])] = bandera
                    break
    
    print("    Tipos                          Nombres")
    print("    ---------------------------------------------------------------------------------------------------------------")
    for clave, valor in lista1.items():
        print(f"    {clave:<30} {valor}")
    lista1.clear()