from Annealing import Annealing
from Warehouse import Warehouse
import random
from copy import copy
import time
import matplotlib.pyplot as plt

"""DEPRECATED (no hace falta que los puntos queden en pasillos)
def creat_prod(shelf, rows, columns): #func para que los puntos inicial y final no se generen en una estanteria
    product = [random.randint(0,rows-1), random.randint(0,columns-1)]
    if product in shelf: 
        return creat_prod(shelf, rows, columns)
    else:
        return product
"""

if __name__=='__main__':
    t1 = time.time()
    columns = 16  #para el genético trabajamos con 16, 13, 3, 6
    rows = 13
    dx = 3
    dy = 6
    warehouse = Warehouse(rows,columns, dx, dy)
    warehouse.create_aisles()
    shelves = warehouse.create_shelves()

    temp_ini = 50
    temp_fin = 0.1
    alph = 0.99
    k = 20 #tamaño de las ordenes
    m = 10 #cantidad de ordenes
    plt.xlim(temp_ini, temp_fin)
    for n in range(m):

        initial_picks = []    
       
        for i in range(k):
            initial_picks.append([random.randint(0,rows-1), random.randint(0,columns-1)]) #no hace falta que uses el create_prod.
                                                                    #cambie el astar para que admita el caso de las estanterias tambien
                                                                    
        #print("lugares a visitar:", initial_picks) 
        annealing = Annealing(temp_ini, temp_fin, alph, warehouse)
    
        order_temp, total_path_length = annealing.simulated_annealing(initial_picks)
        
        plt.plot(annealing.temperatures, annealing.costs)
        
        """
        order_temp = list(map(tuple,order_temp))
        picknumber = {(n,j): i for i, (n,j) in enumerate(initial_picks)} #con lista de tuplas funca
        result = list(map(picknumber.get, order_temp))
        
        print("longitud total a recorrer:", total_path_length)
        print("El orden adecuado de pick es: ")
        print(result)
        """
    t2 = time.time()
    print("tiempo de ejecucion:", t2-t1)
