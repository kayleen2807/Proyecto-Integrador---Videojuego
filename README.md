# 🌿 Prueba de Juego en Pygame

## 🎮 Descripción
Esta es una prueba funcional de un juego de plataformas en 2D desarrollado con Pygame. El objetivo es validar el movimiento del personaje, la cámara dinámica, el zoom visual y las colisiones con el entorno. El mapa fue creado en Tiled y se carga desde un archivo `.tmx`.

## 🧪 ¿Qué incluye esta prueba?
- Movimiento horizontal con colisiones
- Salto con gravedad
- Cámara que sigue al personaje
- Zoom aplicado a mapa y personaje
- Botón para regresar al menú
- Menú principal con navegación básica

## 🕹️ Controles
- **← / →**: Mover al personaje
- **Espacio**: Saltar
- **Mouse**: Navegar por los botones
- **ESC / Cerrar ventana**: Salir del juego

## 🧱 Estructura del proyecto

| Archivo | Descripción |
|--------|-------------|
| `main.py` | Bucle principal que gestiona las pantallas |
| `game.py` | Lógica del juego (`play()`), mapa, personaje, cámara |
| `screens.py` | Pantallas de inicio, menú y opciones |
| `config.py` | Configuración de pantalla y fuente |
| `button.py` | Clase para crear botones interactivos |
| `mapa_prueba.tmx` | Mapa creado en Tiled con objetos de colisión |
| `assets/` | Carpeta con imágenes, fuente y fondo |

## 🧰 Requisitos

- Python 3.10+
- Pygame
- pytmx

Instalación rápida:

```bash
pip install pygame pytmx
