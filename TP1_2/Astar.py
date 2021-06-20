import math
from copy import copy
class Astar:
    def __init__(self, start, finish, warehouse):
        self.start = start
        self.finish = finish
        self.warehouse = warehouse
        
        if self.start in self.warehouse.shelves:
            self.start = self.warehouse.assign_aisle_to_shelf(self.start)
            print("start position is a shelf, changed to", self.start)
            
        if self.finish in self.warehouse.shelves:
            self.finish = self.warehouse.assign_aisle_to_shelf(self.finish)
            print("finish position is a shelf, changed to", self.finish)
        
        
    def h_euclid(self, actual, finish, k): #función heuristica, calculamos la distancia euclidiana entre dos puntos.
        v = []  #la cambie para que sea mas general y se pueda volver a usar
        for i in range(len(actual)):
            v.append(pow((actual[i]-finish[i]),2))
        return math.sqrt(sum(v))*k #multiplicamos por 2 para que tenga mas peso frente a la g. 

    def h_manhattan(self, actual, finish): #heuristica manhattan
        v = []
        for i in range(len(actual)):
            v.append(abs(actual[i] - finish[i]))
        return sum(v)
      
    def path(self, column, row): #Funcion para encontrar el menor camino.
        
        if self.start == self.finish: #termina de una si empieza en el destino
            return [[self.start]], 0
        
        db_check = int(self.warehouse.check_db(self.start, self.finish)) #devuelve -1 si no se calculo todavia
        
        if db_check > 0: #chequea si ese caso ya esta calculado (cuando no esta calculado, devuelve -1)
            return 0, db_check
        
        neighbours=[]   #guardaremos todos los vecinos de la posicion actual
        nodes=[]        #guardaremos todos los nodos - ver class Nodo
        f=0
        prev = Node(self.start, 0, 0, 0)
        g=0

        while True:
            neighbours=self.warehouse.find_neighbours(prev.pos, self.finish)
            
            if self.finish in neighbours:                   #si el final esta dentro de los vecinos, se mueve a el y termina el programa     
                prev = Node(self.finish, 0, "end", prev)    #le pongo cualquier cosa que no sea 0 al nivel
                break
            
            for j in range(len(neighbours)):
                g = prev.level + 1
                f= g + self.h_manhattan(neighbours[j], self.finish) #calculamos la funcion f para cada vecino, g vale una unidad por cada movimiento
                nodes.append(Node(neighbours[j], f, g, prev))
            
            nodes = delete_duplicates(nodes)    #aca hay que quitar duplicados, es decir, nodos de la misma posicion y con un valor igual de f
            
            nodes.sort(key=sort_by_f)           #se ordena la lista de nodos de menor a mayor segun f
            

            
            prev = copy(nodes[0])
            nodes.pop(0)                        #eliminamos el valor actual de los nodos para que no se pueda volver a el   
            
                
        path = []
        path = prev.connect_path(path) 
        path.reverse()
        path_len = len(path)-1 #-1 porque en path se incluye la posicion inicial
        
        for i in path:
            self.warehouse.map[i[0], i[1]] = 1 #1 es por donde pasa
        
        self.warehouse.write_to_db(self.start, self.finish, path_len)  #escribe lo calculado
        
        return path, path_len

def delete_duplicates(lst):
    return list(set(lst))


def sort_by_f(nodo):
    return nodo.f

class Node:
    def __init__(self, pos, f, level, prev):  
        self.pos = pos
        self.f = f
        self.level = level #es el valor de g, los espacios recorridos hasta llegar aca
        self.prev = prev #guarda el nodo previo
        
    def __eq__(self, other): #eq y hash se definen para que el object sea hashable, y se pueda usar set() para eliminar duplicados
        return self.pos == other.pos and self.f == other.f
    
    def __hash__(self):
        return hash((tuple(self.pos), self.f))
    
    def connect_path(self, path): #se conecta un nodo al previo y asi sucesivamente hasta llegar al inicio del recorrido
        path.append(self.pos)
        if self.level == 0:
            return path
        else:
            return self.prev.connect_path(path)