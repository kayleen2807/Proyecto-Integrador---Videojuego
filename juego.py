import pygame, pytmx, sys
from selection_screen import selection
from button import Button
from config import pantalla, get_font
from selection_player import Personaje
from pause_menu import mostrar_menu_pausa
from game_over import game_over
from musica import reproducir_musica, detener_musica, pausar_musica, continuar_musica

#inicio para pygame
pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((1280, 720) , pygame.FULLSCREEN)
pygame.display.set_caption("Menu principal")


#fondo para el nivel 1

nfondo = pygame.image.load("assets/fondos/Fondo.png")

# Función para cargar fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#transicion
def fade_in_total(pantalla, fondo, duracion=1000):
    clock = pygame.time.Clock()
    overlay = pygame.Surface(pantalla.get_size())
    overlay.fill((0, 0, 0))
    alpha = 255
    while alpha > 0:
        pantalla.blit(fondo, (0, 0))
        overlay.set_alpha(alpha)
        pantalla.blit(overlay, (0, 0))
        pygame.display.flip()
        alpha -= 255 / (duracion / clock.tick(60))
