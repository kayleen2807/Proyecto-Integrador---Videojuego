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

        self.sprites = {
            "base": {
                "derecha": escalar(pygame.image.load(f"player/Base_{nombre}.png").convert_alpha(), factor),
                "izquierda": escalar(pygame.image.load(f"player/Base_{nombre}(1).png").convert_alpha(), factor)
            },
            "caminar": {
                "derecha":escalar(pygame.image.load(f"player/Correr_{nombre}.png").convert_alpha(), factor),
                "izquierda": escalar(pygame.image.load(f"player/Correr_{nombre}(1).png").convert_alpha(), factor)
            },
            "saltar": {
                "derecha": escalar(pygame.image.load(f"player/Saltar_{nombre}.png").convert_alpha(), factor),
                "izquierda": escalar(pygame.image.load(f"player/Saltar_{nombre}(1).png").convert_alpha(), factor)
            }
        }

    def actualizar_estado(self, keys, en_el_suelo, vel_y):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direccion = "izquierda"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direccion = "derecha"

        caminando = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_d]
        saltando = not en_el_suelo and vel_y < 0

        if saltando:
            self.estado = "saltar"
        elif caminando:
            self.estado = "caminar"
        else:
            self.estado = "base"

    def dibujar(self, pantalla, camara_x, camara_y, zoom):
        sprite = self.sprites[self.estado][self.direccion]
        sprite_escalado = pygame.transform.scale(sprite, (
            int(sprite.get_width() * zoom),
            int(sprite.get_height() * zoom)
        ))
        pantalla.blit(sprite_escalado, (
            int((self.rect.x - camara_x) * zoom),
            int((self.rect.y - camara_y) * zoom)
        ))

