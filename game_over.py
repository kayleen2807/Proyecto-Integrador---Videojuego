import pygame, config
from juego import get_font
from button import Button
from animacion_gameover import reproducir_animacion
from musica import reproducir_musica, detener_musica

def cargar_img(ruta_relativa):
    ruta = f"assets/{config.idioma}/{ruta_relativa}"
    return pygame.image.load(ruta).convert_alpha()

def game_over(pantalla):
    fondo_game_over = cargar_img("game_over/pantalla.png").convert_alpha()
    # Obtener el rect centrado en la pantalla
    rect_fondo = fondo_game_over.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))
    while True:
        pantalla.fill((0, 0, 0))  # Fondo negro detrás
        pantalla.blit(fondo_game_over, rect_fondo)  # Imagen centrada

        mouse_pos = pygame.mouse.get_pos()

        boton_menu = Button(image=cargar_img("game_over/volver.png"), image_hover=None, pos=(450, 630), text_input=".", font=get_font(1), base_color="White", hovering_color="Blue")
        boton_reiniciar = Button(image=cargar_img("game_over/retry.png"), image_hover=None, pos=(850, 630), text_input=".", font=get_font(1), base_color="White", hovering_color="Blue")

        boton_menu.changeColor(mouse_pos)
        boton_menu.update(pantalla)
        boton_reiniciar.changeColor(mouse_pos)
        boton_reiniciar.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_menu.checkForInput(mouse_pos):
                    return "menu"
                elif boton_reiniciar.checkForInput(mouse_pos):
                    return "reiniciar"

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def pantalla_gameover(pantalla, personaje):
    reproducir_animacion(pantalla, personaje)
    reproducir_musica("assets/musica/game_over.mp3", volumen=0.4, loop=0)
    pygame.time.wait(500)  # Pequeña pausa opcional
    return game_over(pantalla)