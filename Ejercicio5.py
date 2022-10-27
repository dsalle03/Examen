import hashlib

def tabla_1(tamanio):
    tabla = [None] * tamanio
    return tabla

def numero_elementos(tabla):
    return len(tabla) - tabla.count(None)

def hash(dato, tamanio_tabla):
    return len(str(dato).strip())% tamanio_tabla

def anadir(tabla, dato):
    posicion = hash(dato, len(tabla))
    if (tabla[posicion] is None):
        tabla[posicion] = lista()
    insertar(tabla[posicion],dato)
