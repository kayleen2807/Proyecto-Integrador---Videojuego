from config import pantalla, get_font
from button import Button
from musica import reproducir_musica, detener_musica, continuar_musica, pausar_musica
import pygame
import config
#idioma
def cargar_img(ruta_relativa):
    ruta = f"assets/{config.idioma}/{ruta_relativa}"
    return pygame.image.load(ruta).convert_alpha()

# Pantalla de inicio
def inicio():
    # Cargar frames del fondo animado
    pantalla_ancho, pantalla_alto = pantalla.get_size()
    fondos_animados = []
    total_frames = 4
    for i in range(total_frames):
        frame = pygame.image.load(f"assets/fondos/menu_{i}.png").convert()
        frame_escalado = pygame.transform.scale(frame, (pantalla_ancho, pantalla_alto))
        fondos_animados.append(frame_escalado)

    frame_actual = 0
    reloj = pygame.time.Clock()

    pygame.display.set_caption("Inicio")
    while True:
        #menu animado
        pantalla.blit(fondos_animados[frame_actual], (0, 0))
        frame_actual = (frame_actual + 1) % total_frames
        mouse_pos = pygame.mouse.get_pos()

        #boton de empezar que lleva al menu principal
        boton_empezar = Button(image = pygame.image.load("assets/empezar_b2.png"), image_hover= pygame.image.load("assets/empezar_b2_h.png"), pos=(650, 400), text_input="", font=get_font(60), base_color="Black", hovering_color="Grey")
        boton_empezar.changeColor(mouse_pos)
        boton_empezar.update(pantalla)

        #cerrar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_empezar.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()
        reloj.tick(3)  # Controla la velocidad de animación 

# Menú principal
def menu_prin(pantalla):
    pygame.display.set_caption("Menu principal")
    # Cargar frames del fondo animado
    pantalla_ancho, pantalla_alto = pantalla.get_size()
    fondos_animados = []
    total_frames = 4
    for i in range(total_frames):
        frame = pygame.image.load(f"assets/fondos/menu_{i}.png").convert()
        frame_escalado = pygame.transform.scale(frame, (pantalla_ancho, pantalla_alto))
        fondos_animados.append(frame_escalado)

    reproducir_musica ("assets/musica/music_menu.mp3", volumen=0.3, loop=-1)  
    title = pygame.image.load("assets/gatods.png")

    #botones play, opciones y salir
    boton_play = Button(image=cargar_img("boton_menu/boton_jugar.png"), image_hover=cargar_img("boton_menu/boton_jugar_h.png"), pos=(650, 280), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_opciones = Button(image=cargar_img("boton_menu/boton_opciones.png"), image_hover=cargar_img("boton_menu/boton_opciones_h.png"), pos=(650, 420), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_salir = Button(image=cargar_img("boton_menu/boton_Salir.png"), image_hover=cargar_img("boton_menu/boton_Salir_h.png"), pos=(652, 558), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

    frame_actual = 0
    reloj = pygame.time.Clock()

    # Bucle del menú
    while True:
        #menu animado
        pantalla.blit(fondos_animados[frame_actual], (0, 0))
        frame_actual = (frame_actual + 1) % total_frames
        pantalla.blit(title, (350, 70))
        mouse_pos = pygame.mouse.get_pos()


        for boton in [boton_play, boton_opciones, boton_salir]:
            boton.changeColor(mouse_pos)
            boton.update(pantalla)

        #acciones de los botones
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_play.checkForInput(mouse_pos):
                    for alpha in range(0, 255, 5):
                        overlay = pygame.Surface((pantalla_ancho, pantalla_alto))
                        overlay.set_alpha(alpha)
                        overlay.fill((0, 0, 0))
                        pantalla.blit(overlay, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(10)
                    return "nivel"
                elif boton_opciones.checkForInput(mouse_pos):
                    return "opciones"
                elif boton_salir.checkForInput(mouse_pos):
                    detener_musica()
                    return "salir"

        pygame.display.update()
        reloj.tick(3)  # Controla la velocidad de animación 

# Pantalla de opciones
def opciones():
    global musica_activa
    pygame.display.set_caption("Opciones")
    while True:
        fondo_mapa_preview = pygame.image.load("assets/opciones/fondo_opts.png").convert()
        fondo_mapa_preview = pygame.transform.scale(fondo_mapa_preview, pantalla.get_size())
        pantalla.blit(fondo_mapa_preview, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # título opciones
        opc = cargar_img("pantalla_opc/opts.png")
        pantalla.blit(opc, (440, 100))

        # selección de idioma
        lengua = cargar_img("pantalla_opc/Lenguage.png")
        pantalla.blit(lengua, (380, 280))
        bandera1 = Button(image=pygame.image.load("assets/opciones/bandera_e.png"), image_hover=pygame.image.load("assets/opciones/bandera_e_h.png"), pos=(700, 300), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        bandera2 = Button(image=pygame.image.load("assets/opciones/bandera_i.png"), image_hover=pygame.image.load("assets/opciones/bandera_i_h.png"), pos=(840, 300), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        for bandera in [bandera1, bandera2]:
            bandera.changeColor(mouse_pos)
            bandera.update(pantalla)

        # música
        music = cargar_img("pantalla_opc/Music.png")
        pantalla.blit(music, (380, 380))
        icono1 = Button(image=pygame.image.load("assets/opciones/sonido.png"), image_hover=pygame.image.load("assets/opciones/sonido_h.png"), pos=(700, 400), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        icono2 = Button(image=pygame.image.load("assets/opciones/mute.png"), image_hover=pygame.image.load("assets/opciones/mute_h.png"), pos=(840, 400), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        for icono in [icono1, icono2]:
            icono.changeColor(mouse_pos)
            icono.update(pantalla)

        #botones de los controles y salir al menu
        boton_back = Button(image=cargar_img("pantalla_opc/quit_opt.png"), image_hover=cargar_img("pantalla_opc/quit_opt_h.png"), pos=(800, 550), text_input=".", font=get_font(1), base_color="Black", hovering_color="Blue")
        boton_back.changeColor(mouse_pos)
        boton_back.update(pantalla)

        boton_control = Button(image=cargar_img("pantalla_opc/controles.png"), image_hover=cargar_img("pantalla_opc/controles_h.png"), pos=(500, 550), text_input=".", font=get_font(1), base_color="Black", hovering_color="Blue")
        boton_control.changeColor(mouse_pos)
        boton_control.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_back.checkForInput(mouse_pos):
                    return "menu"
                elif icono1.checkForInput(mouse_pos):
                    if not config.musica_activa:
                        reproducir_musica("assets/musica/music_menu.mp3", volumen=0.3, loop=-1)
                        config.musica_activa = True
                    else:
                        continuar_musica()
                elif bandera1.checkForInput(mouse_pos):  # Español
                    config.idioma = "español"
                elif bandera2.checkForInput(mouse_pos):  # Inglés
                    config.idioma= "ingles"
                elif icono2.checkForInput(mouse_pos):
                    config.musica_activa = False
                    pausar_musica()
                elif boton_control.checkForInput(mouse_pos):
                    mostrar_pantalla_controles(pantalla)
                

        pygame.display.update()

# Pantalla de controles
def mostrar_pantalla_controles(pantalla):
    fondo = pygame.image.load("assets/opciones/fondo_opts.png").convert()
    fondo = pygame.transform.scale(fondo, pantalla.get_size())

    # Cargar frames del fondo animado
    pantalla_ancho, pantalla_alto = pantalla.get_size()
    fondos_animados = []
    total_frames = 3
    for i in range(total_frames):
        frame = pygame.image.load(f"assets/opciones/controles/Imagen{i}.png").convert_alpha()
        # Escalar la imagen para que este mas grande
        factor = 1.5
        nuevo_ancho = int(frame.get_width() * factor)
        nuevo_alto = int(frame.get_height() * factor)
        frame_escalado = pygame.transform.scale(frame, (nuevo_ancho, nuevo_alto))

        # Centrar el frame escalado
        rect_frame = frame_escalado.get_rect(center=(pantalla_ancho // 2, pantalla_alto // 2))
        fondos_animados.append((frame_escalado, rect_frame))

    frame_actual = 0
    reloj = pygame.time.Clock()

    boton_salir = Button(image=cargar_img("pantalla_opc/quit_opt.png"), image_hover=cargar_img("pantalla_opc/quit_opt_h.png"), pos=(800, 550), text_input=".", font=get_font(1), base_color="Black", hovering_color="Blue")


    while True:
        pantalla.blit(fondo, (0, 0))
        frame, rect_frame = fondos_animados[frame_actual]
        pantalla.blit(frame, rect_frame)
        frame_actual = (frame_actual + 1) % total_frames
        mouse_pos = pygame.mouse.get_pos()

        boton_salir.changeColor(mouse_pos)
        boton_salir.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_salir.checkForInput(mouse_pos):
                    return  # ← vuelve a la pantalla de opciones

        pygame.display.update()
        reloj.tick(3)  # Controla la velocidad de animación