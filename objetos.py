import pygame
from musica import reproducir_musica, detener_musica
# Cargar sprites
sprite_basura = pygame.image.load("assets/basura/basura 2.png").convert_alpha()
sprite_drone = pygame.image.load("assets/dron.png").convert_alpha()
sprite_boton = pygame.image.load("assets/boton.png").convert_alpha()
sprite_nube = pygame.image.load("assets/nube.png").convert_alpha()

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
    for frame in frames:
        pantalla.blit(frame, (0, 0))
        pygame.display.update()
        pygame.time.delay(1200)  # ajusta velocidad (100 ms = 10 fps)

    
    reproducir_musica("assets/musica/victoria.mp3", volumen=0.7)
    # Mostrar fondo final con texto
    fondo_color = (30, 30, 60)
    pantalla.fill(fondo_color)

    texto_color = (255, 255, 255)
    sombra_color = (100, 100, 200)
    fuente = pygame.font.Font(None, 80)
    subfuente = pygame.font.Font(None, 40)

    texto = fuente.render("¡Victoria!", True, texto_color)
    sombra = fuente.render("¡Victoria!", True, sombra_color)
    texto_rect = texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2 - 50))
    sombra_rect = sombra.get_rect(center=(texto_rect.centerx + 4, texto_rect.centery + 4))

    subtexto = subfuente.render("Has limpiado el mundo :D ¡Excelente!", True, texto_color)
    subtexto_rect = subtexto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2 + 30))

    pantalla.blit(sombra, sombra_rect)
    pantalla.blit(texto, texto_rect)
    pantalla.blit(subtexto, subtexto_rect)

    pygame.display.update()
    pygame.time.wait(3000)  # espera antes de volver al menú
    detener_musica()

def cargar_drones(tmx_data):
    drones = []
    for obj in tmx_data.objects:
        if obj.name == "d":
            rect = pygame.Rect(obj.x - obj.width // 2, obj.y - obj.height, obj.width, obj.height)
            drones.append(rect)
    return drones

def cargar_boton(tmx_data):
    for obj in tmx_data.objects:
        if obj.name == "b":
            return pygame.Rect(obj.x, obj.y, obj.width, obj.height)
    return None

def cargar_nubes(tmx_data):
    nubes = []
    for obj in tmx_data.objects:
        if obj.name == "n":
            rect = pygame.Rect(obj.x - obj.width // 2, obj.y - obj.height, obj.width, obj.height)
            nubes.append(rect)
    return nubes