from datos import*
import json

def crear_listas(lista:list,key:str):
    lista_nueva = []
    for elemento in lista:
        lista_nueva.append(elemento[key])
    return lista_nueva

def generar_archivo(nombre_archivo:str,lista:list):
    '''Recibe como parametro la ubicacion del archivo una key y una lista
       abre el archivo en modo de w+ primero escribe el titulo que sera la key
       y recorre la lista para escribir las value de la key en el nuevo archivo generado'''
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(lista, archivo, indent=4)
            
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
        return False