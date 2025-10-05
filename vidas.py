import pygame

sprites_vidas = [
    pygame.image.load("assets/vidas/Muerte.png").convert_alpha(),
    pygame.image.load("assets/vidas/Vidas_Bajo.png").convert_alpha(),
    pygame.image.load("assets/vidas/Vidas_Medio.png").convert_alpha(),
    pygame.image.load("assets/vidas/Vidas_Completo.png").convert_alpha(),
]

def dibujar_hud_vidas(pantalla, vidas):
    sprite_vida = sprites_vidas[max(0, min(vidas, len(sprites_vidas) - 1))]
    pantalla.blit(sprite_vida, (20, 20))