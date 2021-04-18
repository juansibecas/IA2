from Almacen import Almacen
from Aestrella import Aestrella
import random


def crear_punto(estante, filas, columnas): #func para que los puntos inicial y final no se generen en una estanteria
    punto = [random.randint(0,filas-1),random.randint(0,columnas-1)]
    if punto in estante: 
        return crear_punto(estante, filas, columnas)
    else:
        return punto

if __name__ == '__main__':
    columnas = 10
    filas = 11
    almacen = Almacen(filas,columnas)
    mapa = almacen.almacen
    pasillo=almacen.crear_pasillo()
    estante=almacen.crear_estante()
    
    inicio = crear_punto(estante, filas, columnas)
    final = crear_punto(estante, filas, columnas)
    
    inicio = [2, 3]
    final = [3, 0]
    
    print("La posicion inicial es :")
    print(inicio)
    print("La posicion final es :")
    print(final)
    print("Camino recorrido: ")
    aestrella=Aestrella(inicio,final,mapa,pasillo,estante)
    camino=aestrella.camino(columnas, filas)
    print("El camino más corto es:")
    print(camino)


