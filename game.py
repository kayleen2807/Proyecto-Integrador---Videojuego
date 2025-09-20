import pygame
import pytmx
import sys
from button import Button
from config import pantalla, get_font
import pygame, pytmx

pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((1280, 720),) #pygame.FULLSCREEN)
pygame.display.set_caption("Menu principal")

#fondo
fondo = pygame.image.load("assets/Background.png")

# Función para cargar fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Pantalla principal del juego
def play():
    zoom = 1.5  # Menor a 1.0 para alejar, mayor a 1.0 para acercar

    pygame.display.set_caption("Play")

    # Cargar mapa
    tmx_data = pytmx.util_pygame.load_pygame("mapas/nivel1_mapa.tmx")

    # Cargar colisiones desde objetos del mapa
    colisiones = []
    for obj in tmx_data.objects:
        colisiones.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    # Personaje
    # Buscar objeto llamado "player_start"
    for obj in tmx_data.objects:
        if obj.name == "player_start":
            personaje = pygame.Rect(obj.x, obj.y, 24, 24)  # Más pequeño
            break

    vel_y = 0
    en_el_suelo = False
    gravedad = 0.4

    while True:
        mouse_pos = pygame.mouse.get_pos()
        pantalla.fill("black")

        velocidad_base = 2.4
        velocidad = velocidad_base / zoom

        # Movimiento horizontal
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            personaje.x -= velocidad
        if keys[pygame.K_RIGHT]:
            personaje.x += velocidad

        # Colisiones horizontales
        for rect in colisiones:
            if personaje.colliderect(rect):
                if keys[pygame.K_LEFT]:
                    personaje.left = rect.right
                elif keys[pygame.K_RIGHT]:
                    personaje.right = rect.left

        # Salto
        if keys[pygame.K_SPACE] and en_el_suelo:
            vel_y = -12.90 / zoom
            en_el_suelo = False

        # Gravedad
        vel_y += gravedad
        personaje.y += vel_y

        # Colisiones verticales
        en_el_suelo = False
        for rect in colisiones:
            if personaje.colliderect(rect):
                if vel_y > 0:
                    personaje.bottom = rect.top
                    vel_y = 0
                    en_el_suelo = True
                elif vel_y < 0:
                    personaje.top = rect.bottom
                    vel_y = 0

        # Recalcular cámara
        camara_x = personaje.x - pantalla.get_width() // 2 + personaje.width // 2
        camara_y = personaje.y - (pantalla.get_height() / zoom) // 2 + personaje.height // 2

        #  Limitar cámara para que no se salga del mapa
        map_width_px = tmx_data.width * tmx_data.tilewidth
        map_height_px = tmx_data.height * tmx_data.tileheight
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

        # Dibujar personaje
        pygame.draw.rect(pantalla, (0, 255, 0), pygame.Rect(
            int((personaje.x - camara_x) * zoom),
            int((personaje.y - camara_y) * zoom),
            int(personaje.width * zoom),
            int(personaje.height * zoom)
        ))

        # Botón ATRÁS
        boton_atras = Button(image=None, pos=(640, 460), text_input="ATRAS", font=get_font(15), base_color="White", hovering_color="Blue")
        boton_atras.changeColor(mouse_pos)
        boton_atras.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_atras.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()
