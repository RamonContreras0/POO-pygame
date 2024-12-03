
import pygame

class Circulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.05  # Velocidad de movimiento en pixeles
        self.color = (0, 255, 0)  # Color verde
        self.radio = 25  # Radio del círculo

    def dibujar(self, ventana):
        # Dibujar el círculo
        pygame.draw.circle(ventana, self.color, (int(self.x), int(self.y)), self.radio)

    def mover(self, teclas):
        if teclas[pygame.K_j]:  # Mover hacia la izquierda
            self.x -= self.velocidad
        if teclas[pygame.K_l]:  # Mover hacia la derecha
            self.x += self.velocidad
        if teclas[pygame.K_i]:  # Mover hacia arriba
            self.y -= self.velocidad
        if teclas[pygame.K_k]:  # Mover hacia abajo
            self.y += self.velocidad
