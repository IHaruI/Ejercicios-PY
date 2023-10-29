import pygame
from configuracion import *
from funciones import *
from random import randint, randrange

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Figuras")

# radio = 100
# rectangulo = (200 ,100)
# cuadrado = (200, 200)
triangulo_rectangulo = [(300, 100), (300, 400), (500, 400)]

# perimetro_circulo = calcular_perimetro_circulo(radio)
# area_circulo = calcular_area_circulo(radio)
# perimetro_rectangulo = calcular_perimetro_rectangulo(rectangulo)
# area_rectangulo = calcular_area_rectangulo(rectangulo)
# perimetro_cuadrado = calcular_perimetro_cuadrado(cuadrado)
# area_cuadrado = calcular_area_cuadrado(cuadrado)
perimetro_triangulo_rectangulo = calcular_perimetro_triangulo_rectangulo(triangulo_rectangulo)
area_triangulo_rectangulo = calcular_area_triangulo_rectangulo(triangulo_rectangulo)

# circulo = {"rect": pygame.Rect((CENTER_WIDTH - radio), (CENTER_HEIGHT - radio), radio * 2, radio * 2), "color": GREEN, "borde": 0, "radio": radio}
# rectangulo = {"rect": pygame.Rect((CENTER_WIDTH - (rectangulo[0] // 2)), (CENTER_HEIGHT - (rectangulo[1] // 2)), rectangulo[0], rectangulo[1]), "color": GREEN, "borde": 0, "radio": -1}
# cuadrado = {"rect": pygame.Rect((CENTER_WIDTH - (cuadrado[0] // 2)), (CENTER_HEIGHT - (cuadrado[1] // 2)), cuadrado[0], cuadrado[1]), "color": GREEN, "borde": 0, "radio": -1}
poligono = {"punto_A": triangulo_rectangulo[0], "punto_B": triangulo_rectangulo[1], "punto_C": triangulo_rectangulo[2], "color": GREEN, "borde": 0, "radio": -1}


fuente = pygame.font.SysFont(None, 40)
# texto_perimetro = fuente.render(f"Perimetro: {perimetro_circulo:.5f} px", True, GREEN, BLUE)
# texto_area = fuente.render(f"Area: {area_circulo:.5f} px", True, GREEN, BLUE)
# texto_perimetro = fuente.render(f"Perimetro: {perimetro_rectangulo:.5f} px", True, GREEN, BLUE)
# texto_area = fuente.render(f"Area: {area_rectangulo:.5f} px", True, GREEN, BLUE)
# texto_perimetro = fuente.render(f"Perimetro: {perimetro_cuadrado:.5f} px", True, GREEN, BLUE)
# texto_area = fuente.render(f"Area: {area_cuadrado:.5f} px", True, GREEN, BLUE)
texto_perimetro = fuente.render(f"Perimetro: {perimetro_triangulo_rectangulo:.5f} px", True, GREEN, BLUE)
texto_area = fuente.render(f"Area: {area_triangulo_rectangulo:.5f} px", True, GREEN, BLUE)

is_running = True

while is_running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_running = False

    # pygame.draw.rect(screen, circulo["color"], circulo["rect"], circulo["borde"], circulo["radio"])
    # pygame.draw.rect(screen, rectangulo["color"], rectangulo["rect"], rectangulo["borde"], rectangulo["radio"])
    # pygame.draw.rect(screen, cuadrado["color"], cuadrado["rect"], cuadrado["borde"], cuadrado["radio"])
    pygame.draw.polygon(screen, poligono["color"], ((poligono["punto_A"]), (poligono["punto_B"]), (poligono["punto_C"])))

    screen.blit(texto_perimetro, (60, 490))
    screen.blit(texto_area, (60, 520))

    pygame.display.flip()