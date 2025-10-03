import pygame
from button import Button
from config import get_font

def mostrar_menu_pausa(pantalla):
    mouse_pos = pygame.mouse.get_pos()

    #fondo oscuro
    overlay = pygame.Surface(pantalla.get_size())
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    pantalla.blit(overlay, (0, 0))
    
    #texto pausa
    texto_pausa = get_font(50).render("PAUSE", True, "White")
    pantalla.blit(texto_pausa, texto_pausa.get_rect(center=(650, 80)))

    #botones para elmenu de pausa
    boton_continuar = Button(image=pygame.image.load("assets/boton_pausa/Resume.png"), image_hover=pygame.image.load("assets/boton_pausa/hover_resume.png"), pos=(650, 200), text_input=".", font=get_font(1), base_color="White", hovering_color="Green")
    boton_reiniciar = Button(image=pygame.image.load("assets/boton_pausa/Restart.png"), image_hover=pygame.image.load("assets/boton_pausa/hover_restart.png"), pos=(650, 380), text_input=".", font=get_font(1), base_color="White", hovering_color="Orange")
    boton_menu = Button(image=pygame.image.load("assets/boton_pausa/Quit.png"), image_hover=pygame.image.load("assets/boton_pausa/hover_quit.png"), pos=(640, 560), text_input=".", font=get_font(1), base_color="White", hovering_color="Red")

    for boton in [boton_continuar, boton_reiniciar, boton_menu]:
        boton.changeColor(mouse_pos)
        boton.update(pantalla)

    return boton_continuar, boton_reiniciar, boton_menu