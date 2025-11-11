import pygame 
import config
#reproducir musica
def reproducir_musica(ruta, volumen=0.5, loop=-1):
    if config.musica_activa:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(-1)

def detener_musica():
    pygame.mixer.music.stop()

def pausar_musica():
    pygame.mixer.music.pause()

def continuar_musica():
    pygame.mixer.music.unpause()
