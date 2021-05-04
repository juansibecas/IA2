from Almacen import Almacen
from Aestrella import Aestrella
from Annealing import Annealing
import random

def orders():
    orders=open("orders.txt")
    line=orders.readline()
    print(line)

if __name__ == "__main__":
    max_it = 1000 
    columns=13
    rows=16
    store = Almacen(rows,columns)
    map = store.almacen
    shelve=store.crear_pasillo()
    hal=store.crear_estante()
    orders()