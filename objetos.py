import pygame

# Cargar sprites
sprite_basura = pygame.image.load("assets/basura/Basura.png").convert_alpha()
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
    return portal and jugador.rect.colliderect(portal) and items_recogidos == total

def victoria(pantalla):
    fuente = pygame.font.Font(None, 60)
    texto = fuente.render("¡Victoria!", True, (255, 255, 255))
    pantalla.fill((0, 0, 0))
    pantalla.blit(texto, (100, 100))
    pygame.display.flip()
    pygame.time.wait(3000)