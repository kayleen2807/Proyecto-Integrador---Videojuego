from config import pantalla, get_font
from button import Button
from musica import reproducir_musica, detener_musica
import pygame
# Pantalla de inicio
def inicio():
    pygame.display.set_caption("Inicio")
    while True:
        #fondo
        mouse_pos = pygame.mouse.get_pos()
        pantalla.fill("black")

        #texto de bienvenida
        texto = get_font(80).render("Bienvenido", True, "White")
        texto_rect = texto.get_rect(center=(640, 200))
        pantalla.blit(texto, texto_rect)

        #boton de empezar que lleva al menu principal
        boton_empezar = Button(image=None, image_hover=None, pos=(640, 400), text_input="EMPEZAR", font=get_font(45), base_color="White", hovering_color="Blue")
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

    reproducir_musica ("assets/musica/music_menu.mp3", volumen=0.6)
    title = pygame.image.load("assets/gatods.png")

    #botones play, opciones y salir
    boton_play = Button(image=pygame.image.load("assets/español/boton_menu/boton_jugar.png"), image_hover=pygame.image.load("assets/español/boton_menu/boton_jugar_h.png"), pos=(650, 280), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_opciones = Button(image=pygame.image.load("assets/español/boton_menu/boton_opciones.png"), image_hover=pygame.image.load("assets/español/boton_menu/boton_opciones_h.png"), pos=(650, 420), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
    boton_salir = Button(image=pygame.image.load("assets/español/boton_menu/boton_Salir.png"), image_hover=pygame.image.load("assets/español/boton_menu/boton_Salir_h.png"), pos=(652, 558), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")

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
                    detener_musica()
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
    pygame.display.set_caption("Opciones")
    while True:
        fondo_mapa_preview = pygame.image.load("assets/opciones/fondo_opts.png").convert()
        fondo_mapa_preview = pygame.transform.scale(fondo_mapa_preview, pantalla.get_size())
        pantalla.blit(fondo_mapa_preview, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        opc = pygame.image.load("assets/opciones/opts.png")
        pantalla.blit(opc, (550, 190))

        lengua = pygame.image.load("assets/opciones/Lenguage.png")
        pantalla.blit(lengua, (490, 300))
        bandera1 = Button(image=pygame.image.load("assets/opciones/bandera_e.png"), image_hover=None, pos=(660, 300), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        bandera2 = Button(image=pygame.image.load("assets/opciones/bandera_i.png"), image_hover=None, pos=(760, 300), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        for bandera in [bandera1, bandera2]:
            bandera.changeColor(mouse_pos)
            bandera.update(pantalla)

        music = pygame.image.load("assets/opciones/Music.png")
        pantalla.blit(music, (490, 400))
        icono1 = Button(image=pygame.image.load("assets/opciones/sonido.png"), image_hover=None, pos=(660, 400), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        icono2 = Button(image=pygame.image.load("assets/opciones/mute.png"), image_hover=None, pos=(760, 400), text_input=".", font=get_font(1), base_color="#d7fcd4", hovering_color="White")
        for icono in [icono1, icono2]:
            icono.changeColor(mouse_pos)
            icono.update(pantalla)


        boton_back = Button(image=pygame.image.load("assets/opciones/quit_opt.png"), image_hover=None, pos=(660, 560), text_input="BACK", font=get_font(1), base_color="Black", hovering_color="Blue")
        boton_back.changeColor(mouse_pos)
        boton_back.update(pantalla)

        boton_control = Button(image=pygame.image.load("assets/opciones/controles.png"), image_hover=None, pos=(660, 480), text_input=".", font=get_font(1), base_color="Black", hovering_color="Blue")
        boton_control.changeColor(mouse_pos)
        boton_control.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_back.checkForInput(mouse_pos):
                    return "menu"

        pygame.display.update()
