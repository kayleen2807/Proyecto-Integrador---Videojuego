from pantalla_seleccion import inicio, menu_prin, opciones
from selection_screen import selection
from game import play
import pygame, sys

# Bucle principal del juego
def main():
    #Se incia el programa con la pantalla de inicio (bienvevida)
    pantalla_actual = "inicio"
    #Este bucle hace el intercanbio de una pantalla a otra y se activa la funcion de cada una
    while True: 
        #inicio/bienvenida
        if pantalla_actual == "inicio":
            pantalla_actual = inicio()
        #menu principal
        elif pantalla_actual == "menu":
            pantalla_actual = menu_prin()
        #seleccion de personajes
        elif pantalla_actual == "selection":
            pantalla_actual = selection()
        #ventana para jugar
        elif pantalla_actual == "play":
            pantalla_actual = play()
        #ventana opciones
        elif pantalla_actual == "opciones":
            pantalla_actual = opciones()
        #salir del juego
        elif pantalla_actual == "salir":
            pygame.quit()
            sys.exit()
try:
    main()
except Exception as e:
    #detectar algun erro mas facil
    print("¡Error detectado!")
    print(e)