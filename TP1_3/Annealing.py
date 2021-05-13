import random
import math
from Astar import Astar
from Warehouse import Warehouse

class Annealing:
    def __init__(self, tempini, tempfin, alph, neighbours, rows, columns, dx, dy): 
        self.tempini = tempini 
        self.tempfin = tempfin
        self.alph = alph
        self.neighbours = neighbours
        self.rows = rows
        self.columns = columns
        self.wh_dx = dx
        self.wh_dy = dy
    
<<<<<<< HEAD
    def astar_path(self,pick_in,pick_fin):              #decidi crear un almacen en cada intervalo de 
        warehouse = Almacen(self.rows,self.columns)    #picking porque las restricciones de vecinos podian 
        warehouse_map =  warehouse.almacen              #mamar la busqueda siguiente
        hall = warehouse.crear_pasillo()
        shelf = warehouse.crear_estante()
        astar = Aestrella(pick_in,pick_fin,warehouse_map,hall,shelf)
        return astar.camino(self.columns,self.rows)     #devuelve el camino de la busqueda entre dos productos
=======
    def astar_path(self, pick_in, pick_fin):              #decidi crear un almacen en cada intervalo de 
        warehouse = Warehouse(self.rows, self.columns, self.wh_dx, self.wh_dy)    #picking porque las restricciones de vecinos podian 
                                                          #mamar la busqueda siguiente
        warehouse.create_aisles()
        warehouse.create_shelves()
        astar = Astar(pick_in, pick_fin, warehouse)

        return astar.path()     #devuelve el camino de la busqueda entre dos productos
>>>>>>> 955967fc2007dea5c92ecb29cef28f3f778a0183

    def get_energy(self,state):            #funcion para conseguir la energia del estado, es decir, la cantidad de nodos 
        path=[]                            #que visito en total al hacer la busqueda anidada de pj. 5 productos
        for i in range (len(state)-1):
            pick1=state[i]
            pick2=state[i+1]
            path.extend(self.astar_path(pick1,pick2))  #se van agregando los caminos entre cada pick
        return len(path)
    
    def get_neighbour(self):            #toma los puntos de picking generados aleatoriamente y crea un vecino con una permutacion
        rand_neighbours = self.neighbours         #cada vecino es un arreglo de puntos en el almacen, pj 5 productos 
        val1= random.choice(rand_neighbours) 
        val2=random.choice(rand_neighbours)
        while val2 == val1:
<<<<<<< HEAD
            val2= random.choice(rand_neigh)        
        ind1 = rand_neigh.index(val1)
        ind2 = rand_neigh.index(val2)
        rand_neigh.remove(val1)
        rand_neigh.insert(ind1, val2)
        rand_neigh.remove(val2)
        rand_neigh.insert(ind2, val1)
        print (rand_neigh)
        return rand_neigh             #retorna un arreglo similar al inicial pero con una permutacion en el orden de pick
=======
            val2= random.choice(rand_neighbours)        
        ind1 = rand_neighbours.index(val1)
        ind2 = rand_neighbours.index(val2)
        rand_neighbours.remove(val1)
        rand_neighbours.insert(ind1, val2)
        rand_neighbours.remove(val2)
        rand_neighbours.insert(ind2, val1)
        return rand_neighbours           #retorna un arreglo similar al inicial pero con una permutacion en el orden de pick
>>>>>>> 955967fc2007dea5c92ecb29cef28f3f778a0183

    def simulated_annealing(self, init_state):
        current_temp= self.tempini              #temperatura inicial (alta)
        current_state = init_state              #estado actaul: arreglo inicial de picking (producto 1, producto 2,....)
        solution = current_state

        while current_temp > self.tempfin:      
            neigh = self.get_neighbour() #generacion de estado vecino 
            energy_diff = self.get_energy(current_state) - self.get_energy(neigh) #diferencia de energia entre estados
            if energy_diff > 0: #puede o no cambiar el estado actual (estocasticidad)
                solution = neigh #si es menor lo toma
            else:
                if random.uniform(0,1) < math.exp(- energy_diff/current_temp): #si es mayor pero bajo una probabilidad, lo toma
                    solution = neigh
            current_temp-=self.alph #resta a la temp una constante (funcion de varacion lineal -- puede ser exp o log tambien)
            print(solution)
        return solution 
    
        
    
    
   