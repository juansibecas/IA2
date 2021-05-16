from Warehouse import Warehouse
from Astar import Astar
from Annealing import Annealing
from Orders import Order
from Gen import Gen
import random

def orders(): #Funcion para leer el archivo de ordenes y separar cada orden
    orders=[]
    lines=[]
    f=open("orders.txt")
    line=(f.readline())
    orders.append(Order(line))
    i=0
    while line != '': #Para indicar que estamos en el fin de la lista
        if line == '\n': #Si solo tenemos \n pasamos a la siguiente orden
            orders[i].setorder(lines) #guardamos en la orden las lineas que teniamos anteriormente y luego las limpiamos
            i+=1
            line=(f.readline())
            orders.append(Order(line))#El primer elemento del archivo es el orden del pedido. lo guardamos aparte
            lines=[]
        else:
            line=f.readline()
            if line != '\n':
                line=line.rstrip('\n')
                lines.append(line)
    #for j in range(i):
        #orders[j].getorder()


if __name__ == "__main__":
    max_it = 1000 
    columns=16 #con 16, 13, 3, 6 tenemos un almacen de 2x5, y cada grupo de estanterias de 5x2 = 100 estanterias
    rows=13
    dx=3
    dy=6
    n=10
    warehouse = Warehouse(rows,columns,dx,dy)
    map = warehouse.warehouse
    aisles=warehouse.create_aisles()
    shelves=warehouse.create_shelves()
    for i in range(len(shelves)): #En la estanteria le ponemos el valor como lo tenemos en ordenes
        shelves[i]= 'P'+str(i)
    map = warehouse.map
    print(map)
    orders=orders()
    gen=Gen(shelves,n)
    best=gen.sel_and_rep() #El mejor recorrido posible
    print(best)