import pygame

# Cargar frames por personaje
frames_masculino = [
    pygame.image.load("assets/gameover/m1.png"),
    pygame.image.load("assets/gameover/m2.png"),
    pygame.image.load("assets/gameover/m3.png"),
    pygame.image.load("assets/gameover/m4.png"),
    pygame.image.load("assets/gameover/m5.png")
]

frames_femenino = [
    pygame.image.load("assets/gameover/ff1.png"),
    pygame.image.load("assets/gameover/ff2.png"),
    pygame.image.load("assets/gameover/ff3.png"),
    pygame.image.load("assets/gameover/ff4.png"),
    pygame.image.load("assets/gameover/ff55.png")
]

# Diccionario para acceder por nombre
frames_por_personaje = {
    "masculino": frames_masculino,
    "femenino": frames_femenino
}

# Función para reproducir animación
def reproducir_animacion(pantalla, personaje, posicion=(100, 0), tiempo_por_frame=300):
    frames = frames_por_personaje.get(personaje)
    if not frames:
        print(f"No hay animación para el personaje: {personaje}")
        return

    reloj = pygame.time.Clock()
    frame_actual = 0
    tiempo_total = len(frames) * tiempo_por_frame
    tiempo_inicio = pygame.time.get_ticks()

    while pygame.time.get_ticks() - tiempo_inicio < tiempo_total:
        for event in pygame.event.get():  # Evita que se congele la ventana
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pantalla.fill((0, 0, 0))  # Fondo negro
        pantalla.blit(frames[frame_actual], posicion)
        pygame.display.flip()

        pygame.time.delay(tiempo_por_frame)
        frame_actual = (frame_actual + 1) % len(frames)
        reloj.tick(60)