from config import pantalla, get_font
from juego import fondo
from button import Button
import pygame
# Pantalla de inicio
def inicio():
    pygame.display.set_caption("Inicio")
    while True:
        #fondo
        mouse_pos = pygame.mouse.get_pos()
        pantalla.fill("black")

        #texto de bienvenida
        texto = get_font(80).render("Bienvenido", True, "White")
        texto_rect = texto.get_rect(center=(640, 200))
        pantalla.blit(texto, texto_rect)

        #boton de empezar que lleva al menu principal
        boton_empezar = Button(image=None, image_hover=None, pos=(640, 400), text_input="EMPEZAR", font=get_font(45), base_color="White", hovering_color="Blue")
        boton_empezar.changeColor(mouse_pos)
        boton_empezar.update(pantalla)

        #cerrar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_empezar.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()

# Menú principal
def menu_prin():
    pygame.display.set_caption("Menu principal")
    while True:
        #diseño menu principal
        pantalla.blit(fondo, (0,0))
        mouse_pos = pygame.mouse.get_pos()

        title = pygame.image.load("assets/title.png")
        pantalla.blit(title, (320, 5))

        #botones play, opciones y salir
        boton_play = Button(image=pygame.image.load("assets/button_play.png"), image_hover=pygame.image.load("assets/hover_play.png"), pos=(650, 300), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        boton_opciones = Button(image=pygame.image.load("assets/button_opts.png"), image_hover=pygame.image.load("assets/hover_opts.png"), pos=(650, 440), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        boton_salir = Button(image=pygame.image.load("assets/button_exit.png"), image_hover=pygame.image.load("assets/hover_exit.png"), pos=(635, 590), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

        for boton in [boton_play, boton_opciones, boton_salir]:
            boton.changeColor(mouse_pos)
            boton.update(pantalla)

        #acciones de los botones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_play.checkForInput(mouse_pos):
                    return "play"
                elif boton_opciones.checkForInput(mouse_pos):
                    return "opciones"
                elif boton_salir.checkForInput(mouse_pos):
                    return "salir"

        pygame.display.update()

# Pantalla de opciones
def opciones():
    pygame.display.set_caption("Opciones")
    while True:
        mouse_pos = pygame.mouse.get_pos()
        pantalla.fill("White")

        #opciones (en proceso)
        texto = get_font(15).render("Estas seran las opciones", True, "Black")
        texto_rect = texto.get_rect(center=(640, 260))
        pantalla.blit(texto, texto_rect)

        boton_back = Button(image=None, image_hover=None, pos=(640, 460), text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Blue")
        boton_back.changeColor(mouse_pos)
        boton_back.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_back.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()
