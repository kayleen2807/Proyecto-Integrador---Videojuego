# 🌿 Prueba de Juego en Pygame - **Nivel 1 Completado**

## 🎮 Descripción
Esta es una prueba funcional de un juego de plataformas en 2D desarrollado con Pygame, con el Nivel 1 ya completado. El objetivo es validar que el nivel 1 funcione corectamente con, la cámara dinámica, el zoom visual y las colisiones con el entorno. El mapa fue creado en Tiled y se carga desde un archivo `.tmx`. Despues se agregara los demas niveles  

## 🧪 ¿Qué incluye esta prueba?
- Movimiento horizontal con colisiones
- Salto con gravedad
- Cámara que sigue al personaje
- Zoom aplicado a mapa y personaje
- Botón para regresar al menú
- Menú principal con navegación básica
- Diseños en pixel art muy visuales
- Cambio de pantallas correctamente
- Pantallas de victoria y de game over (dependiendo si se gana o se pierda)
- Recoleccion de objetos
- Reproduccion de musica
- Pequeñas animaciones

## 🕹️ Controles
- **← / →** y **a / d**: Mover al personaje
- **Espacio** y **w**: Saltar
- **Mouse**: Navegar por los botones
- **ESC / Cerrar ventana**: Salir del juego

## 🧱 Estructura del proyecto

| Archivo | Descripción |
|--------|-------------|
| `animacion_gameover.py` | Funcion para reproducir de una animacion, de acuerdo al personaje, cuando el jugador pierde y la carga de los frames para la animacion |
| `basura` | Carga de los sprites (imagenes) de los objetos **basura** y contador de este mismo, que incluye en nuestro juego, y funcion que los muestra en pantalla |
| `button.py` | Clase para crear botones interactivos con sprites (imagenes) |
| `config.py` | Configuración de pantalla y fuente |
| `game_over.py` | Pantalla de game over cuando el jugador pierde y reproduccion de la animacion de muerte|
| `juego.py` | Lógica del juego (`play()`), mapa, personaje, cámara del **Nivel 1**|
| `main.py` | Bucle principal que gestiona las pantallas |
| `objetos.py` | Carga de sprites (imagenes) de la basura, funciones para la recoleccion de objetos (basura), mostrar en pantalla y pantalla de victoria (con verificacion)  |
| `pantalla_seleccion.py` | Pantallas de inicio, menú y opciones |
| `pause_menu.py` | Pantalla de menu de pausa con acciones **resume** **restart** **quit** |
| `selection_player.py` | Carga de los sprites de los personajes (imagenes), clase **personaje** en donde estan las funciones para mostrar, dependiendo el personaje, en el juego, respetando colisones, camara, velocidad, salto ,etc |
| `selection_screen.py` | Pantalla de seleccion del perosnaje **Masculino** o **Femenino** y animaciones entre el mapa |
| `vidas.py` | Carga de los sprites (imagenes), del contador de vidas y mostrarlos en pantalla|
| `assets/` | Carpeta con imágenes, fuente, fondos, botones, sprites de los personajes (imagenes), sprites de los objetos (basura), mapa, musica. **Todo esto con sus respectivas carpetas ordenadas e indetificables** |

## 🧰 Requisitos

- Python 3.10+
- Pygame
- pytmx

Instalación rápida:

```bash
pip install pygame pytmx
