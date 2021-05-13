import random
from copy import copy

class Space:
    
    def __init__(self, rev, dx, dim):
        self.rev = rev #largo total del espacio
        self.dx = dx #discretizacion
        self.dim = dim
        self.obstacles = []
        
    def create_obstacles(self, n, obs_dx): 
        self.obs_dx = obs_dx
        temp = []
        for i in range(n): #creo n obstaculos de la forma [a1, a2, a3, ...]
            for j in range(self.dim):          
                temp.append(random.randrange(0, self.rev, self.dx))
            self.obstacles.append(copy(temp))
            temp.clear()
        
        """#DEPRECATED (complejidad de recursos muy alta)
        #obstacles_percent = round(percent*pow(self.rev/self.dx, self.dim - self.fixed_coords)/100) #calculo cuantos puntos hay en x% de la sup
        for i in range(n):#cambiar esto por otro metodo que no demore tanto. esto crea una lista con cada punto que no se permite, y para 6 dim es una barbaridad
            for j in range(self.dim):
                lst.append(j)
            for j in range(self.fixed_coords):
                value.append(random.randrange(0, self.rev, self.dx))   #varia los indices que se van dejando fijos y asegura que sean distintos
                index.append(random.choice(lst))
                lst.remove(index[j])
                    
            for j in range(obstacles_percent): #genera obstaculos de la forma [x, y, int, int, int, int], x e y fijos
                for k in range(self.dim):          
                    temp.append(random.randrange(0, self.rev, self.dx))
                for k in range(self.fixed_coords):
                    temp[index[k]] = value[k]
                    
                self.obstacles.append(copy(temp))
                temp.clear()
            index.clear()
            value.clear()
            lst.clear()
        """
        
    def find_neighbours(self, pos):
        neighbours = []
        temp = []
        temp_1 = []

        #-------------------------------------------------
        """#DEPRECATED (no era generalizable y se ve bastante feo)
        for a in range(pos[0]- self.dx, pos[0]+2*self.dx, self.dx): #bastante horrible se ve esto pero funciona igual que combinations
            for b in range(pos[1]- self.dx, pos[1]+2*self.dx, self.dx): #por ej si la posicion es n, el for loopea entre n-1 y n+1 (incluido)
                for c in range(pos[2]- self.dx, pos[2]+2*self.dx, self.dx):
                    for d in range(pos[3]- self.dx, pos[3]+2*self.dx, self.dx):
                        for e in range(pos[4]- self.dx, pos[4]+2*self.dx, self.dx):
                            for f in range(pos[5]- self.dx, pos[5]+2*self.dx, self.dx):     
                                neighbours.append([a, b, c, d, e, f]) #todo delete actual position
        """                        
        #arriba y abajo son 2 maneras de hacer lo mismo, la de abajo se ve mas clean y esta generalizada pero es mas complicada(quizas demore mucho tiempo)         
        for dim in range(self.dim): #genero la lista anidada con los valores que se deben combinar [[a-1, a, a+1], [b-1, b, b+1], ...]
            for position in range(pos[dim]-self.dx, pos[dim]+2*self.dx, self.dx): #si pos[dim] es 1, loopea 0, 1 y 2, dx=1
                temp_1.append(position)
            temp.append(copy(temp_1))
            temp_1.clear()
          
        temp = combinations(temp)   #genera todas las combinaciones de n-1, n y n+1 de las {dim} coordenadas
        
        for i in temp:  #transformo la lista de listas a lista de tuplas, para poder eliminar los duplicados que quedan
            temp_1.append(tuple(i))
         
        temp_1 = delete_duplicates(temp_1)
        
        for i in temp_1: #transformo de vuelta a lista de listas
            temp.append(list(i))
        neighbours=copy(temp)
        #-------------------------------------------------
        
        neighbours = self.delete_non_valid_neighbours(temp, neighbours, pos)
    
        return neighbours
        
    
    def delete_non_valid_neighbours(self, neighbours_temp, neighbours, pos): #elimino en base a 3 casos. vecinos que entran en los obstaculos, vecinos que salen de los limites del mapa, y la posicion actual
    
        flag=0
        for neighbour in neighbours_temp: #elimino de los vecinos si esta dentro del obstaculo obs+-obs_dx
            for obstacle in self.obstacles:
                dim_counter=0
                for n in range(self.dim):             #obs_dx es la mitad del ancho del obstaculo en puntos de discretizacion, por eso va multiplicado por self.dx
                    if neighbour[n] <= obstacle[n] + self.obs_dx*self.dx and neighbour[n] >= obstacle[n] - self.obs_dx*self.dx:   #se podria optimizar con generator o iterator   
                        dim_counter+=1 #suma uno para cada dimension en la que el vecino esta dentro de un obstaculo
                    if dim_counter == self.dim: #solo se elimina si el vecino esta dentro del obstaculo en todas las dimensiones
                        neighbours.remove(neighbour)
                        dim_counter=0 #se resetea el contador
                        flag=1
                        break
                if flag == 1: #con confirmar un solo obstaculo ya alcanza para quitar al vecino, y pasar al siguiente en el for neighbour
                    flag=0
                    break
           
        for neighbour in neighbours_temp: #si sale de los limites en cualquier dimension, y este vecino no fue eliminado en el paso anterior, se elimina
            for n in range(self.dim):
                if (neighbour[n] < 0 or neighbour[n] >self.rev) and neighbour in neighbours:
                    neighbours.remove(neighbour)            
        
        if pos in neighbours: #se elimina la posicion actual
            neighbours.remove(pos)
        
        return neighbours

def delete_duplicates(lst):
    return list(set(lst)) #no se puede con listas anidadas. habria que transformarlas a tuplas

                                     
def combinations(pos, acc=[[]]*3): #una variante para los for anidados que se puede generalizar para diferentes dimensiones
    if len(pos) == 0:
        return acc
    else:
        return combinations(pos[1:], #esto es magia, solo sepan que devuelve la lista de combinaciones
                            acc = \
                            [x + [y] for x in acc for y in pos[0]])