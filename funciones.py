from datos import*
import json
import pygame
from colores import*

def crear_listas(lista:list,key:str):
    lista_nueva = []
    for elemento in lista:
        lista_nueva.append(elemento[key])
    return lista_nueva

def guardar_archivo(nombre_archivo:str,lista:list):
    '''Recibe como parametro la ubicacion del archivo una key y una lista
       abre el archivo en modo de w+ primero escribe el titulo que sera la key
       y recorre la lista para escribir las value de la key en el nuevo archivo generado'''
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(lista, archivo, indent=4)
            
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
        return False

def leer_archivo(nombre_archivo:str):
        '''Lee el archivo que recibe como parametro en modo solo lectura y retorna los datos que haya dentro de ese archivo'''
        with open(nombre_archivo, 'r') as archivo:
            datos_existente = json.load(archivo)
            return datos_existente

def ordenamiento(lista:list):
    '''Recibe como parametros, una lista y una cadena
       con el metodo sorted y un lambda que me devuelve el contenido de una key
       retorna esta misma como una lista ordenada'''
    lista_ordenada = sorted(lista, key=lambda elemento: elemento["puntaje"], reverse = True)
    return lista_ordenada

def botones_respuesta(rectangulo_a,rectangulo_b,rectangulo_c,evento:str,lista:list,indice:int):
    '''Recibe varios Rect , un evento, una lista y un indice
       La funcion inicializa una variable booleana que cambiara en true o false dependiendo si responde bien o mal
       y luego lo retorna'''
    estado = bool
    if rectangulo_a.collidepoint(evento.pos):
        if lista[indice] == "a":
            estado = True
        elif lista[indice] != "a":
            estado = False
    if rectangulo_b.collidepoint(evento.pos):
        if lista[indice] == "b":
            estado = True
        elif lista[indice] != "b":
            estado = False
    if rectangulo_c.collidepoint(evento.pos):
        if lista[indice] == "c":
            estado = True
        elif lista[indice] != "c":
            estado = False
    return estado

def ubicacion_personaje(ubicacion:int,lista:list):
    '''Recibe como paramtro una ubicacion y una lista
       la funcion controla el valor de ubicacion dependiendo que numero sea para luego retornarla'''
    if ubicacion < 0:
        ubicacion = 0
    elif ubicacion == 6:
        ubicacion += 1
    elif ubicacion == 13:
        ubicacion -= 1
    elif ubicacion >= len(lista):
        ubicacion = 17
    return ubicacion

def presiono_espacio(evento:str,score:int,ingreso:str):
    '''Recibe como paremtro un evento, score e ingreso
       La funcion se encarga de crear un dicc con las key nombre y puntaje, ese dicc lo agrega al archivo json ya ordenado'''
    if evento.key == pygame.K_SPACE:
        ingreso = ingreso.strip()
        nuevo_jugador = {"nombre":ingreso,"puntaje":score}
        datos = leer_archivo("puntuaciones.json")
        datos.append(nuevo_jugador)
        datos_ordenados = ordenamiento(datos)
        guardar_archivo("puntuaciones.json",datos_ordenados)
    
def dibujar_juego(juego_terminado:bool,pantalla,rect_comenzar,rect_terminar,rect_respuesta_a,rect_respuesta_b,rect_respuesta_c,rect_ingreso,rect_salir):
    '''Recibe un booleano y varios Rects
       Se encarga de dibujar los Rects en la pantalla'''
    if juego_terminado == False:
        pygame.draw.rect(pantalla, COLOR_CELESTE_CLARO, rect_comenzar)
        pygame.draw.rect(pantalla, COLOR_CELESTE_CLARO, rect_terminar)
        pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, rect_respuesta_a)
        pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, rect_respuesta_b)
        pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, rect_respuesta_c)
        pygame.draw.rect(pantalla, COLOR_VERDE_OSCURO, (270, 10, 830, 190))
        pygame.draw.rect(pantalla, COLOR_NARANJA, (250,300,100,300))
        pygame.draw.rect(pantalla, COLOR_VERDE_CLARO, (370,300,100,300))
        pygame.draw.rect(pantalla, COLOR_AMARILLO, (490,300,100,300))
        pygame.draw.rect(pantalla, COLOR_CELESTE, (610,300,100,300))
        pygame.draw.rect(pantalla, COLOR_ROJO, (730,300,100,300))
        pygame.draw.rect(pantalla, COLOR_VIOLETA, (850,300,100,300))
        pygame.draw.rect(pantalla, COLOR_MARRON, (970,300,100,300))
        pygame.draw.rect(pantalla, COLOR_ROSA,(1090,300,100,300))
        pygame.draw.rect(pantalla, COLOR_CELESTE_OSCURO, (250,400,1000,100))
    elif juego_terminado == True:
        pygame.draw.rect(pantalla, COLOR_BLANCO, rect_ingreso)
        pygame.draw.rect(pantalla, COLOR_CELESTE_CLARO, rect_salir)

def escribir_juego(juego_terminado:bool,fuente_botones,fuente_textos,segundos:int,tiempo_juego:int,score:int,pantalla,imagen_estudiante,lista_ubicaciones_casillas:list,ubicacion:int,imagen_carrera_utn,posicion_carrera_utn,ingreso:str,rect_ingreso):
    '''Recibe un booleano un rect una fuente y variables
       Se encarga de escribir los textos en la pantalla'''
    if juego_terminado == False:
        texto_comenzar = fuente_botones.render("COMENZAR", True, COLOR_NEGRO)
        texto_terminar = fuente_botones.render("TERMINAR", True, COLOR_NEGRO)
        texto_tiempo = fuente_botones.render("TIEMPO:", True, COLOR_BLANCO)
        texto_fin_juego = fuente_botones.render("FIN DEL JUEGO:",True,COLOR_BLANCO)
        texto_segundos = fuente_botones.render(str(segundos), True, COLOR_BLANCO)
        texto_tiempo_juego = fuente_botones.render(str(tiempo_juego),True,COLOR_BLANCO)
        texto_puntaje = fuente_textos.render("PUNTAJE:",True, COLOR_BLANCO)
        texto_score = fuente_textos.render(str(score), True, COLOR_BLANCO)
        texto_salida = fuente_textos.render("Salida", True, COLOR_NEGRO)
        texto_llegada = fuente_textos.render("Llegada", True, COLOR_NEGRO)
        texto_avanza_1 = fuente_textos.render("Avanza 1", True, COLOR_NEGRO)
        texto_retrocede_1 = fuente_textos.render("Retrocede 1", True, COLOR_NEGRO)
        pantalla.blit(texto_comenzar, (310, 795))
        pantalla.blit(texto_tiempo, (1110, 50))
        pantalla.blit(texto_fin_juego,(0,700))
        pantalla.blit(texto_segundos, (1235, 50))
        pantalla.blit(texto_tiempo_juego,(0,750))
        pantalla.blit(texto_score,(1235, 100))
        pantalla.blit(texto_puntaje,(1110,100))
        pantalla.blit(texto_avanza_1,(848,370))
        pantalla.blit(texto_retrocede_1, (590,570))
        pantalla.blit(texto_llegada,(120,560))
        pantalla.blit(imagen_estudiante, lista_ubicaciones_casillas[ubicacion])
        pantalla.blit(texto_salida,(120,360))
        pantalla.blit(imagen_carrera_utn, (posicion_carrera_utn))
        pantalla.blit(texto_terminar, (710,795))
    elif juego_terminado == True:
        texto_tabla_puntaje = fuente_botones.render("PUNTAJES:", True, COLOR_BLANCO)
        texto_introducir_nombre = fuente_textos.render("INGRESE SU NOMBRE:", True, COLOR_BLANCO)
        texto_nombre = fuente_textos.render(ingreso, True, COLOR_NEGRO)
        texto_salir = fuente_textos.render("SALIR", True, COLOR_NEGRO)
        pantalla.blit(texto_introducir_nombre, (0,0))
        pantalla.blit(texto_tabla_puntaje, (500,0))
        pantalla.blit(texto_salir, (1100,795))
        pantalla.blit(texto_nombre, rect_ingreso)
        pantalla.blit(imagen_estudiante, (0,100))

def recorrer_lista(lista_ordenada:list,fuente_textos,pantalla):
    '''Recibe como parametros una lista un fuente y la pantalla de pygame
       Recorre la lista con una condicion si se cumple escribe en la pantalla los valores de la lista'''
    for i in range(len(lista_ordenada)):
        if i <= 10:
            texto_jugador = fuente_textos.render(f"Nombre: {lista_ordenada[i]['nombre']}, Puntaje: {lista_ordenada[i]['puntaje']}", True, COLOR_BLANCO)
            pantalla.blit(texto_jugador, (500, 55 + i * 30)) 

def escribir_preguntas(mostrar_preguntas:bool,fuente_textos,lista_preguntas:list,lista_respuestas_a:list,lista_respuestas_b:list,lista_respuestas_c:list,index:int,pantalla):
    '''Recibe como parametros un booleeano una fuente un indice y varias listas
       Se encarga de escribir las preguntas que esten en la posicion de las listas en la pantalla'''
    if mostrar_preguntas == True:
        texto_preguntas = fuente_textos.render(lista_preguntas[index], True, COLOR_AMARILLO)
        texto_respuestas_a = fuente_textos.render(lista_respuestas_a[index], True, COLOR_AMARILLO)
        texto_respuestas_b = fuente_textos.render(lista_respuestas_b[index], True, COLOR_AMARILLO)
        texto_respuestas_c = fuente_textos.render(lista_respuestas_c[index], True, COLOR_AMARILLO)
        pantalla.blit(texto_preguntas, (370, 50))
        pantalla.blit(texto_respuestas_a, (270, 150))
        pantalla.blit(texto_respuestas_b, (550, 150))
        pantalla.blit(texto_respuestas_c, (850, 150))
