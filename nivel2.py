import pygame, pytmx, sys
from selection_screen import selection
from button import Button
from config import pantalla, get_font
from selection_player import Personaje
from pause_menu import mostrar_menu_pausa
from game_over import pantalla_gameover
from juego import fade_in_total, nfondo
from musica import reproducir_musica, detener_musica, pausar_musica, continuar_musica

# Pantalla principal del juego:
def jugar_nivel2(pantalla, personaje):
    from vidas import dibujar_hud_vidas
    pygame.display.set_caption("Play")
    reproducir_musica ("assets/musica/music_game.mp3", volumen=0.5)
    zoom = 1.5
    gravedad = 0.4
    vel_y = 0
    en_el_suelo = False
    vidas = 3
    pausado = False

    nombre = personaje.lower()
    fondo_mapa_preview = pygame.image.load("assets/fondos/fondo_nvl2.png").convert()
    fondo_mapa_preview = pygame.transform.scale(fondo_mapa_preview, pantalla.get_size())
    fade_in_total(pantalla, fondo_mapa_preview)

    tmx_data = pytmx.util_pygame.load_pygame("mapas/Nvl2(c).tmx")
    colisiones = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects]


    for obj in tmx_data.objects:
        if obj.name == "player_start":
            jugador = Personaje(nombre, obj.x, obj.y)
            break

    # Botón de pausa:
    boton_pausa = Button(image = pygame.image.load("assets/pausa.png"), image_hover = None, pos=(1220, 50), text_input="", font=get_font(1), base_color="#FFFFFF", hovering_color="Gray")
    clock = pygame.time.Clock()

    while True:
        pantalla.blit(fondo_mapa_preview, (0, 0))
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
                    detener_musica()
                    from game_over import pantalla_gameover
                    return pantalla_gameover(pantalla, nombre)

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
            
            # Dibujar HUD de vidas
            dibujar_hud_vidas(pantalla, vidas)

        jugador.actualizar_estado(keys, en_el_suelo, vel_y)
        jugador.dibujar(pantalla, camara_x, camara_y, zoom)

        # Botón de pausa
        boton_pausa.changeColor(mouse_pos)
        boton_pausa.update(pantalla)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                detener_musica()
                return "salir"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = not pausado
                    if pausado:
                        pausar_musica()
                    else:
                        continuar_musica()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_pausa.checkForInput(mouse_pos):
                    pausado = not pausado
                    if pausado:
                        pausar_musica()
                    else:
                        continuar_musica()

                if pausado:
                    # Mostrar botones del menú de pausa
                    boton_continuar, boton_reiniciar, boton_menu = mostrar_menu_pausa(pantalla)

                    if boton_continuar and boton_continuar.checkForInput(mouse_pos):
                        pausado = False
                        continuar_musica()

                    elif boton_menu and boton_menu.checkForInput(mouse_pos):
                        detener_musica()
                        return "menu"

                    elif boton_reiniciar and boton_reiniciar.checkForInput(mouse_pos):
                        reproducir_musica("assets/musica/music_game.mp3", volumen=0.5)
                        return "reiniciar"

        # Renderizado constante del menú de pausa
        if pausado:
            boton_continuar, boton_reiniciar, boton_menu = mostrar_menu_pausa(pantalla)



        pygame.display.flip()
        clock.tick(60)