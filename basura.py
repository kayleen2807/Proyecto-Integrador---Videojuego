import pygame

sprites_basura = [
    pygame.image.load("assets/basura/Contador_Basura_0.png").convert_alpha(),
    pygame.image.load("assets/basura/Contador_Basura_1.png").convert_alpha(),
    pygame.image.load("assets/basura/Contador_Basura_2.png").convert_alpha(),
    pygame.image.load("assets/basura/Contador_Basura_3.png").convert_alpha(),
    pygame.image.load("assets/basura/Contador_Basura_4.png").convert_alpha(),
    pygame.image.load("assets/basura/Contador_Basura_5.png").convert_alpha(),
    pygame.image.load("assets/basura/Contador_Basura_6.png").convert_alpha(),
    
]
def dibujar_hud_basura(pantalla, recogidos, total_basura):
    # Mostrar basura recolectada con sprite visual
    sprite_basura = sprites_basura[max(0, min(recogidos, len(sprites_basura) - 1))]
    pantalla.blit(sprite_basura, (20, 80))  # Ajusta la posición como prefieras