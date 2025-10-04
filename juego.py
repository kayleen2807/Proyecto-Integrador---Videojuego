import pygame
import pytmx
import sys
from selection_screen import selection
from button import Button
from config import pantalla, get_font
from selection_player import Personaje
from pause_menu import mostrar_menu_pausa
from game_over import game_over

#inicio para pygame
pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((1280, 720)) #, pygame.FULLSCREEN)
pygame.display.set_caption("Menu principal")

#fondo para el menu principal
fondo = pygame.image.load("assets/fondos/menu_fondo.png").convert()
fondo = pygame.transform.scale(fondo, pantalla.get_size())

#fondo para el nivel 1
pantalla.blit(fondo, (0, 0))

nfondo = pygame.image.load("assets/fondos/Fondo.png")

# Función para cargar fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#transicion
def fade_in_total(pantalla, fondo, duracion=1000):
    clock = pygame.time.Clock()
    overlay = pygame.Surface(pantalla.get_size())
    overlay.fill((0, 0, 0))
    alpha = 255
    while alpha > 0:
        pantalla.blit(fondo, (0, 0))
        overlay.set_alpha(alpha)
        pantalla.blit(overlay, (0, 0))
        pygame.display.flip()
        alpha -= 255 / (duracion / clock.tick(60))

# Pantalla principal del juego para jugar
def play():
    from objetos import recolectar_items, dibujar_items, dibujar_portal, sprite_basura, sprite_portal_abierto, verificar_victoria, cargar_basura, cargar_portal, victoria
    pygame.display.set_caption("Play")
    zoom = 1.5
    gravedad = 0.4
    vel_y = 0
    en_el_suelo = False
    vidas = 3
    pausado = False

    nombre = selection(pantalla)  # "Masculino" o "Femenino"
    fondo_mapa_preview = pygame.image.load("assets/fondos/Fondo.png").convert()
    fondo_mapa_preview = pygame.transform.scale(fondo_mapa_preview, pantalla.get_size())
    fade_in_total(pantalla, fondo_mapa_preview)

    tmx_data = pytmx.util_pygame.load_pygame("mapas/nivel1_mapa.tmx")
    colisiones = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects]
    basura = cargar_basura(tmx_data)
    total_basura = len(basura)
    recogidos = 0
    portal = cargar_portal(tmx_data)

    for obj in tmx_data.objects:
        if obj.name == "player_start":
            jugador = Personaje(nombre, obj.x, obj.y)
            break

    boton_pausa = Button(image=None, image_hover=None, pos=(1200, 50), text_input="||", font=get_font(40), base_color="#FFFFFF", hovering_color="Gray")
    clock = pygame.time.Clock()

    while True:
        pantalla.blit(nfondo, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        velocidad = 4.2 / zoom

        if not pausado:
            # Movimiento horizontal
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                jugador.rect.x -= velocidad
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                jugador.rect.x += velocidad

            # Colisión horizontal
            for rect in colisiones:
                if jugador.rect.colliderect(rect):
                    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                        jugador.rect.left = rect.right
                    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        jugador.rect.right = rect.left

            # Salto
            if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and en_el_suelo:
                vel_y = -12.5 / zoom
                en_el_suelo = False

            # Gravedad y movimiento vertical
            vel_y += gravedad
            jugador.rect.y += vel_y

            # Colisión vertical
            en_el_suelo = False
            for rect in colisiones:
                if jugador.rect.colliderect(rect):
                    if vel_y > 0:
                        jugador.rect.bottom = rect.top
                        vel_y = 0
                        en_el_suelo = True
                    elif vel_y < 0:
                        jugador.rect.top = rect.bottom
                        vel_y = 0

            # Recolectar basura
            recogidos += recolectar_items(jugador, basura)

            # Verificar caída fuera del mapa
            map_height_px = tmx_data.height * tmx_data.tileheight
            if jugador.rect.y > map_height_px:
                vidas -= 1
                if vidas > 0:
                    for obj in tmx_data.objects:
                        if obj.name == "player_start":
                            jugador.rect.x = obj.x
                            jugador.rect.y = obj.y
                            vel_y = 0
                            break
                else:
                    return game_over(pantalla)

            # Cámara
            camara_x = jugador.rect.x - pantalla.get_width() // 2 + jugador.rect.width // 2
            camara_y = jugador.rect.y - pantalla.get_height() // 2 + jugador.rect.height // 2
            map_width_px = tmx_data.width * tmx_data.tilewidth
            visible_width = pantalla.get_width() / zoom
            visible_height = pantalla.get_height() / zoom
            camara_x = max(0, min(camara_x, map_width_px - visible_width))
            camara_y = max(0, min(camara_y, map_height_px - visible_height))

            # Dibujar mapa
            for layer in tmx_data.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid in layer:
                        if gid == 0:
                            continue
                        tile = tmx_data.get_tile_image_by_gid(gid)
                        if tile:
                            pantalla.blit(pygame.transform.smoothscale(tile, (
                                int(tmx_data.tilewidth * zoom),
                                int(tmx_data.tileheight * zoom)
                            )), (
                                int((x * tmx_data.tilewidth - camara_x) * zoom),
                                int((y * tmx_data.tileheight - camara_y) * zoom)
                            ))

            # Dibujar basura y portal
            dibujar_items(pantalla, basura, sprite_basura, camara_x, camara_y, zoom)
            dibujar_portal(pantalla, portal, sprite_portal_abierto, recogidos, total_basura, camara_x, camara_y, zoom)

            # Verificar victoria
            if verificar_victoria(jugador, portal, recogidos, total_basura):
                return victoria(pantalla)

        jugador.actualizar_estado(keys, en_el_suelo, vel_y)
        jugador.dibujar(pantalla, camara_x, camara_y, zoom)

        # Botón de pausa
        boton_pausa.changeColor(mouse_pos)
        boton_pausa.update(pantalla)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = not pausado
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_pausa.checkForInput(mouse_pos):
                    pausado = not pausado

        # Menú de pausa
        if pausado:
            boton_continuar, boton_reiniciar, boton_menu = mostrar_menu_pausa(pantalla)
            if boton_continuar and boton_continuar.checkForInput(mouse_pos):
                pausado = False
            elif boton_menu and boton_menu.checkForInput(mouse_pos):
                return "menu"
            elif boton_reiniciar and boton_reiniciar.checkForInput(mouse_pos):
                return play()

        # HUD
        texto_vidas = get_font(25).render(f"Vidas: {vidas}", True, "White")
        pantalla.blit(texto_vidas, (30, 30))
        texto_basura = get_font(25).render(f"Basura: {recogidos}/{total_basura}", True, "White")
        pantalla.blit(texto_basura, (30, 60))

        pygame.display.flip()
        clock.tick(60)