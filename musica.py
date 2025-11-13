import pygame 
import config
musica_actual = None
#reproducir musica
def reproducir_musica(ruta, volumen=0.5, loop=-1):
    global musica_actual
    if config.musica_activa and ruta != musica_actual:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(loop)
        musica_actual = ruta

def detener_musica():
    pygame.mixer.music.stop()

def pausar_musica():
    pygame.mixer.music.pause()

def continuar_musica():
    pygame.mixer.music.unpause()
