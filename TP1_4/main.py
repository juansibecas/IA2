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
            if line != '\n':
                line=line.rstrip('\n')
                lines.append(line)
    #for j in range(i):
        #orders[j].getorder()

def individuals(shelves,n):
    i=len(shelves)
    individuals=[]
    for j in range(n):
        individuals.append(Individual(random.sample(range(0,i),i)))
        #individuals[j].getind()

if __name__ == "__main__":
    max_it = 1000 
    columns=13
    rows=16
    n=10
    store = Almacen(rows,columns)
    map = store.almacen
    shelves=store.crear_pasillo()
    for i in range(len(shelves)):
        shelves[i]= 'P'+str(i)
    print(shelves[6])
    hal=store.crear_estante()
    orders=orders()
    individuals(shelves,n)