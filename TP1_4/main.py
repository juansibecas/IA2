from Almacen import Almacen
from Aestrella import Aestrella
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
    columns=16
    rows=13
    n=10
    store = Almacen(rows,columns)
    map = store.almacen
    hal=store.crear_pasillo()
    shelves=store.crear_estante()
    for i in range(len(shelves)): #En la estanteria le ponemos el valor como lo tenemos en ordenes
        shelves[i]= 'P'+str(i)
        map = warehouse.map
    print(map)
    orders=orders()
    gen=Gen(shelves,n)
    gen.sel_and_rep()