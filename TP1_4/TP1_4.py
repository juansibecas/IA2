from Warehouse import Warehouse
from Astar import Astar
from Annealing import Annealing
from Orders import Order
from Gen import Gen
import random

def orders(init_pos): #Funcion para leer el archivo de ordenes y separar cada orden
    orders=[]
    lines=[]
    with open('orders.txt', 'r') as f:
        line=(f.readline())
        orders.append(Order(line, init_pos))
        i=0
        while line != '': #Para indicar que estamos en el fin de la lista   
            if line == '\n': #Si solo tenemos \n pasamos a la siguiente orden
                orders[i].setorder(lines) #guardamos en la orden las lineas que teniamos anteriormente y luego las limpiamos
                i+=1
                line=(f.readline())
                orders.append(Order(line, init_pos))#El primer elemento del archivo es el orden del pedido. lo guardamos aparte
                lines=[]
            else:
                line=f.readline()
                if line != '\n':
                    line=line.rstrip('\n')
                    lines.append(line)
        #for j in range(i):
            #orders[j].getorder()
        orders_length = len(orders)
        orders.remove(orders[orders_length-1]) #al final se agregaba una orden sin nada, en vez de arreglarlo la quito asi y a la mierda
    return orders


if __name__ == "__main__":
    max_it = 1000 
    columns=16 #con 16, 13, 3, 6 tenemos un almacen de 2x5, y cada grupo de estanterias de 5x2 = 100 estanterias
    rows=13
    dx=3
    dy=6
    warehouse = Warehouse(rows,columns, dx, dy)
    aisles=warehouse.create_aisles()
    shelves=warehouse.create_shelves()
    init_pos = [0,0]
    orders=orders(init_pos)
    
    temp_ini_annealing = 20
    temp_fin_annealing = 0.1
    alpha_annealing = 0.5
    
    population_length = 10
    it = 5
    max_time_in_hours = 5
    tolerance = 1
    genetic_algorithm = Gen(population_length, warehouse, orders, temp_ini_annealing, temp_fin_annealing, alpha_annealing)
    genetic_algorithm.population_init()
    genetic_algorithm.GA(it, max_time_in_hours/3600, tolerance)

    