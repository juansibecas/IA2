from Almacen import Almacen
from Aestrella import Aestrella
from Annealing import Annealing
import random

def orders():
    line=[]
    orders=open("orders.txt")
    line.append(orders.readline())
    i=0
    while line[i] != '':
        i+=1
        line.append(orders.readline())

def individuals(shelves):
    
    n=len(shelves)
    individual=random.sample(range(1,n+1),n)
    print(individual)
    
if __name__ == "__main__":
    max_it = 1000 
    columns=13
    rows=16
    store = Almacen(rows,columns)
    map = store.almacen
    shelves=store.crear_pasillo()
    hal=store.crear_estante()
    orders()
    individuals(shelves)
