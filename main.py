from screens import inicio, menu_prin, opciones
from game import play
import pygame, sys

# Bucle principal del juego
def main():
    #Se incia el programa con la pantalla de inicio (bienvevida)
    pantalla_actual = "inicio"
    while True: 
        if pantalla_actual == "inicio":
            pantalla_actual = inicio()
        elif pantalla_actual == "menu":
            pantalla_actual = menu_prin()
        elif pantalla_actual == "play":
            pantalla_actual = play()
        elif pantalla_actual == "opciones":
            pantalla_actual = opciones()
        elif pantalla_actual == "salir":
            pygame.quit()
            sys.exit()
try:
    main()
except Exception as e:
    print("¡Error detectado!")
    print(e)