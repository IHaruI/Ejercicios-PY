from lista_personajes import lista_heroes
from funciones import *
import os

while True:
    try:
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("|     ----- ¡Bienvenido! -----     |")
        print("|――――――――――――――――――――――――――――――――――|")
        print("|         Menu de Opciones         |")
        print("|――――――――――――――――――――――――――――――――――|")
        print("|1. Nombre de Heroes.              |")
        print("|2. Nombre y altura de Heroes.     |")
        print("|3. Altura del heroe mas alto.     |")
        print("|4. Altura del heroe mas bajo.     |")
        print("|5. Altura promedio de Heroes.     |")
        print("|6. Nombre del mas alto y bajo.    |")
        print("|7. Nombre del mas y menos pesado. |")
        print("|8. Devolver solo numero pares.    |")
        print("|9. Calcular productos de números. |")
        print("|10. Determinar si es palíndromo.  |")
        print("|0. Para salir.                    |")
        print("|__________________________________|")

        opcion = int(input("Opción elegida: "))
        os.system("cls")

        match opcion:
            case 1:
                lista_nombres(lista_heroes)
                limpiado_de_pantalla()
            case 2:
                nombre_altura(lista_heroes)
                limpiado_de_pantalla()
            case 3:
                print(f"El heroe mas alto mide: {heroe_mas_alto(lista_heroes)}")
                limpiado_de_pantalla()
            case 4:
                print(f"El heroe mas bajo mide: {heroe_mas_bajo(lista_heroes)}")
                limpiado_de_pantalla()
            case 5:
                print(f"El promedio es: {promedio(lista_heroes):.2f}")
                limpiado_de_pantalla()
            case 6:
                print(nombres_del_mas_alto_y_bajo(lista_heroes))
                limpiado_de_pantalla()
            case 7:
                print(mas_y_menos_pesado(lista_heroes))
                limpiado_de_pantalla()
    
    except ValueError:
        print("Error, Eliga una de las opciones!")
        os.system("pause")
        os.system("cls")