import math
from copy import copy

class Astar:
    def __init__(self, start, finish, space, it):
        self.start = start
        self.finish = finish
        self.space = space
        self.it = it

    def h_euclid(self, actual, finish, k): #función heuristica, calculamos la distancia euclidiana entre dos puntos.
        v = []
        for i in range(len(actual)):
            v.append(pow((actual[i]-finish[i]),2))
        return math.sqrt(sum(v))*k  #k elegido por usuario segun necesidad. factor de multiplicacion normalmente igual a 1


    def path(self): #Funcion para encontrar el menor camino.
            neighbours=[]  #guardaremos todos los vecinos de la posicion actual
            nodes=[]    #guardaremos todos los nodos - ver class Nodo
            flag=1
            f=0
            prev = Node(self.start, 0, 0, 0)
            g=0
            it = 0
            
            if self.start == self.finish: #termina de una si empieza en el destino
                return [[self.start]]

            while flag:
                it+=1
                g+=1
                neighbours=self.space.find_neighbours(prev.pos)
                
                for j in range(len(neighbours)):
                    f=g+self.h_euclid(neighbours[j], self.finish, 1)      #calculamos la funcion f para cada vecino, g vale una unidad por cada movimiento
                    nodes.append(Node(neighbours[j], f, g, prev))
                
                
                nodes = delete_duplicates(nodes)  #aca hay que quitar duplicados, es decir, nodos de la misma posicion y con un valor igual de f
                
                nodes.sort(key=sort_by_f) #se ordena la lista de nodos de menor a mayor segun f
                
                
                g = nodes[0].level #si el algoritmo vuelve a una rama anterior, vuelve el valor de g al original
                
                prev = copy(nodes[0])
                nodes.pop(0)                    #eliminamos el valor actual de los nodos para que no se pueda volver a el   
                
                if self.finish in neighbours:       #si el final esta dentro de los vecinos, se mueve a el y termina el programa. Llegamos  
                    flag=0
                    
                if it == self.it:   
                    flag=0

            path = []
            path = prev.connect_path(path) 
            path.reverse()
            
            return path

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

