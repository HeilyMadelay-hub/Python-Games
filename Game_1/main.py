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

bg = pygame.transform.scale(pygame.image.load("assets/bg.jpg"), (WIDHT, HEIGHT))  # Cargamos la imagen de fondo y la escalamos al tamaño de la ventana con transform.scale hacemos que la imagen de fondo se ajuste al tamaño de la ventana

player_width = 50
player_height = 50

def draw(player):

    surface.blit(bg, (0, 0))  # Dibujamos el fondo en la superficie en la posición (0, 0) blit es una función que dibuja una superficie sobre otra
   
    pygame.draw.rect(surface, (255, 0, 0), player)  # Dibujamos un rectángulo rojo que representa al jugador en la superficie

    pygame.display.update()  # Actualizamos la pantalla para reflejar los cambios


def main():
    run = True

    player = pygame.Rect(200, HEIGHT - player_height,player_width, player_height) 

    """
    pygame.Rect(x, y, width, height) crea un rectángulo que representa al jugador.
    - x: posición horizontal del rectángulo
    - y: posición vertical del rectángulo
    - width: ancho del rectángulo
    - height: altura del rectángulo

    HEIGHT - player_height calcula la posición vertical del jugador para que esté en la parte inferior de la ventana, restando la altura del jugador de la altura total de la ventana.
    Esto asegura que el jugador comience en la parte inferior de la pantalla.


    """

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # Manejo de teclas para mover el personaje 18:15


        draw(player)  # Llamamos a la función draw para dibujar el fondo y el jugador

    pygame.quit()

if __name__ == "__main__":
    main()
