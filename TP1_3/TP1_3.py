from Annealing import Annealing
from Warehouse import Warehouse
import random

def creat_prod(shelf, rows, columns): #func para que los puntos inicial y final no se generen en una estanteria
    product = [random.randint(0,rows-1), random.randint(0,columns-1)]
    if product in shelf: 
        return creat_prod(shelf, rows, columns)
    else:
        return product

if __name__=='__main__':
    columns = 16  #para el genético trabajamos con 16, 13, 3, 6
    rows = 13
    dx = 3
    dy = 6
    warehouse = Warehouse(rows,columns, dx, dy)
    warehouse.create_aisles()
    shelves = warehouse.create_shelves()

    k = 5 #cantidad de productos en la lista de pick
    initial_picks = []    
   
    for i in range(k):
        initial_picks.append(creat_prod(shelves,rows,columns))  #no hace falta que uses el create_prod.
                                                                #cambie el astar para que admita el caso de las estanterias tambien
    
    temp_ini = 100
    temp_fin = .1
    alph = 0.1
    annealing = Annealing(temp_ini, temp_fin, alph, initial_picks, rows, columns, dx, dy)
    order_temp = annealing.simulated_annealing(initial_picks)
    order = []
    init = []
        
    picknumber = {n: i for i, n in enumerate([tuple(n) for n in initial_picks])} #con lista de tuplas funca
    result = list(map(picknumber.get, order))
    print("El orden adecuado de pick es: ")
    print(result)