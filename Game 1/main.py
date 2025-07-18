import pygame
import time
import random
import sys
"""
VAMOS A CREAR LA VENTANA.TODA VENTANA NECESITA ANCHO Y ALTURA Y COLOR

WIDHT,HEIGHT =1000,800 # Las constantes de la ventana
WHITE = (255, 255, 255) # Definimos un color blanco en formato RGB
    
surface = pygame.display.set_mode((WIDHT,HEIGHT)) # pygame.display.set_mode() crea la ventana principal del juego devuelve un objeto surface donde dibujas todos los elementos de la ventana

pygame.display.set_caption("Mi primera ventana") # pygame.display.set_caption() establece el título de la ventana del juego

def main():
    clock = pygame.time.Clock() # pygame.time.Clock() para controlar los FPS (frames por segundo)

    running = True # Bucle principal del juego

    while running:
        # Manejar eventos
        for event in pygame.event.get(): # pygame.event.get() obtiene todos los eventos que han ocurrido desde la última vez que se llamó a esta función
            if event.type == pygame.QUIT: # Si el evento es de tipo QUIT, significa que el usuario ha cerrado la ventana
                running = False

        # Llenar pantalla con color
        surface.fill(WHITE)
        
        # Actualizar pantalla
        pygame.display.flip()
        
        # Controlar FPS
        clock.tick(60)

    # Cerrar pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

"""

WIDHT,HEIGHT =1000,800 # Las constantes de la ventana   
surface = pygame.display.set_mode((WIDHT,HEIGHT)) # pygame.display.set_mode() crea la ventana principal del juego devuelve un objeto surface donde dibujas todos los elementos de la ventana
pygame.display.set_caption("Perro astronauta") # pygame.display.set_caption() establece el título de la ventana del juego

bg = pygame.image.load("assets/bg.jpg").convert() # Cargamos la imagen de fondo y la convertimos para optimizar su uso convert() mejora el rendimiento al usar imágenes en Pygame

def draw():

    surface.blit(bg, (0, 0))  # Dibujamos el fondo en la superficie en la posición (0, 0) blit es una función que dibuja una superficie sobre otra
    pygame.display.update()  # Actualizamos la pantalla para reflejar los cambios


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw()  # Llamamos a la función draw para dibujar el fondo

    pygame.quit()

if __name__ == "__main__":
    main()
