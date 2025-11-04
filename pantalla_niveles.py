import pygame
from button import Button
from juego import get_font
from juego import fade_in_total

def pantalla_seleccion_nivel(pantalla):
    fondo = pygame.image.load("assets/fondos/seleccion.png").convert()
    fondo = pygame.transform.scale(fondo, pantalla.get_size())
    fade_in_total(pantalla, fondo)

    fuente = pygame.font.Font(None, 60)
    texto = fuente.render("Selecciona un nivel", True, (0, 0, 0))
    texto_rect = texto.get_rect(center=(pantalla.get_width() // 2, 110))

    boton_nivel1 = Button(image=pygame.image.load("assets/botones_niveles/boton_nivel1.png"), image_hover=pygame.image.load("assets/botones_niveles/boton_nivel1_h.png"), pos=(650, 200), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_nivel2 = Button(image=pygame.image.load("assets/botones_niveles/boton_nivel2.png"), image_hover=pygame.image.load("assets/botones_niveles/boton_nivel2_h.png"), pos=(650, 320), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_nivel3 = Button(image=pygame.image.load("assets/botones_niveles/boton_nivel3.png"), image_hover=pygame.image.load("assets/botones_niveles/boton_nivel3_h.png"), pos=(650, 440), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_salir = Button(image=pygame.image.load("assets/botones_niveles/boton_back.png"), image_hover=pygame.image.load("assets/botones_niveles/boton_back_h.png"), pos=(650, 575), text_input="", font=get_font(1), base_color="#d7fcd4", hovering_color="White")    

    while True:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto, texto_rect)

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