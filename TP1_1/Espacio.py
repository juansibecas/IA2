import random
from copy import copy

class Espacio:
    
    def __init__(self, rev, dx, dim):
        self.rev = rev #largo total del espacio
        self.dx = dx #discretizacion
        self.dim = dim
        self.fixed_coords = 2 #es para generar los obstaculos hago como una "superficie" dejando 2 dimensiones fijas y moviendome en las otras
        global dim #para la funcion de combinacion
        dim = self.dim
        self.obstacles = []
        
    def create_obstacles(self, percent, n): #la idea de esto es generar n obstaculos que c/u sigue la forma de una "superficie"
        temp = []                           #c/u de esas superficies queda "tapada" en un cierto porcentaje
        obstacles_percent = round(percent*pow(self.rev/self.dx, self.dim - self.fixed_coords)/100) #calculo cuantos puntos hay en x% de la sup
        value = []
        index = []
        lst = []
        #TODO GENERAR OBSTACULOS DE OTRA MANERA
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
        
        
        
    def find_neighbours(self, pos):
        neighbours = []
        temp = []
        temp_2 = []
        lst = []
        #-------------------------------------------------
        """
        for a in range(pos[0]- self.dx, pos[0]+2*self.dx, self.dx): #bastante horrible se ve esto pero funciona igual que combinations
            for b in range(pos[1]- self.dx, pos[1]+2*self.dx, self.dx): #por ej si la posicion es n, el for loopea entre n-1 y n+1 (incluido)
                for c in range(pos[2]- self.dx, pos[2]+2*self.dx, self.dx):
                    for d in range(pos[3]- self.dx, pos[3]+2*self.dx, self.dx):
                        for e in range(pos[4]- self.dx, pos[4]+2*self.dx, self.dx):
                            for f in range(pos[5]- self.dx, pos[5]+2*self.dx, self.dx):     
                                neighbours.append([a, b, c, d, e, f]) #todo delete actual position"""
                                
        #arriba y abajo son 2 maneras de hacer lo mismo, la de abajo se ve mas clean pero es mas complicada(quizas demore mucho tiempo)         
        for i in range(self.dim):
            for j in range(self.pos[i]-self.dx, pos[i]+2*self.dx, self.dx):
                lst.append(j)
            temp.append(copy(lst))
            lst.clear()
        temp = combinations(temp)   #genera todas las combinaciones de n-1, n y n+1 de las {dim} coordenadas
        
        for i in temp:  #transformo la lista de listas a lista de tuplas, para poder eliminar los duplicados que quedan
            temp_2.append(tuple(i))
            
        temp_2 = delete_duplicates(temp_2)
        
        for i in temp_2: #transformo de vuelta a lista de listas
            neighbours.append(list(i))
        #-------------------------------------------------
        
        for j in neighbours: #elimino de los vecinos si es un obstaculo
            if j in self.obstacles:
                neighbours.remove(j)
                
        return neighbours
        
    def check_limits(self, n): #funcion para no usar valores que escapen de los limites (0 - {self.rev})
        if n > self.rev:
            return self.rev
        elif n < 0:
            return 0
        else: 
            return n

def delete_duplicates(lst):
    return list(set(lst)) #no se puede con listas anidadas. habria que transformarlas a tuplas


def combinations(pos, acc=[[]] * dim): #una variante para los for anidados que se puede generalizar para diferentes dimensiones
    if len(pos) == 0:
        return acc
    else:
        return combinations(pos[1:], #esto es magia, solo sepan que devuelve la lista de combinaciones
                            acc = \
                            [x + [y] for x in acc for y in pos[0]])