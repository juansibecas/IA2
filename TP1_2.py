from Almacen import Almacen
#from Aestrella import *


if __name__ == '__main__':
    columnas = 10
    filas = 11
    almacen = Almacen(columnas,filas)
    mapa = almacen.crear_almacen()
    pasillo=almacen.crear_pasillo()
    estante=almacen.crear_estante()
