import pygame
from funciones import*
pygame.init()

# LISTAS 
lista_preguntas = crear_listas(lista,"pregunta")
lista_respuestas_a = crear_listas(lista,"a")
lista_respuestas_b = crear_listas(lista,"b")
lista_respuestas_c = crear_listas(lista,"c")
lista_respuestas_correctas = crear_listas(lista,"correcta")
lista_ubicaciones_casillas = [(140,220),(250,220),(370,220),(490,220),(610,220),(730,220),(850,220),(970,220),(1090,220),(1070,450),(950,450),(830,450),(700,450),(590,450),(470,450),(350,450),(220,450),(140,350)]
posicion_carrera_utn = [0, 0]
datos = []

# INICIALIZACIONES
index = 0
score = 0
ubicacion = 0
ingreso = ""
segundos = "5"
tiempo_juego = "120"

# CARGA DE IMAGENES
imagen_carrera_utn = pygame.image.load("imagen_utn.PNG")
imagen_estudiante = pygame.image.load("personaje.png")

# ESCALA DE IMAGENES
imagen_carrera_utn = pygame.transform.scale(imagen_carrera_utn,(265, 200))
imagen_estudiante = pygame.transform.scale(imagen_estudiante,(140, 140))

# EVENTOS DE USUARIO
tiempo = pygame.USEREVENT
# ESTABLECER TIEMPO
pygame.time.set_timer(tiempo, 1000)

# FUENTES PARA TEXTOS
fuente_botones = pygame.font.SysFont("Arial", 30)
fuente_textos = pygame.font.SysFont("Arial", 25)

# RECTANGULOS
rect_comenzar = pygame.Rect((250,740), (300, 150))
rect_terminar = pygame.Rect((650,740),(300,150))
rect_respuesta_a = pygame.Rect((270,140),(235,50))
rect_respuesta_b = pygame.Rect((547,140),(235,50))
rect_respuesta_c = pygame.Rect((847,140),(235,50))
rect_casilla_avanza = pygame.Rect((850,300),(100,100))
rect_casilla_retrocede = pygame.Rect((610,500),(100,100))
rect_ingreso = pygame.Rect((0,30),(250,30))
rect_salir = pygame.Rect((990,740),(300,150))

# BANDERAS
juego_terminado = False
mostrar_preguntas = False
mostrar_juego = True
tabla = False
fin_tiempo = False
archivo_creado = False

# PANTALLA
pantalla = pygame.display.set_mode((1300, 900))
pygame.display.set_caption("VIDEOJUEGO")