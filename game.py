import pygame
import pytmx
import sys
from selection_screen import selection
from button import Button
from config import pantalla, get_font
from selection_player import Personaje
import pygame, pytmx

pygame.init()

# Configuración de pantalla
pantalla = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
pygame.display.set_caption("Menu principal")

#fondo
fondo = pygame.image.load("assets/Background.png")
nfondo = pygame.image.load("assets/Fondo.png")

# Función para cargar fuente
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

# Pantalla principal del juego
def play():
    pygame.display.set_caption("Play")
    zoom = 1.5
    gravedad = 0.4
    vel_y = 0
    en_el_suelo = False

    nombre = selection(pantalla)  # "Masculino" o "Femenino"
    tmx_data = pytmx.util_pygame.load_pygame("mapas/nivel1_mapa.tmx")
    colisiones = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects]

    for obj in tmx_data.objects:
        if obj.name == "player_start":
            jugador = Personaje(nombre, obj.x, obj.y)
            break

    clock = pygame.time.Clock()
    while True:
        pantalla.blit(nfondo, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        velocidad = 4.2 / zoom

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            jugador.rect.x -= velocidad
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            jugador.rect.x += velocidad

        for rect in colisiones:
            if jugador.rect.colliderect(rect):
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    jugador.rect.left = rect.right
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    jugador.rect.right = rect.left

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and en_el_suelo:
            vel_y = -12.5 / zoom
            en_el_suelo = False

        vel_y += gravedad
        jugador.rect.y += vel_y

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

        camara_x = jugador.rect.x - pantalla.get_width() // 2 + jugador.rect.width // 2
        camara_y = jugador.rect.y - pantalla.get_height() // 2 + jugador.rect.height // 2

        map_width_px = tmx_data.width * tmx_data.tilewidth
        map_height_px = tmx_data.height * tmx_data.tileheight
        visible_width = pantalla.get_width() / zoom
        visible_height = pantalla.get_height() / zoom

        camara_x = max(0, min(camara_x, map_width_px - visible_width))
        camara_y = max(0, min(camara_y, map_height_px - visible_height))

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

        jugador.actualizar_estado(keys, en_el_suelo, vel_y)
        jugador.dibujar(pantalla, camara_x, camara_y, zoom)

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

        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

