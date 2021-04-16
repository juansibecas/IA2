from Almacen import Almacen
from Aestrella import Aestrella
import random

if __name__ == '__main__':
    columnas = 10
    filas = 11
    almacen = Almacen(filas,columnas)
    mapa = almacen.almacen
    pasillo=almacen.crear_pasillo()
    estante=almacen.crear_estante()
    inicio=[random.randint(0,filas-1),random.randint(0,columnas-1)]
    final=[random.randint(0,filas-1),random.randint(0,columnas-1)]
    print("La posicion inicial es :")
    print(inicio)
    print("La posicion final es :")
    print(final)
    print("Camino recorrido: ")
    aestrella=Aestrella(inicio,final,mapa,pasillo,estante)
    camino=aestrella.camino(columnas, filas)
    print("El menor más corto es:")
    print(camino)


