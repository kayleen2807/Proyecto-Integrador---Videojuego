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

def victoria(pantalla):
    reproducir_musica("assets/musica/victoria.mp3", volumen=0.7)
    # Colores y fuentes
    fondo_color = (30, 30, 60)  # Azul oscuro mágico
    texto_color = (255, 255, 255)
    sombra_color = (100, 100, 200)
    fuente = pygame.font.Font(None, 80)
    subfuente = pygame.font.Font(None, 40)

    # Fondo
    pantalla.fill(fondo_color)

    # Texto principal con sombra
    texto = fuente.render("¡Victoria!", True, texto_color)
    sombra = fuente.render("¡Victoria!", True, sombra_color)
    texto_rect = texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2 - 50))
    sombra_rect = sombra.get_rect(center=(texto_rect.centerx + 4, texto_rect.centery + 4))
    pantalla.blit(sombra, sombra_rect)
    pantalla.blit(texto, texto_rect)

    # Subtexto
    subtexto = subfuente.render("Has limpiado el mundo :D ¡Excelemte!", True, texto_color)
    subtexto_rect = subtexto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2 + 30))
    pantalla.blit(subtexto, subtexto_rect)
    detener_musica()

    pygame.display.flip()
    pygame.time.wait(5000)  # Espera 3 segundos antes de volver al menú

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