import random
import math
from Astar import Astar
from Warehouse import Warehouse
from copy import copy
import matplotlib.pyplot as plt

class Annealing:
    def __init__(self, tempini, tempfin, alph, warehouse): 
        self.tempini = tempini 
        self.tempfin = tempfin
        self.alph = alph
        self.warehouse = warehouse
        self.temperatures = []
        self.costs = []
    
    def astar_path(self, pick_in, pick_fin):
        astar = Astar(pick_in, pick_fin, self.warehouse)
        self.warehouse.clear_map() #el problema estaba en como chequea los lugares que ya visito, agregue esta func para limpiar el mapa despues de cada a*
        return astar.path()     #devuelve el camino de la busqueda entre dos productos

    def get_energy(self, state):            #funcion para conseguir la energia del estado, es decir, la cantidad de nodos 
        energy = 0                           #que visito en total al hacer la busqueda anidada de pj. 5 productos
        
        for i in range (len(state)-1):
            pick1=state[i]
            pick2=state[i+1]
            _, path_len = self.astar_path(pick1,pick2)
            energy += path_len  #se van agregando los caminos entre cada pick
        return energy
    
    def get_neighbour(self, solution):            #toma los puntos de picking generados aleatoriamente y crea un vecino con una permutacion
        rand_neighbours = copy(solution)         #cada vecino es un arreglo de puntos en el almacen, pj 5 productos 

        idx1 = random.randint(1, len(rand_neighbours)-2) #ahora es con 1 y -2 para no cambiar el punto inicial y el final
        idx2 = random.randint(1, len(rand_neighbours)-2)
        
        while idx1 == idx2:
            idx2 = random.randint(1, len(rand_neighbours)-2)
        
        rand_neighbours[idx1], rand_neighbours[idx2] = rand_neighbours[idx2], rand_neighbours[idx1]
        
        """DEPRECATED
        val1= random.choice(rand_neighbours) 
        val2=random.choice(rand_neighbours)
        while val2 == val1:
            val2= random.choice(rand_neighbours)        
        ind1 = rand_neighbours.index(val1)
        ind2 = rand_neighbours.index(val2)
        rand_neighbours.remove(val1)
        rand_neighbours.insert(ind1, val2)
        rand_neighbours.remove(val2)
        rand_neighbours.insert(ind2, val1)"""
        
        return rand_neighbours           #retorna un arreglo similar al inicial pero con una permutacion en el orden de pick

    def simulated_annealing(self, init_state):
        current_temp = self.tempini              #temperatura inicial (alta)
        solution = init_state              #estado actaul: arreglo inicial de picking (producto 1, producto 2,....)
        while current_temp > self.tempfin:
            self.temperatures.append(current_temp)
            self.costs.append(self.get_energy(solution))
            neigh = self.get_neighbour(solution) #generacion de estado vecino 
            energy_diff = self.get_energy(solution) - self.get_energy(neigh) #diferencia de energia entre estados
            if energy_diff > 0: #puede o no cambiar el estado actual (estocasticidad)
                solution = neigh #si es menor lo toma
            elif random.uniform(0,1) < math.exp(energy_diff/current_temp): #si es mayor pero bajo una probabilidad, lo toma (va energy_diff sin signo, el negativo ya lo trae)
                solution = neigh
            current_temp *= self.alph #resta a la temp una constante (funcion de varacion lineal -- puede ser exp o log tambien))
        total_path_length = self.get_energy(solution)
        
        return solution, total_path_length
    
        
    
    
   