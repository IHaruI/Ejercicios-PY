from lista_personajes import lista_heroes
from funciones import *
import os

while True:
    try:
        print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
        print("|             ----- ¡Bienvenido! -----            |")
        print("|―――――――――――――――――――――――――――――――――――――――――――――――――|")
        print("|                 Menu de Opciones                |")
        print("|―――――――――――――――――――――――――――――――――――――――――――――――――|")
        print("|1. Nombre de Heroes.                             |")
        print("|2. Nombre y altura de Heroes.                    |")
        print("|3. Altura del heroe mas alto.                    |")
        print("|4. Altura del heroe mas bajo.                    |")
        print("|5. Altura promedio de Heroes.                    |")
        print("|6. Nombre del mas alto y bajo.                   |")
        print("|7. Nombre del mas y menos pesado.                |")
        print("|8. Nombre de heroes masculinos.                  |")
        print("|9. Nombre de heroes femeninos.                   |")
        print("|10. Heroe mas alto masculino.                    |")
        print("|11. Heroe mas alto femenino.                     |")
        print("|12. Heroe mas bajo masculino.                    |")
        print("|13. Heroe mas bajo femenino.                     |")
        print("|14. Promedio de heroes masculinos.               |")
        print("|15. Promedio de heroes femeninos.                |")
        print("|16. Cantidad de heroes por tipos de ojo.         |")
        print("|17. Cantidad de heroes por tipos de pelo.        |")
        print("|18. Cantidad de heroes por tipos de inteligencia.|")
        print("|19. Listado de heroes por color de ojos.         |")
        print("|20. Listado de heroes por color de pelo.         |")
        print("|21. Listado de heroes por tipo de inteligencia.  |")
        print("|_________________________________________________|")

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
            case 8:
                nombres_masculinos_y_femeninos(lista_heroes, "M")
                limpiado_de_pantalla()
            case 9:
                nombres_masculinos_y_femeninos(lista_heroes, "F")
                limpiado_de_pantalla()
            case 10:
                print(f"El heroe mas alto masculino es: {heroe_mas_alto_y_bajo_masculino_y_femenino(lista_heroes, 'M', 'Alto')}")
                limpiado_de_pantalla()
            case 11:
                print(f"La heroe mas alta femenina es: {heroe_mas_alto_y_bajo_masculino_y_femenino(lista_heroes, 'F', 'Alto')}")
                limpiado_de_pantalla()
            case 12:
                print(f"El heroe mas bajo masculino es: {heroe_mas_alto_y_bajo_masculino_y_femenino(lista_heroes, 'M', 'Bajo')}")
                limpiado_de_pantalla()
            case 13:
                print(f"La heroe mas baja femenina es: {heroe_mas_alto_y_bajo_masculino_y_femenino(lista_heroes, 'F', 'Bajo')}")
                limpiado_de_pantalla()
            case 14:
                print(f"El promedio de los heroes masculinos es: {altura_promedio_masculino_y_femenino(lista_heroes, 'M'):.2f}")
                limpiado_de_pantalla()
            case 15:
                print(f"El promedio de las heroes femeninas es: {altura_promedio_masculino_y_femenino(lista_heroes, 'F'):.2f}")
                limpiado_de_pantalla()
            case 16:
                tipos_de_ojos_y_pelos_de_heroes(lista_heroes, "color_ojos")
                limpiado_de_pantalla()
            case 17:
                tipos_de_ojos_y_pelos_de_heroes(lista_heroes, "color_pelo")
                limpiado_de_pantalla()
            case 18:
                tipos_de_ojos_y_pelos_de_heroes(lista_heroes, "inteligencia")
                limpiado_de_pantalla()
            case 19:
                tipos_de_heroes_por_pelos_ojos__y_inteligencia(lista_heroes, "color_ojos")
                limpiado_de_pantalla()
            case 20:
                tipos_de_heroes_por_pelos_ojos__y_inteligencia(lista_heroes, "color_pelo")
                limpiado_de_pantalla()
            case 21:
                tipos_de_heroes_por_pelos_ojos__y_inteligencia(lista_heroes, "inteligencia")
                limpiado_de_pantalla()
    
    except ValueError:
        print("Error, Eliga una de las opciones!")
        os.system("pause")
        os.system("cls")