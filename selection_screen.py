import pygame
from config import get_font
def selection(pantalla):
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

        pantalla.fill((30, 30, 30))
        pantalla.blit(personaje1, (200, 250))
        pantalla.blit(personaje2, (500, 250))

        if seleccion == "Masculino":
            pygame.draw.rect(pantalla, (255, 255, 0), (200, 250, 256, 256), 4)
        else:
            pygame.draw.rect(pantalla, (255, 255, 0), (500, 250, 256, 256), 4)

        texto = get_font(30).render("Usa ← → o A/D para elegir. ENTER para confirmar", True, "#ebe8e2")
        texto_rect = texto.get_rect(center=(640, 100))
        pantalla.blit(texto, texto_rect)

        pygame.display.flip()
        clock.tick(60)

    return seleccion
