from pantalla_seleccion import inicio, menu_prin, opciones
from pantalla_niveles import pantalla_seleccion_nivel
from selection_screen import selection
from juego import pantalla
from nivel1 import jugar_nivel1
from nivel2 import jugar_nivel2
from nivel3 import jugar_nivel3
import pygame, sys
from game_over import pantalla_gameover


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
            pantalla_actual = menu_prin(pantalla)

        elif pantalla_actual == "nivel":  # Nueva pantalla (seleccion de niveles)
            nivel_elegido = pantalla_seleccion_nivel(pantalla)
            if nivel_elegido == "salir":
                pantalla_actual = "salir"
            elif nivel_elegido == "menu":
                pantalla_actual = "menu"
            else:
                nivel_seleccionado = nivel_elegido
                pantalla_actual = "selection"

        elif pantalla_actual == "selection":
            personaje = selection(pantalla)
            pantalla_actual = "play"

        elif pantalla_actual == "reiniciar":
            pantalla_actual = "play"

        elif pantalla_actual == "play":
            if nivel_seleccionado == 1:
                resultado = jugar_nivel1(pantalla, personaje)
            elif nivel_seleccionado == 2:
                resultado = jugar_nivel2(pantalla, personaje)
            elif nivel_seleccionado == 3:
                resultado = jugar_nivel3(pantalla, personaje)

            if resultado == "nivel2":
                nivel_seleccionado = 2
                pantalla_actual = "play"
            elif resultado == "nivel3":
                nivel_seleccionado = 3
                pantalla_actual = "play"
            elif resultado == "victoria":
                pantalla_actual = "menu"
            elif resultado == "game_over":
                pantalla_actual = pantalla_gameover(pantalla, personaje)
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