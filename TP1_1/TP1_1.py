from Space import Space
from Astar import Astar
import time
import random
import matplotlib.pyplot as plt

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
        dim_counter = 0
    return point

def run():
    dx = 1 #discretizacion
    dim = 6
    angle = 180 #rango de movimiento de articulaciones
    obs_n = 20 #numero de obstaculos a generar
    obs_dx = 12 #es la mitad del ancho(por dimension) de los obstaculos(cuadrados). el ancho real(total) es (2*obs_dx+1)*dx
    it=10000 #numero maximo de iteraciones
       
    space = Space(angle, dx, dim)
    space.create_obstacles(obs_n, obs_dx)
    obstacles = space.obstacles
    
    t1 = time.time()
    
    start = create_point(dim, angle, dx, obstacles, obs_dx)
    finish = create_point(dim, angle, dx, obstacles, obs_dx)
    print(start,"a", finish)

    astar = Astar(start, finish, space, it)
    path, path_len = astar.path()
    
    t2 = time.time()
    print(t2-t1, "seconds")
    lst = []
    for i in range(dim):
        lst.append(abs(start[i] - finish[i]))
    
    print("distancia minima: ", max(lst))
    print("distancia recorrida: ", path_len)
    
    """ plot(para chequear en 2d)
    x = []
    y = []
    for i in path:
        x.append(i[0])
        y.append(i[1])
    
    xobs = []
    yobs = []
    
    for i in obstacles:
        xobs.append(i[0])
        yobs.append(i[1])
    
    plt.figure(figsize=(6,6))
    plt.scatter(start[0], start[1], color = "black")
    plt.scatter(finish[0], finish[1], color = "green")
    plt.grid()
    plt.xlim(0,angle)
    plt.ylim(0,angle)
    plt.plot(x, y)
    plt.scatter(xobs, yobs, marker = "s", color = "red") #ajustar tamaño
    """
    

    return obstacles, path

if __name__ == '__main__':
    obstacles, path = run()
    
    