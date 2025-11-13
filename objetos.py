import pygame
from musica import reproducir_musica, detener_musica
# Cargar sprites
sprite_basura = pygame.image.load("assets/basura/basura 2.png").convert_alpha()
sprite_humo = pygame.image.load("mapas/humo.png").convert_alpha()

def animacion_intro(pantalla, personaje):
     # Cargar animación del personaje
    ruta_frames = f"assets/intro/nivel1/{personaje}/"
    total_frames = 10
    frames = []

    for i in range(total_frames):
        frame = pygame.image.load(f"{ruta_frames}intro_{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, pantalla.get_size())
        frames.append(frame)

    pantalla_ancho, pantalla_alto = pantalla.get_size()
    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)

    # Reproducir animación una sola vez
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)

def animacion_intro2(pantalla, personaje):
     # Cargar animación del personaje
    ruta_frames = f"assets/intro/nivel2/{personaje}/"
    total_frames = 10
    frames = []

    for i in range(total_frames):
        frame = pygame.image.load(f"{ruta_frames}intro_{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, pantalla.get_size())
        frames.append(frame)

    pantalla_ancho, pantalla_alto = pantalla.get_size()
    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)

    # Reproducir animación una sola vez
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)

def animacion_intro3(pantalla, personaje):
     # Cargar animación del personaje
    ruta_frames = f"assets/intro/nivel2/{personaje}/"
    total_frames = 10
    frames = []

    for i in range(total_frames):
        frame = pygame.image.load(f"{ruta_frames}intro_{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, pantalla.get_size())
        frames.append(frame)

    pantalla_ancho, pantalla_alto = pantalla.get_size()
    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)

    # Reproducir animación una sola vez
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)


def cargar_humos(tmx_data):
    humos = []
    for obj in tmx_data.objects:
        if obj.name == "h":
            rect = pygame.Rect(obj.x - obj.width // 2, obj.y - obj.height, obj.width, obj.height)
            humos.append(rect)
    return humos


def cargar_basura(tmx_data):
    basura = []
    for obj in tmx_data.objects:
        if obj.name == "b":
            rect = pygame.Rect(obj.x - obj.width // 2, obj.y - obj.height, obj.width, obj.height)
            basura.append(rect)
    return basura

def dibujar_items(pantalla, items, sprite, camara_x, camara_y, zoom):
    sprite_escalado = pygame.transform.scale(sprite, (
        int(sprite.get_width() * zoom),
        int(sprite.get_height() * zoom)
    ))
    for item in items:
        pantalla.blit(sprite_escalado, (
            int((item.centerx - camara_x) * zoom - sprite_escalado.get_width() // 2),
            int((item.bottom - camara_y) * zoom - sprite_escalado.get_height())
        ))


def recolectar_items(jugador, basura):
    recogidos = 0
    basura_restante = []
    for rect in basura:
        if jugador.rect.colliderect(rect):
            recogidos += 1
        else:
            basura_restante.append(rect)
    basura[:] = basura_restante  # Actualiza la lista original sin romper el bucle
    return recogidos

def verificar_victoria(jugador, items_recogidos, total):
    completo = items_recogidos == total
    return completo

def victoria(pantalla, personaje):
    # Cargar animación del personaje
    ruta_frames = f"assets/victoria/nivel1/{personaje}/"
    total_frames = 7  # ajusta según tu animación
    frames = []

    for i in range(total_frames):
        frame = pygame.image.load(f"{ruta_frames}lv1_{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, pantalla.get_size())
        frames.append(frame)

    pantalla_ancho, pantalla_alto = pantalla.get_size()
    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)

    # Reproducir animación una sola vez
    reproducir_musica("assets/musica/victoria.mp3", volumen=0.7, loop=0)
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)

    pygame.display.update()
    pygame.time.wait(3000)  # espera antes de volver al menú
    detener_musica()

def victoria2(pantalla, personaje):
    # Cargar animación del personaje
    ruta_frames = f"assets/victoria/nivel2/{personaje}/"
    total_frames = 4  # ajusta según tu animación
    frames = []

    for i in range(total_frames):
        frame = pygame.image.load(f"{ruta_frames}lv2_{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, pantalla.get_size())
        frames.append(frame)

    pantalla_ancho, pantalla_alto = pantalla.get_size()
    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)

    # Reproducir animación una sola vez
    reproducir_musica("assets/musica/victoria.mp3", volumen=0.7, loop=0)
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)

    pygame.display.update()
    pygame.time.wait(3000)  # espera antes de volver al menú
    detener_musica()

def victoria3(pantalla, personaje):
    # Cargar animación del personaje
    ruta_frames = f"assets/victoria/nivel3/{personaje}/"
    total_frames = 4  # ajusta según tu animación
    frames = []

    for i in range(total_frames):
        frame = pygame.image.load(f"{ruta_frames}lv3_{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, pantalla.get_size())
        frames.append(frame)

    pantalla_ancho, pantalla_alto = pantalla.get_size()
    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)

    # Reproducir animación una sola vez
    reproducir_musica("assets/musica/victoria.mp3", volumen=0.7, loop=0)
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)

    pygame.display.update()
    pygame.time.wait(3000)  # espera antes de volver al menú
    detener_musica()

    