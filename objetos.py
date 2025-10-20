import pygame
from musica import reproducir_musica, detener_musica
# Cargar sprites
sprite_basura = pygame.image.load("assets/basura/basura 2.png").convert_alpha()
sprite_portal_abierto = pygame.image.load("assets/portal.png").convert_alpha()

def cargar_basura(tmx_data):
    basura = []
    for obj in tmx_data.objects:
        if obj.name == "b":
            rect = pygame.Rect(obj.x - obj.width // 2, obj.y - obj.height, obj.width, obj.height)
            basura.append(rect)
    return basura

def cargar_portal(tmx_data):
    for obj in tmx_data.objects:
        if obj.name == "portal":
            return pygame.Rect(obj.x, obj.y, obj.width, obj.height)
    return None

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

def dibujar_portal(pantalla, portal, sprite_abierto, items_recogidos, total, camara_x, camara_y, zoom):
    if portal and items_recogidos == total:
        # Escalar el sprite del portal según el zoom
        sprite_escalado = pygame.transform.scale(sprite_abierto, (
            int(sprite_abierto.get_width() * zoom),
            int(sprite_abierto.get_height() * zoom)
        ))

        # Calcular posición centrada sobre el rect del portal
        pantalla.blit(sprite_escalado, (
            int((portal.centerx - camara_x) * zoom - sprite_escalado.get_width() // 2),
            int((portal.bottom - camara_y) * zoom - sprite_escalado.get_height())
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

def verificar_victoria(jugador, portal, items_recogidos, total):
    colision = jugador.rect.colliderect(portal)
    completo = items_recogidos == total
    return colision and completo

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