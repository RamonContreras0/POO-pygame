
import pygame
import math

class Circulo:
    def __init__(self, x, y, radio, color, velocidad, teclas_mov):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.velocidad = velocidad
        self.teclas_mov = teclas_mov
        self.default_color = color

    def dibujar(self, ventana):
        # Dibujar el círculo
        pygame.draw.circle(ventana, self.color, (int(self.x), int(self.y)), self.radio)

    def mover(self, teclas):
        # Mover el círculo según las teclas presionadas
        if teclas[self.teclas_mov['izq']]:
            self.x -= self.velocidad
        if teclas[self.teclas_mov['der']]:
            self.x += self.velocidad
        if teclas[self.teclas_mov['arr']]:
            self.y -= self.velocidad
        if teclas[self.teclas_mov['aba']]:
            self.y += self.velocidad

    def colisiona(self, otro_circulo):
        # Detectar colisiones circulares
        distancia = math.sqrt((self.x - otro_circulo.x) ** 2 + (self.y - otro_circulo.y) ** 2)
        return distancia < self.radio + otro_circulo.radio

    def cambiar_color(self, color):
        self.color = color

    def resetear_color(self):
        self.color = self.default_color


# Inicializar Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimiento de Círculos con Detección de Colisiones")

# Definir los círculos
circulo1 = Circulo(200, 300, 40, (0, 255, 0), 0.3, {
    'izq': pygame.K_a, 'der': pygame.K_d, 'arr': pygame.K_w, 'aba': pygame.K_s
})

circulo2 = Circulo(600, 300, 40, (0, 0, 255), 0.3, {
    'izq': pygame.K_LEFT, 'der': pygame.K_RIGHT, 'arr': pygame.K_UP, 'aba': pygame.K_DOWN
})

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener estado de las teclas
    teclas = pygame.key.get_pressed()

    # Mover los círculos
    circulo1.mover(teclas)
    circulo2.mover(teclas)

    # Verificar colisiones
    if circulo1.colisiona(circulo2):
        circulo1.cambiar_color((255, 0, 0))  # Cambiar a rojo en caso de colisión
        circulo2.cambiar_color((255, 0, 0))  # Cambiar a rojo en caso de colisión
    else:
        circulo1.resetear_color()  # Restablecer color
        circulo2.resetear_color()  # Restablecer color

    # Pintar fondo
    ventana.fill((0, 0, 0))

    # Dibujar los círculos
    circulo1.dibujar(ventana)
    circulo2.dibujar(ventana)

    # Actualizar pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()