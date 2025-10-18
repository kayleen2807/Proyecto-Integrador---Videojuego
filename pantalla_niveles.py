import pygame
from button import Button
from juego import get_font

def pantalla_seleccion_nivel(pantalla):
    fondo = pygame.image.load("assets/fondos/seleccion.png").convert()
    fondo = pygame.transform.scale(fondo, pantalla.get_size())

    fuente = pygame.font.Font(None, 60)
    texto = fuente.render("Selecciona un nivel", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(pantalla.get_width() // 2, 100))

    boton_nivel1 = Button(image=None, image_hover=None, pos=(500, 220), text_input="Nivel 1", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
    boton_nivel2 = Button(image=None, image_hover=None, pos=(500, 320), text_input="Nivel 2", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
    boton_nivel3 = Button(image=None, image_hover=None, pos=(500, 420), text_input="Nivel 3", font=get_font(100), base_color="#d7fcd4", hovering_color="White")
    

    while True:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(texto, texto_rect)

        mouse_pos = pygame.mouse.get_pos()
        for boton in [boton_nivel1, boton_nivel2, boton_nivel3]:
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

        pygame.display.update()