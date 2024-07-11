from datos import*
import json
import pygame

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
        with open('puntuaciones.json', 'r') as archivo:
            datos_existente = json.load(archivo)
            return datos_existente

def ordenamiento(lista:list):
    '''Recibe como parametros, una lista y una cadena
       con el metodo sorted y un lambda que me devuelve el contenido de una key
       retorna esta misma como una lista ordenada'''
    lista_ordenada = sorted(lista, key=lambda elemento: elemento["puntaje"], reverse = True)
    return lista_ordenada

def botones_respuesta(rectangulo_a,rectangulo_b,rectangulo_c,evento,lista,indice):

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

def ubicacion_personaje(ubicacion,lista:list):

    if ubicacion < 0:
        ubicacion = 0
    elif ubicacion == 6:
        ubicacion += 1
    elif ubicacion == 13:
        ubicacion -= 1
    elif ubicacion >= len(lista):
        ubicacion = 17
    return ubicacion

