from pantalla_seleccion import inicio, menu_prin, opciones
from pantalla_niveles import pantalla_seleccion_nivel
from selection_screen import selection
from juego import play, pantalla
import pygame, sys

# Bucle principal del juego
def main():
    #Se incia el programa con la pantalla de inicio (bienvevida)
    pantalla_actual = "inicio"
    nivel_seleccionado = None
    personaje = None
    #Este bucle hace el intercanbio de una pantalla a otra y se activa la funcion de cada una
    while True:
        if pantalla_actual == "inicio":
            pantalla_actual = inicio()

        elif pantalla_actual == "menu":
            pantalla_actual = menu_prin()

        elif pantalla_actual == "nivel":  # Nueva pantalla
            nivel_elegido = pantalla_seleccion_nivel(pantalla)
            if nivel_elegido == "salir":
                pantalla_actual = "salir"
            else:
                # Guarda el nivel elegido y pasa a selección de personaje
                nivel_seleccionado = nivel_elegido
                pantalla_actual = "selection"

        elif pantalla_actual == "selection":
            personaje = selection(pantalla)
            pantalla_actual = "play"

        elif pantalla_actual == "reiniciar":
            pantalla_actual = "play"

        elif pantalla_actual == "play":
            resultado = play(nivel_seleccionado, personaje)
            if resultado == "victoria":
                pantalla_actual = "menu"
            elif resultado == "game_over":
                pantalla_actual = "menu"
            elif resultado == "salir":
                pantalla_actual = "salir"
            elif resultado == "menu":
                pantalla_actual = "menu"
            elif resultado == "reiniciar":
                pantalla_actual = "play"

        elif pantalla_actual == "opciones":
            pantalla_actual = opciones()

        elif pantalla_actual == "salir":
            pygame.quit()
            sys.exit()                                                                                                                                                                                                                                                                                                                                  
try:
    main()
except Exception as e:
    #detectar algun erro mas facil
    print("¡Error detectado!")
    print(e)