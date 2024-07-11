import pygame
from datos import *
from colores import *
from biblioteca import *
from variables import *

pygame.init()

pantalla = pygame.display.set_mode((1300, 900))
pygame.display.set_caption("VIDEOJUEGO")

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
                if evento.key == pygame.K_RETURN:
                    nuevo_jugador = {"nombre":ingreso,"puntaje":score}
                    ingreso = ""
                    datos = leer_archivo("puntuaciones.json")
                    datos.append(nuevo_jugador)
                    datos_ordenados = ordenamiento(datos)
                    guardar_archivo("puntuaciones.json",datos_ordenados)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_comenzar.collidepoint(evento.pos):
                mostrar_preguntas = True
            if rect_terminar.collidepoint(evento.pos): 
                juego_terminado = True
            if rect_salir.collidepoint(evento.pos):
                mostrar_preguntas = False
                juego_terminado = False
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
            if index >= len(lista_preguntas):
                index = 0  
        if evento.type == pygame.USEREVENT:
            if evento.type == tiempo:
                if mostrar_preguntas == True:
                    if fin_tiempo == False:
                        segundos = int(segundos) - 1
                        if int(segundos) == 0:
                            segundos = 5
                            index += 1
        
    if juego_terminado == False:

        ubicacion = ubicacion_personaje(ubicacion,lista_ubicaciones_casillas)
        if ubicacion == 15:
            score = 0
        if ubicacion == 17:
            juego_terminado = True

        pantalla.fill(COLOR_CELESTE_OSCURO)

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

        texto_comenzar = fuente_botones.render("COMENZAR", True, COLOR_NEGRO)
        texto_terminar = fuente_botones.render("TERMINAR", True, COLOR_NEGRO)
        texto_tiempo = fuente_botones.render("TIEMPO:", True, COLOR_BLANCO)
        texto_segundos = fuente_botones.render(str(segundos), True, COLOR_BLANCO)
        texto_puntaje = fuente_textos.render("PUNTAJE:",True, COLOR_BLANCO)
        texto_score = fuente_textos.render(str(score), True, COLOR_BLANCO)
        texto_salida = fuente_textos.render("Salida", True, COLOR_NEGRO)
        texto_llegada = fuente_textos.render("Llegada", True, COLOR_NEGRO)
        texto_avanza_1 = fuente_textos.render("Avanza 1", True, COLOR_NEGRO)
        texto_retrocede_1 = fuente_textos.render("Retrocede 1", True, COLOR_NEGRO)

        pantalla.blit(texto_comenzar, (310, 795))
        pantalla.blit(texto_tiempo, (1110, 50))
        pantalla.blit(texto_segundos, (1235, 50))
        pantalla.blit(texto_score,(1235, 100))
        pantalla.blit(texto_puntaje,(1110,100))
        pantalla.blit(texto_avanza_1,(848,370))
        pantalla.blit(texto_retrocede_1, (590,570))
        pantalla.blit(imagen_estudiante, lista_ubicaciones_casillas[ubicacion])
        pantalla.blit(texto_salida,(120,360))
        pantalla.blit(imagen_carrera_utn, (posicion_carrera_utn))
        pantalla.blit(texto_terminar, (710,795))

        if mostrar_preguntas:
            texto_preguntas = fuente_textos.render(lista_preguntas[index], True, COLOR_AMARILLO)
            texto_respuestas_a = fuente_textos.render(lista_respuestas_a[index], True, COLOR_AMARILLO)
            texto_respuestas_b = fuente_textos.render(lista_respuestas_b[index], True, COLOR_AMARILLO)
            texto_respuestas_c = fuente_textos.render(lista_respuestas_c[index], True, COLOR_AMARILLO)
            pantalla.blit(texto_preguntas, (370, 50))
            pantalla.blit(texto_respuestas_a, (270, 150))
            pantalla.blit(texto_respuestas_b, (550, 150))
            pantalla.blit(texto_respuestas_c, (850, 150))

        pygame.display.flip()

    if juego_terminado:

        pantalla.fill(COLOR_CELESTE_OSCURO)

        pygame.draw.rect(pantalla, COLOR_BLANCO, rect_ingreso)
        pygame.draw.rect(pantalla, COLOR_CELESTE_CLARO, rect_salir)

        texto_introducir_nombre = fuente_textos.render("INGRESE SU NOMBRE:", True, COLOR_BLANCO)
        texto_nombre = fuente_textos.render(ingreso, True, COLOR_NEGRO)
        texto_salir = fuente_textos.render("SALIR", True, COLOR_NEGRO)

        jugadores = leer_archivo("puntuaciones.json")
        lista_ordenada = ordenamiento(jugadores)
        for i in range(len(lista_ordenada)):
            if i <= 10:
                texto_jugador = fuente_textos.render(f"Nombre: {lista_ordenada[i]['nombre']}, Puntaje: {lista_ordenada[i]['puntaje']}", True, COLOR_BLANCO)
                pantalla.blit(texto_jugador, (500, 0 + i * 30)) 

        pantalla.blit(texto_introducir_nombre, (0,0))
        pantalla.blit(texto_salir, (1100,795))
        pantalla.blit(texto_nombre, rect_ingreso)
        pantalla.blit(imagen_estudiante, (0,100))

        pygame.display.flip()


pygame.quit()
