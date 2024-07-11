import pygame
from colores import *
from datos import *
from funciones import *
from variables import *

while mostrar_juego:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            mostrar_juego = False
        if evento.type == pygame.KEYDOWN:
            if juego_terminado == True:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                else:
                    ingreso += evento.unicode
                presiono_espacio(evento,score,ingreso)
                if evento.key == pygame.K_SPACE:
                    ingreso = ""
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_comenzar.collidepoint(evento.pos):
                mostrar_preguntas = True
                ingreso = ""
            if rect_terminar.collidepoint(evento.pos): 
                juego_terminado = True
            if rect_salir.collidepoint(evento.pos):
                mostrar_preguntas = False
                juego_terminado = False
                tiempo_juego = 120
                segundos = 5
                ubicacion = 0
                index = 0
                score = 0
            respuesta = botones_respuesta(rect_respuesta_a,rect_respuesta_b,rect_respuesta_c,evento,lista_respuestas_correctas,index)
            if respuesta == True:
                index += 1
                segundos = 5
                score += 10
                ubicacion += 2
            elif respuesta == False:
                index += 1
                segundos = 5
                ubicacion -= 1
        if evento.type == pygame.USEREVENT:
            if evento.type == tiempo:
                if mostrar_preguntas == True:
                    if fin_tiempo == False:
                        tiempo_juego = int(tiempo_juego) - 1
                        if int(tiempo_juego) == 0:
                            juego_terminado = True
                        segundos = int(segundos) - 1
                        if int(segundos) == 0:
                            segundos = 5
                            index += 1
                            
    if index >= len(lista_preguntas):
        index = 0  

    if juego_terminado == False:
        pantalla.fill(COLOR_CELESTE_OSCURO)
        dibujar_juego(juego_terminado,pantalla,rect_comenzar,rect_terminar,rect_respuesta_a,rect_respuesta_b,rect_respuesta_c,rect_ingreso,rect_salir)
        if ubicacion == 15:
            ubicacion = 0
            score = 0
        ubicacion = ubicacion_personaje(ubicacion,lista_ubicaciones_casillas)
        if ubicacion == 17:
            juego_terminado = True
        escribir_juego(juego_terminado,fuente_botones,fuente_textos,segundos,tiempo_juego,score,pantalla,imagen_estudiante,lista_ubicaciones_casillas,ubicacion,imagen_carrera_utn,posicion_carrera_utn,ingreso,rect_ingreso)
        if mostrar_preguntas:
            escribir_preguntas(mostrar_preguntas,fuente_textos,lista_preguntas,lista_respuestas_a,lista_respuestas_b,lista_respuestas_c,index,pantalla)
        pygame.display.flip()

    if juego_terminado:
        pantalla.fill(COLOR_CELESTE_OSCURO)
        dibujar_juego(juego_terminado,pantalla,rect_comenzar,rect_terminar,rect_respuesta_a,rect_respuesta_b,rect_respuesta_c,rect_ingreso,rect_salir)
        escribir_juego(juego_terminado,fuente_botones,fuente_textos,segundos,tiempo_juego,score,pantalla,imagen_estudiante,lista_ubicaciones_casillas,ubicacion,imagen_carrera_utn,posicion_carrera_utn,ingreso,rect_ingreso)
        jugadores = leer_archivo("puntuaciones.json")
        lista_ordenada = ordenamiento(jugadores)
        recorrer_lista(lista_ordenada,fuente_textos,pantalla)
        pygame.display.flip()

pygame.quit()
