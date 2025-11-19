import pygame, config
from button import Button
from juego import get_font
from juego import fade_in_total

#idioma
def cargar_img(ruta_relativa):
    ruta = f"assets/{config.idioma}/{ruta_relativa}"
    return pygame.image.load(ruta).convert_alpha()

#pantalla de seleccion de nivel
def pantalla_seleccion_nivel(pantalla):
    fondo = pygame.image.load("assets/fondos/seleccion.png").convert()
    fondo = pygame.transform.scale(fondo, pantalla.get_size())
    fade_in_total(pantalla, fondo)

    select = cargar_img("texto/nivel.png").convert_alpha()
    pantalla.blit(select, (440, 100))

    boton_nivel1 = Button(image=cargar_img("botones_niveles/boton_nivel1.png"), image_hover=cargar_img("botones_niveles/boton_nivel1_h.png"), pos=(650, 200), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_nivel2 = Button(image=cargar_img("botones_niveles/boton_nivel2.png"), image_hover=cargar_img("botones_niveles/boton_nivel2_h.png"), pos=(650, 320), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_nivel3 = Button(image=cargar_img("botones_niveles/boton_nivel3.png"), image_hover=cargar_img("botones_niveles/boton_nivel3_h.png"), pos=(650, 440), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_salir = Button(image=cargar_img("botones_niveles/boton_back.png"), image_hover=cargar_img("botones_niveles/boton_back_h.png"), pos=(650, 575), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")    

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for boton in [boton_nivel1, boton_nivel2, boton_nivel3, boton_salir]:
            boton.changeColor(mouse_pos)
            boton.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_nivel1.checkForInput(mouse_pos):
                    return 1
                elif boton_nivel2.checkForInput(mouse_pos):
                    return 2
                elif boton_nivel3.checkForInput(mouse_pos):
                    return 3
                elif boton_salir.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()