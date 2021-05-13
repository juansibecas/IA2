from Warehouse import Warehouse
from Astar import Astar
from Annealing import Annealing
from Orders import Order
from Individuals import Individual
import random

def orders():
    orders=[]
    lines=[]
    with open("orders.txt", 'r') as f:
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
    return orders

def individuals(shelves):
    n=len(shelves)
    individuals=[]
    individuals.append(Individual(random.sample(range(1,n+1),n)))
    return individuals

    
if __name__ == "__main__":
    max_it = 1000 
    columns=10
    rows=9
    warehouse = Warehouse(rows,columns)
    warehouse.create_aisles()
    warehouse.create_shelves()
    orders = orders()
