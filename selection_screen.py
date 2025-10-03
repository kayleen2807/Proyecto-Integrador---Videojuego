import pygame
from config import get_font

def fade_in(pantalla, fondo, duracion=1000):
    clock = pygame.time.Clock()
    alpha = 0
    fondo = fondo.copy()
    overlay = pygame.Surface(pantalla.get_size())
    overlay.fill((0, 0, 0))

    while alpha < 255:
        pantalla.blit(fondo, (0, 0))
        overlay.set_alpha(255 - alpha)
        pantalla.blit(overlay, (0, 0))
        pygame.display.flip()
        alpha += 255 / (duracion / clock.tick(60))

def fade_out_zoom(pantalla, personaje_img, fondo, seleccion, duracion=1000):
    clock = pygame.time.Clock()
    alpha = 0
    scale = 1.0
    overlay = pygame.Surface(pantalla.get_size())
    overlay.fill((0, 0, 0))

    while alpha < 255:
        pantalla.blit(fondo, (0, 0))

        # Zoom del personaje seleccionado
        if seleccion == "Masculino":
            x = 350
        else:
            x = 650
        personaje_zoom = pygame.transform.scale(personaje_img, (
            int(personaje_img.get_width() * scale),
            int(personaje_img.get_height() * scale)
        ))
        pantalla.blit(personaje_zoom, (
            int(x + personaje_img.get_width() / 2 - personaje_zoom.get_width() / 2),
            300 + personaje_img.get_height() / 2 - personaje_zoom.get_height() / 2
        ))

        # Fade-out
        overlay.set_alpha(alpha)
        pantalla.blit(overlay, (0, 0))

        pygame.display.flip()
        alpha += 255 / (duracion / clock.tick(60))
        scale += 0.01  # velocidad de zoom


def selection(pantalla):
    #fondo para la seleccion
    fondo_seleccion = pygame.image.load("assets/fondos/seleccion.png").convert()
    fondo_seleccion = pygame.transform.scale(fondo_seleccion, pantalla.get_size())
    fade_in(pantalla, fondo_seleccion)

    x1 = -256  # personaje1 entra desde la izquierda
    x2 = pantalla.get_width()  # personaje2 entra desde la derecha
    texto_alpha = 0  # transparencia del texto

    # Cargar sprites base
    personaje1 = pygame.image.load("player/Base_Masculino.png").convert_alpha()
    personaje2 = pygame.image.load("player/Base_Femenino.png").convert_alpha()
    personaje1 = pygame.transform.scale(personaje1, (256, 256))
    personaje2 = pygame.transform.scale(personaje2, (256, 256))

    seleccion = "Masculino"
    confirmado = False
    clock = pygame.time.Clock()

    while not confirmado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key in [pygame.K_LEFT, pygame.K_a]:
                    seleccion = "Masculino"
                elif evento.key in [pygame.K_RIGHT, pygame.K_d]:
                    seleccion = "Femenino"
                elif evento.key == pygame.K_RETURN:
                    confirmado = True
                    if seleccion == "Masculino":
                        personaje_img = personaje1
                    else:
                        personaje_img = personaje2
                    fade_out_zoom(pantalla, personaje_img, fondo_seleccion, seleccion)
        # Animar entrada de personajes
        if x1 < 350:
            x1 += 10  # velocidad de entrada
        if x2 > 650:
            x2 -= 10
        # Animar aparición del texto
        if texto_alpha < 255:
            texto_alpha += 5

        pantalla.blit(fondo_seleccion, (0,0))
        pantalla.blit(personaje1, (x1, 300))
        pantalla.blit(personaje2, (x2, 300))

        if seleccion == "Masculino":
            pygame.draw.rect(pantalla, (255, 255, 0), (350, 300, 256, 256), 4)
        else:
            pygame.draw.rect(pantalla, (255, 255, 0), (650, 300, 256, 256), 4)

        texto = get_font(20).render("Usa ← → o A/D para elegir. ENTER para confirmar", True, "#000000")
        texto.set_alpha(texto_alpha)
        texto_rect = texto.get_rect(center=(640, 200))
        pantalla.blit(texto, texto_rect)

        pygame.display.flip()
        clock.tick(60)
        
    fade_out_total(pantalla)
    return seleccion

def fade_out_total(pantalla, duracion=1000):
    clock = pygame.time.Clock()
    overlay = pygame.Surface(pantalla.get_size())
    overlay.fill((0, 0, 0))
    alpha = 0
    while alpha < 255:
        overlay.set_alpha(alpha)
        pantalla.blit(overlay, (0, 0))
        pygame.display.flip()
        alpha += 255 / (duracion / clock.tick(60))