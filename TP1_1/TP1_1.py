from Espacio import Espacio
from Astar import Astar
import time
import random

def crear_punto(dim, final, dx, obstacles): #func para que los puntos inicial y final no se generen en obstaculos
    punto = []
    for i in range(dim):    
        punto.append(random.randrange(0, final, dx))
    if punto in obstacles: 
        return crear_punto(dim, final, dx, obstacles)
    else:
        return punto


def sort(lst):
    return lst[0]

def delete_duplicates(lst):
    return list(set(lst)) #no se puede con listas anidadas. habria que transformarlas a tuplas

def run():
    dx = 1
    dim = 3
    angle = 360
    
    t0 = time.time()
    
    espacio = Espacio(angle, dx, dim)
    espacio.create_obstacles(90, 30)
    obstacles = espacio.obstacles

    
    t1 = time.time()
    
    start = crear_punto(dim, angle, dx, obstacles)
    finish = crear_punto(dim, angle, dx, obstacles)
    print(start, finish)
    
    astar = Astar(start, finish, espacio)
    camino = astar.camino()
    
    t2 = time.time()
    print(t1-t0, t2-t1, "seconds each part")
    
        
    return obstacles, camino

if __name__ == '__main__':
    obstacles, camino = run()
    
    