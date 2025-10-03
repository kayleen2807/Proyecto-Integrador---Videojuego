import pygame
from button import Button
from config import get_font

def mostrar_menu_pausa(pantalla):
    mouse_pos = pygame.mouse.get_pos()

    boton_continuar = Button(image=None, image_hover=None, pos=(640, 300), text_input="CONTINUAR", font=get_font(30), base_color="White", hovering_color="Green")
    boton_reiniciar = Button(image=None, image_hover=None, pos=(640, 400), text_input="REINICIAR", font=get_font(30), base_color="White", hovering_color="Orange")
    boton_menu = Button(image=None, image_hover=None, pos=(640, 500), text_input="MENU PRINCIPAL", font=get_font(30), base_color="White", hovering_color="Red")

    overlay = pygame.Surface(pantalla.get_size())
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    pantalla.blit(overlay, (0, 0))

    texto_pausa = get_font(50).render("PAUSA", True, "White")
    pantalla.blit(texto_pausa, texto_pausa.get_rect(center=(640, 200)))

    for boton in [boton_continuar, boton_reiniciar, boton_menu]:
        boton.changeColor(mouse_pos)
        boton.update(pantalla)

    return boton_continuar, boton_reiniciar, boton_menu