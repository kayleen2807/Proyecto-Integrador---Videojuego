import pygame 
#reproducir musica
def reproducir_musica(ruta, volumen=0.5, loop=-1):
    try
pygame.mixer.music.load(ruta)

pygame.mixer.music.set_volume(volumen)

pygame.mixer.music.play(loop)
     except Exception as e:
print(f"Error al reproducir música: {e}")

def detener_musica():
pygame.mixer.music.stop()

def pausar_musica():
pygame.mixer.music.pause()

def continuar_musica():

pygame.mixer.music.unpause()
