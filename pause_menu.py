import pygame, config
from button import Button
from config import get_font

#idioma
def cargar_img(ruta_relativa):
    ruta = f"assets/{config.idioma}/{ruta_relativa}"
    return pygame.image.load(ruta).convert_alpha()

def mostrar_menu_pausa(pantalla):
    mouse_pos = pygame.mouse.get_pos()

    #fondo oscuro
    overlay = pygame.Surface(pantalla.get_size())
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    pantalla.blit(overlay, (0, 0))
    
    #texto pausa
    texto_pausa = get_font(50).render("PAUSA", True, "White")
    pantalla.blit(texto_pausa, texto_pausa.get_rect(center=(650, 100)))

    #botones para elmenu de pausa
    boton_continuar = Button(image=cargar_img("boton_pausa/Resume_icono.png"), image_hover=cargar_img("boton_pausa/Resume_hover.png"), pos=(645, 250), text_input=".", font=get_font(1), base_color="White", hovering_color="Green")
    boton_reiniciar = Button(image=cargar_img("boton_pausa/Restart_icono.png"), image_hover=cargar_img("boton_pausa/Restart_hover.png"), pos=(650, 400), text_input=".", font=get_font(1), base_color="White", hovering_color="Orange")
    boton_menu = Button(image=cargar_img("boton_pausa/Quit_icono.png"), image_hover=cargar_img("boton_pausa/Quit_hover.png"), pos=(645, 550), text_input=".", font=get_font(1), base_color="White", hovering_color="Red")

    for boton in [boton_continuar, boton_reiniciar, boton_menu]:
        boton.changeColor(mouse_pos)
        boton.update(pantalla)

    return boton_continuar, boton_reiniciar, boton_menu