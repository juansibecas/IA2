from Space import Space
from Astar import Astar
import time
import random

def create_point(dim, final, dx, obstacles, obs_dx): #func para que los puntos inicial y final no se generen en obstaculos. igual que en delete_non_valid_neighbours
    dim_counter=0
    point = []
    for n in range(dim):    
        point.append(random.randrange(0, final, dx))
    for obstacle in obstacles:
        for l in range(dim):
            if point[l] <= obstacle[l] + obs_dx*dx and point[l] >= obstacle[l] - obs_dx*dx:
                dim_counter+=1
            if dim_counter == dim:    
                return create_point(dim, final, dx, obstacles, obs_dx)    
        dim_counter=0
    else:
        return point

def run():
    dx = 1 #discretizacion
    dim = 6
    angle = 360 
    obs_n = 30 #numero de obstaculos a generar
    obs_dx = 5 #es la mitad del ancho(por dimension) de los obstaculos
    it=10000 #numero maximo de iteraciones
       
    space = Space(angle, dx, dim)
    space.create_obstacles(obs_n, obs_dx)
    obstacles = space.obstacles
    
    t1 = time.time()
    
    start = create_point(dim, angle, dx, obstacles, obs_dx)
    finish = create_point(dim, angle, dx, obstacles, obs_dx)
    print(start,"a", finish)

    astar = Astar(start, finish, space, it)
    path = astar.path()
    
    t2 = time.time()
    print(t2-t1, "seconds")
    lst = []
    for i in range(dim):
        lst.append(abs(start[i] - finish[i]))
    
    print("distancia minima: ", max(lst))
    print("distancia recorrida: ", len(path)-1)

    return obstacles, path

if __name__ == '__main__':
    obstacles, path = run()
    
    