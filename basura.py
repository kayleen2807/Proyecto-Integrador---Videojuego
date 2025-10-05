import pygame

sprites_basura = [
    pygame.image.load("assets/basura/basura_0.png").convert_alpha(),
    pygame.image.load("assets/basura/basura_1.png").convert_alpha(),
    pygame.image.load("assets/basura/basura_2.png").convert_alpha(),
    pygame.image.load("assets/basura/basura_3.png").convert_alpha(),
    pygame.image.load("assets/basura/basura_4.png").convert_alpha(),
    pygame.image.load("assets/basura/basura_5.png").convert_alpha(),
    pygame.image.load("assets/basura/basura_6.png").convert_alpha()
    # Agrega más según el total posible
]
def dibujar_hud_basura(pantalla, recogidos, total_basura):
    # Mostrar basura recolectada con sprite visual
    sprite_basura = sprites_basura[max(0, min(recogidos, len(sprites_basura) - 1))]
    pantalla.blit(sprite_basura, (20, 20))  # Ajusta la posición como prefieras

    # También puedes mostrar texto si quieres reforzar el contador
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"{recogidos}/{total_basura}", True, (255, 255, 255))
    pantalla.blit(texto, (30 + sprite_basura.get_width(), 30))  # Al lado del sprite