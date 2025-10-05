import pygame
frames = [
    pygame.image.load("assets/gameover/g1.png"),
    pygame.image.load("assets/gameover/g2.png"),
    pygame.image.load("assets/gameover/g3.png"),
    pygame.image.load("assets/gameover/g4.png"),
    pygame.image.load("assets/gameover/g5.png"),
    pygame.image.load("assets/gameover/m1.png"),
    pygame.image.load("assets/gameover/g2.png"),
    pygame.image.load("assets/gameover/g3.png"),
    pygame.image.load("assets/gameover/g4.png"),
    pygame.image.load("assets/gameover/g5.png"),
    # Agrega todos los que tengas
]
def reproducir_animacion(pantalla, frames, posicion, tiempo_por_frame=100):
    reloj = pygame.time.Clock()
    frame_actual = 0
    tiempo_total = len(frames) * tiempo_por_frame
    tiempo_inicio = pygame.time.get_ticks()

    while pygame.time.get_ticks() - tiempo_inicio < tiempo_total:
        pantalla.fill((0, 0, 0))  # Fondo negro o el que tú quieras
        pantalla.blit(frames[frame_actual], posicion)
        pygame.display.flip()

        pygame.time.delay(tiempo_por_frame)
        frame_actual = (frame_actual + 1) % len(frames)
        reloj.tick(60)