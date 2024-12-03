
import pygame
from triangulo import Triangulo
from cuadrado import Cuadrado
from circulo import Circulo

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimiento de Figuras")

background_color = (0, 0, 0)

# Instancias de las clases Triángulo, Cuadrado y Círculo
triangulo = Triangulo(400, 100)
cuadrado = Cuadrado(200, 300)
circulo = Circulo(600, 400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Estado de las teclas
    teclas = pygame.key.get_pressed()

    # Mover las figuras
    triangulo.mover(teclas)
    cuadrado.mover(teclas)
    circulo.mover(teclas)

    # Pintar el fondo
    ventana.fill(background_color)

    # Dibujar las figuras
    triangulo.dibujar(ventana)
    cuadrado.dibujar(ventana)
    circulo.dibujar(ventana)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()
