from Almacen import Almacen
from Aestrella import Aestrella
from Annealing import Annealing
from Orders import Order
from Individuals import Individual
import random

def orders():
    orders=[]
    lines=[]
    f=open("orders.txt")
    line=(f.readline())
    orders.append(Order(line))
    i=0
    while line != '':
        if line == '\n':
            orders[i].setorder(lines)
            i+=1
            line=(f.readline())
            orders.append(Order(line))
            lines=[]
        else:
            line=f.readline()
            if line != '\n': lines.append(line)

def individuals(shelves):
    n=len(shelves)
    individuals=[]
    individuals.append(Individual(random.sample(range(1,n+1),n)))

    
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
