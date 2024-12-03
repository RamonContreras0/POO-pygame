
import pygame

class Cuadrado:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.05  # Velocidad de movimiento en pixeles
        self.color = (255, 255, 0)  # Color amarillo
        self.lado = 50  # Tamaño del cuadrado

    def dibujar(self, ventana):
        # Dibujar el cuadrado
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.lado, self.lado))

    def mover(self, teclas):
        if teclas[pygame.K_a]:  # Mover hacia la izquierda
            self.x -= self.velocidad
        if teclas[pygame.K_d]:  # Mover hacia la derecha
            self.x += self.velocidad
        if teclas[pygame.K_w]:  # Mover hacia arriba
            self.y -= self.velocidad
        if teclas[pygame.K_s]:  # Mover hacia abajo
            self.y += self.velocidad
