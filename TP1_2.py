from Almacen import Almacen
from Aestrella import Aestrella


if __name__ == '__main__':
    columnas = 10
    filas = 11
    almacen = Almacen(columnas,filas)
    mapa = almacen.almacen
    pasillo=almacen.crear_pasillo()
    estante=almacen.crear_estante()
    aestrella=Aestrella([0,0],[7,7],mapa,pasillo,estante)
    aestrella.camino(columnas, filas)
