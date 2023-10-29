import math
import pygame
from configuracion import *

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def calcular_area_circulo(radio) -> float:
    return math.pi * pow(radio, 2)

def calcular_perimetro_rectangulo(rectangulo):
    return (rectangulo[0] * 2) + (rectangulo[1] * 2)

def calcular_area_rectangulo(rectangulo):
    return rectangulo[0] * rectangulo[1]

def calcular_perimetro_cuadrado(cuadrado):
    return (cuadrado[0] * 2) + (cuadrado[1] * 2)

def calcular_area_cuadrado(cuadrado):
    return cuadrado[0] * cuadrado[1]

def calcular_perimetro_triangulo_rectangulo(triangulo_rectangulo):
    altura = triangulo_rectangulo[1][1] - triangulo_rectangulo[0][1]
    base = triangulo_rectangulo[2][0] - triangulo_rectangulo[1][0]
    c = math.sqrt(pow(altura, 2) + pow(base, 2))

    return altura + base + c

def calcular_area_triangulo_rectangulo(triangulo_rectangulo):
    altura = triangulo_rectangulo[1][1] - triangulo_rectangulo[0][1]
    base = triangulo_rectangulo[2][0] - triangulo_rectangulo[1][0]

    return (altura * base) / 2

def crear_bloque(left = 0, top = 0, ancho = 40, alto = 40, color = RED, borde = 0, radio = -1):
    
    rect = pygame.Rect(left, top, ancho, alto)

    return {"rect": rect, "color": color, "borde": borde, "radio": radio}