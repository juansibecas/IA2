from Warehouse import Warehouse
from Astar import Astar
import random
import time


def create_point(shelves, rows, columns): #func para que los puntos inicial y final no se generen en una estanteria
    point = [random.randint(0,rows-1),random.randint(0,columns-1)]
    if point in shelves: 
        return create_point(shelves, rows, columns) #DEPRECATED (nos conviene para ejercicios siguientes que si pueda tocar una estanteria)
    else:                                           #si toca estanteria, la cambiamos por el pasillo adyacente
        return point


def run():
    columns = 16 #para ejercicios siguientes conviene trabajar con 16, 13, 3, 6
    rows = 13
    dx = 3
    dy = 6
    warehouse = Warehouse(rows, columns, dx, dy)
    warehouse.create_aisles()
    warehouse.create_shelves()
    warehouse_map = warehouse.map
    
    start = [random.randint(0,rows-1),random.randint(0,columns-1)]
    finish = [random.randint(0,rows-1),random.randint(0,columns-1)]
    
    astar=Astar(start, finish, warehouse)
    path, path_len=astar.path(columns, rows)
    
    print("La posicion inicial es :")
    print(finish)
    print("La posicion final es :")
    print(start)
    print("Camino recorrido:") #si no sale nada es porque se obtuvo el valor desde archivo
    print("El camino más corto es:")
    print(path)
    print(path_len)
    
    warehouse.clear_map()
    warehouse.write_db_to_file()
    
    return warehouse_map
    
if __name__ == '__main__':
    t0 = time.time()
    warehouse_map = run()
    t1 = time.time()
    print("time elapsed: ", t1-t0)