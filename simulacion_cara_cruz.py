import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 155, 0)

# Cargar imágenes
imagen_mano = pygame.image.load('mano.png')
imagen_mano2 = pygame.image.load('mano2.png')  # Nueva imagen para animación
imagen_cara = pygame.image.load('cara.png')
imagen_cruz = pygame.image.load('cruz.png')

# Escalar imágenes
imagen_mano = pygame.transform.scale(imagen_mano, (200, 200))
imagen_mano2 = pygame.transform.scale(imagen_mano2, (200, 200))
imagen_cara = pygame.transform.scale(imagen_cara, (150, 150))
imagen_cruz = pygame.transform.scale(imagen_cruz, (150, 150))

# Configurar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Simulación de Lanzamiento de Moneda')

# Fuente para texto
fuente = pygame.font.Font(None, 36)

def dibujar_boton(texto, rect, color_base, color_hover, accion=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if rect.collidepoint(mouse):
        pygame.draw.rect(pantalla, color_hover, rect)
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color_base, rect)
    texto_superficie = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_superficie, texto_superficie.get_rect(center=rect.center))

resultado = None

def lanzar_moneda():
    global resultado
    pantalla.fill(BLANCO)
    texto_resultado = fuente.render('Resultado:', True, AMARILLO)
    pantalla.blit(texto_resultado, (20, 20))
    pantalla.blit(imagen_mano2, (ANCHO // 2 - 100, ALTO // 2))  # Aparece mano2.png
    boton_rect = pygame.Rect((ANCHO // 2 - 100, ALTO - 150, 200, 50))
    dibujar_boton('Lanzar Moneda', boton_rect, (0, 255, 0), (0, 200, 0))
    pygame.display.flip()
    time.sleep(0.5)  # Mostrar mano2.png por 0.5 segundos
    resultado = random.choice(['cara', 'cruz'])

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(BLANCO)
    texto_resultado = fuente.render('Resultado:', True, AMARILLO)
    pantalla.blit(texto_resultado, (20, 20))

    if resultado:
        pantalla.blit(fuente.render(resultado.capitalize(), True, NEGRO), (170, 20))

    if not resultado:
        pantalla.blit(imagen_mano, (ANCHO // 2 - 100, ALTO // 2))
    else:
        pantalla.blit(imagen_mano, (ANCHO // 2 - 100, ALTO // 2))
        if resultado == 'cara':
            pantalla.blit(imagen_cara, (ANCHO // 2 - 75, ALTO // 2 - 160))
        elif resultado == 'cruz':
            pantalla.blit(imagen_cruz, (ANCHO // 2 - 75, ALTO // 2 - 160))

    boton_rect = pygame.Rect((ANCHO // 2 - 100, ALTO - 150, 200, 50))
    dibujar_boton('Lanzar Moneda', boton_rect, (0, 255, 0), (0, 200, 0), lanzar_moneda)
    pygame.display.flip()

pygame.quit()
