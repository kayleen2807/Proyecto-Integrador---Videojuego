import pygame
pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((1280, 720),) #pygame.FULLSCREEN)
pygame.display.set_caption("Menu principal")

# Función para cargar fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)