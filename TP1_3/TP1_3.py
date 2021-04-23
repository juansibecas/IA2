from Annealing import Annealing
from Almacen import Almacen
import random

def creat_prod(shelf, rows, columns): #func para que los puntos inicial y final no se generen en una estanteria
    product = [random.randint(0,rows-1),random.randint(0,columns-1)]
    if product in shelf: 
        return creat_prod(shelf, rows, columns)
    else:
        return product

if __name__=='__main__':
    columns = 10
    rows = 10
    warehouse = Almacen(rows,columns)
    shelf = warehouse.crear_estante()
    k = 5 #cantidad de productos en la lista de pick
    initial_picks = []    
   
    for i in range(k):
        initial_picks.append(creat_prod(shelf,rows,columns))
    temp_ini = 100
    temp_fin = .1
    alph = 0.01
    annealing = Annealing(temp_ini,temp_fin,alph,initial_picks,rows,columns)
    order = annealing.simulated_annealing(initial_picks)
    picknumber = {n: i for i, n in enumerate(initial_picks)} 
    result = list(map(picknumber.get, order))
    print("El orden adecuado de pick es: ")
    print(result)