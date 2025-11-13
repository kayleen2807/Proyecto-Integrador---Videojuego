import pygame, pytmx, sys, random
from selection_screen import selection
from button import Button
from config import pantalla, get_font
from selection_player import Personaje
from pause_menu import mostrar_menu_pausa
from juego import fade_in_total, nfondo
from musica import reproducir_musica, detener_musica, pausar_musica, continuar_musica

# Pantalla principal del juego:
def jugar_nivel2(pantalla, personaje):
    from vidas import dibujar_hud_vidas
    from objetos import dibujar_items, sprite_humo, cargar_humos
    from game_over import pantalla_gameover
    pygame.display.set_caption("Play")
    reproducir_musica ("assets/musica/music_game.mp3", volumen=0.3, loop=-1)

    #funcion para detectar el rango
    def esta_en_rango(nube_rect, jugador_rect, rango=350):
        distancia = abs(nube_rect.centerx - jugador_rect.centerx)
        return distancia <= rango
    
    #Clase para los rayos:
    class Proyectil(pygame.sprite.Sprite):
        def __init__(self, x, y, direccion):
            super().__init__()
            self.image = pygame.image.load("assets/rayo.png").convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))
            self.velocidad = 5 * direccion  # dirección: -1 arriba, 1 abajo

        def update(self):
            self.rect.y += self.velocidad
            if self.rect.bottom < 0 or self.rect.top > pantalla.get_height():
                self.kill()

    #Cargar nubes:
    def cargar_nubes(tmx_data):
        nubes = []
        for obj in tmx_data.objects:
            if obj.name == "n":
                rect = pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height))
                nubes.append(rect)
        return nubes
    
    zoom = 1.5
    gravedad = 0.4
    vel_y = 0
    en_el_suelo = False
    pausado = False

    nombre = personaje.lower()
    fondo_mapa_preview = pygame.image.load("assets/fondos/fondo_nvl2.png").convert()
    fondo_mapa_preview = pygame.transform.scale(fondo_mapa_preview, pantalla.get_size())
    fade_in_total(pantalla, fondo_mapa_preview)

    tmx_data = pytmx.util_pygame.load_pygame("mapas/Nvl2(c).tmx")
    colisiones = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects]
    nubes = cargar_nubes(tmx_data)
    nube_imagen = pygame.image.load("mapas/nube.png").convert_alpha()
    humos = cargar_humos(tmx_data)

    grupo_proyectiles = pygame.sprite.Group()

    #Cooldown para que no dispare muy rápido:
    cooldowns = {id(nube_rect): 0 for nube_rect in nubes}


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
                jugador.vidas -= 1
                if jugador.vidas > 0:
                    for obj in tmx_data.objects:
                        if obj.name == "player_start":
                            jugador.rect.x = obj.x
                            jugador.rect.y = obj.y
                            vel_y = 0
                            break
                else:
                    detener_musica()
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
            
            if jugador.vidas <= 0:
                detener_musica()
                return pantalla_gameover(pantalla, nombre)
            
            #Dibujar humo
            dibujar_items(pantalla, humos, sprite_humo, camara_x, camara_y, zoom)

             #eliminar humos
            if keys[pygame.K_e]:
                for humo in humos[:]:  # copia de la lista para evitar errores al eliminar
                    if jugador.rect.colliderect(humo):
                        humos.remove(humo)
                        break  # elimina solo uno por pulsación

            # Dibujar nubes y disparar si el jugador está cerca
            for nube_rect in nubes:
                pantalla.blit(pygame.transform.scale(nube_imagen, (
                    int(nube_imagen.get_width() * zoom),
                    int(nube_imagen.get_height() * zoom)
                )), (
                    int((nube_rect.x - camara_x) * zoom),
                    int((nube_rect.y - camara_y) * zoom)
                ))

                if esta_en_rango(nube_rect, jugador.rect):
                    if cooldowns[id(nube_rect)] <= 0:
                        direccion = 1
                        spawn_x = nube_rect.centerx
                        spawn_y = nube_rect.bottom  # justo debajo de la nube
                        proyectil = Proyectil(spawn_x, spawn_y, direccion)
                        grupo_proyectiles.add(proyectil)
                        cooldowns[id(nube_rect)] = random.randint(120, 240)# espera aleatorio entre disparos

            # Actualizar cooldowns
            for key in cooldowns:
                if cooldowns[key] > 0:
                    cooldowns[key] -= 1

            # Actualizar y dibujar proyectiles
            grupo_proyectiles.update()
            for proyectil in grupo_proyectiles:
                scaled = pygame.transform.scale(proyectil.image, (
                    int(proyectil.image.get_width() * zoom),
                    int(proyectil.image.get_height() * zoom)
                ))
                pantalla.blit(scaled, (
                    int((proyectil.rect.x - camara_x) * zoom),
                    int((proyectil.rect.y - camara_y) * zoom)
                ))

            if pygame.sprite.spritecollide(jugador, grupo_proyectiles, True):
                jugador.recibir_daño()

            jugador.update()

            # Dibujar HUD de vidas
            dibujar_hud_vidas(pantalla, jugador.vidas)

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