from Warehouse import Warehouse
from Astar import Astar
import random


def create_point(shelves, rows, columns): #func para que los puntos inicial y final no se generen en una estanteria
    point = [random.randint(0,rows-1),random.randint(0,columns-1)]
    if point in shelves: 
        return create_point(shelves, rows, columns)
    else:
        return point

<<<<<<< HEAD
if __name__ == '__main__':
    columnas = 10
    filas = 11
    almacen = Almacen(filas,columnas)
    mapa = almacen.almacen
    pasillo=almacen.crear_pasillo()
    estante=almacen.crear_estante()
    print(estante)
=======

def run():
    columns = 16
    rows = 13
    dx = 3
    dy = 6
    warehouse = Warehouse(rows, columns, dx, dy)
    warehouse.create_aisles()
    shelves=warehouse.create_shelves()
    warehouse_map = warehouse.map
>>>>>>> 905defcb6912e9fc485ed3257acf80bd00d96236
    
    start = create_point(shelves, rows, columns)
    finish = create_point(shelves, rows, columns)
    
    print("La posicion inicial es :")
    print(start)
    print("La posicion final es :")
    print(finish)
    print("Camino recorrido: ")
    astar=Astar(start, finish, warehouse)
    path=astar.path(columns, rows)
    print("El camino más corto es:")
    print(path)
    return warehouse_map
    
if __name__ == '__main__':
    warehouse_map = run()