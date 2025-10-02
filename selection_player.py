import pygame

def escalar(sprite, factor):
        ancho = int(sprite.get_width() * factor)
        alto = int(sprite.get_height() * factor)
        return pygame.transform.scale(sprite, (ancho, alto))

class Personaje:
    
    def __init__(self, nombre, x, y):
        factor = 1.5  # Ajusta según lo que se vea bien
        self.nombre = nombre  # "Masculino" o "Femenino"
        self.rect = pygame.Rect(x, y, 32, 32)
        self.estado = "base"
        self.direccion = "derecha"
        self.frame_actual = 0
        self.contador_animacion = 0
        #carga sprites del personaje
        self.sprites = {
            "base": {
                "derecha": [escalar(pygame.image.load(f"player/Base_{nombre}.png").convert_alpha(), factor)],
                "izquierda": [escalar(pygame.image.load(f"player/Base_{nombre}(1).png").convert_alpha(), factor)]
            },
            "caminar": {
                "derecha":[
                     escalar(pygame.image.load(f"player/Correr_{nombre}.png").convert_alpha(), factor),
                     escalar(pygame.image.load(f"player/Correr_{nombre}_1.png").convert_alpha(), factor)
                ],
                "izquierda":[ escalar(pygame.image.load(f"player/Correr_{nombre}(1).png").convert_alpha(), factor),
                             escalar(pygame.image.load(f"player/Correr_{nombre}(1)_1.png").convert_alpha(), factor)
                ]
            },
            "saltar": {
                "derecha": [escalar(pygame.image.load(f"player/Saltar_{nombre}.png").convert_alpha(), factor)],
                "izquierda": [escalar(pygame.image.load(f"player/Saltar_{nombre}(1).png").convert_alpha(), factor)]
            }
        }
        #animacion para que camine en el juego
        self.animacion_caminar = {
            "derecha": self.sprites["base"]["derecha"] + self.sprites["caminar"]["derecha"],
            "izquierda": self.sprites["base"]["izquierda"] + self.sprites["caminar"]["izquierda"]
        }
    #mostrar el sprite correcto al momento de caminar a la derecha o izquierda
    def actualizar_estado(self, keys, en_el_suelo, vel_y):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direccion = "izquierda"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direccion = "derecha"

        #variables para mostrar el sprite correcto al mover al personaje o al saltar
        caminando = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_d]
        saltando = not en_el_suelo and vel_y < 0

        #codicion para mostrar si el personaje salta y camina dependiendo la direccion
        if saltando:
            self.estado = "saltar"
        elif caminando:
            self.estado = "caminar"
        else:
            self.estado = "base"
    
    #aplicar la camara al sprite del personaje
    def dibujar(self, pantalla, camara_x, camara_y, zoom):
        # Selección de frames según estado
        if self.estado == "caminar":
            frames = self.animacion_caminar[self.direccion]
        else:
            frames = self.sprites[self.estado][self.direccion]
        # Protección: si no hay frames, salimos
        if not frames:
            return

        # Animación: avanzar frame cada cierto tiempo
        self.contador_animacion += 1
        if self.contador_animacion >= 10:  # Ajusta la velocidad aquí
            self.frame_actual = (self.frame_actual + 1) % len(frames)
            self.contador_animacion = 0

        # Protección: asegurar que el índice esté dentro del rango
        self.frame_actual = self.frame_actual % len(frames)
        sprite = frames[self.frame_actual]

        # Escalado y dibujo en pantalla
        sprite_escalado = pygame.transform.scale(sprite, (
            int(sprite.get_width() * zoom),
            int(sprite.get_height() * zoom)
        ))
        pantalla.blit(sprite_escalado, (
         int((self.rect.x - camara_x) * zoom),
         int((self.rect.y - camara_y) * zoom)
        ))

