import pygame
from juego import get_font
from button import Button
def game_over(pantalla):
    from juego import play
    while True:
        pantalla.fill((0, 0, 0))

        texto = get_font(60).render("GAME OVER", True, "Red")
        pantalla.blit(texto, texto.get_rect(center=(640, 250)))

        mouse_pos = pygame.mouse.get_pos()

        boton_menu = Button(image=None, image_hover=None, pos=(640, 400), text_input="VOLVER AL MENU", font=get_font(30), base_color="White", hovering_color="Gray")
        boton_reiniciar = Button(image=None, image_hover=None, pos=(640, 500), text_input="REINTENTAR", font=get_font(30), base_color="White", hovering_color="Gray")

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
                    return play()

        pygame.display.flip()
        pygame.time.Clock().tick(60)
